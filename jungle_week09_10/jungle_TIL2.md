## 9주차 pintos USER PROGRAMS 및 알고리즘 문제 풀이

- 2024 - 05 -22 (66일차)   

#### 알고리즘 문제 풀이   
* 10026번 [적록색약](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week09/bk_10026.py)    

#### pintos - argument passing   
* purpose   
    * ```echo x y c```라는 문자열을 파일이름과 인자들을 passing 해서 전달해야한다. passing 된 값들은 user stack에 저장되는데 사용된다. 
* 테스트 실행 방법   
    * ```/userprog/build```로 이동   
    * ```make``` 이후 ``` pintos --fs-disk filesys.dsk -p tests/userprog/args-single:echo -- -q -f run 'echo x y z'```입력하여 hex_dump 출력값이 나오는지 확인   
     * 이후 과제에서 작성할 process_wait함수에 임의로 무한루프를 만들어야 hex_dump 출력을 하여 테스트를 확인할 수 있었다.      
* chellenge         
    * process_exec   
        ```
        palloc_free_page(file_name);
        if (!success)
            return -1;
        ```   
        * 왜 위의 코드 이전에 argument_stack()으로 parse값을 넘겨줘야 하는가   
            * file_name을 passing해서 얻은 토큰들을 복사 없이 그대로 저장하는 경우 토큰들은 여전히 원본 문자열이 위치한 메모리 공간을 참조한다.   
            * 그러므로 원본 문자열이나 토큰들 중 하나가 메모리에서 해제되면 다른 값들도 영향을 주기 때문에 parse값이 제대로 전달되지 않을 수 있다.   
            * 원본 문자열에 대한 메모리 공간을 포인터로 공유하고 있기 때문에 한 쪽이 변경되면 다른 쪽에도 영향을 주게 된다.    
            * 영향을 받지 않게 하기 위해선 각 토큰에 대한 복사본을 만들어 저장해야 한다.    
                ```
                parse[count] = palloc_get_page(0); // 토큰의 복사본을 저장할 메모리 할당
                strlcpy(parse[count], token, PGSIZE); // 토큰의 내용을 복사하여 parse 배열에 저장
                count++;
                ```    
* process_create_initd    
    * 매개변수로 주어진 file_name을 파싱하여 첫번째 인자, 파일 이름을 thread_create에 전달한다.   
        ```
        // user 영역의 첫 번째 프로그램인 "initd"를 file_name에서 로드하여 시작  
        tid_t process_create_initd(const char *file_name)
        {
            char *fn_copy;
            tid_t tid;

            /* Make a copy of FILE_NAME.
            * Otherwise there's a race between the caller and load(). */
            fn_copy = palloc_get_page(0);
            if (fn_copy == NULL)
                return TID_ERROR;
            strlcpy(fn_copy, file_name, PGSIZE); // fn_copy에 file_name copy
            /* add code - gdy_pro2*/
            char *token, *save_ptr, *new_file_name;
            for (token = strtok_r(file_name, " ", &save_ptr); token != NULL; token = strtok_r(NULL, " ", &save_ptr))
            {
                new_file_name = token; // 첫번째 인자 -> 파일 이름
                break;
            }

            // printf("new_filename: %s\n", new_file_name);
            // printf("fn_copy: %s\n", fn_copy);
            /* add code - gdy_pro2*/
            /* Create a new thread to execute FILE_NAME. */
            tid = thread_create(new_file_name, PRI_DEFAULT, initd, fn_copy); // new_file_name을 매개변수로 재 설정, fn_copy 값에는 passing 되지 않은 값이 들어간다.
            if (tid == TID_ERROR)
                palloc_free_page(fn_copy);
            return tid;
        }
        ```    
* process_exec   
    * 주어진 매개변수 f_name을 파싱하여 파일이름은 load에 전달하고 파싱한 인자들을 담은 ```parse```는 argument_stack함수에 전달한다.  
        ```
        int process_exec(void *f_name)
        {
            char *file_name = f_name;
            bool success;

            /* We cannot use the intr_frame in the thread structure.
            * This is because when current thread rescheduled,
            * it stores the execution information to the member. */
            struct intr_frame _if;
            _if.ds = _if.es = _if.ss = SEL_UDSEG;
            _if.cs = SEL_UCSEG;
            _if.eflags = FLAG_IF | FLAG_MBS;

            /* We first kill the current context */
            process_cleanup();

            /* And then load the binary */
            /* add code - gdy_pro2*/
            /* 문자열 파싱*/
            char *token, *save_ptr;
            int count = 0;
            char *parse[128]; // 파일이름 + 인자 저장x
            for (token = strtok_r(file_name, " ", &save_ptr); token != NULL;
                token = strtok_r(NULL, " ", &save_ptr))
            {
                parse[count] = token;
                // printf("parse1: %s \n", parse[count]);
                count++;
                
            }
            /* add code - gdy_pro2*/
            /* 프로그램을 메모리에 적재 */
            success = load(parse[0], &_if); // load에 파일이름만 넘겨준다.
            /* add code - gdy_pro2*/
            if (!success){
                palloc_free_page(file_name);
                return -1;
            }

            argument_stack(parse, count, &_if.rsp); // 파싱한 문자들을 담은 배열(parse), 인자의 개수(count), 스택 포인터(rsp)를 넣어준다.
            // 메모리 내용을 16진수로 화면에 출력한다. (유저 스택에 인자를 저장 후 유저 스택 메모리 확인)
            hex_dump(_if.rsp, _if.rsp, USER_STACK - _if.rsp, true);

            /* add code - gdy_pro2*/

            /* If load failed, quit. */
            // argument_stack으로 parse를 전달해준 이후에 palloc_free_page를 통해 file_name이 가리키는 메모리를 해제한다.
            palloc_free_page(file_name);

            /* Start switched process. */
            do_iret(&_if);
            NOT_REACHED();
        }
        ```    
* argument_stack    
    * user stack에 파싱한 인자와 그 인자들의 스택 주소를 넣어준다.    
        ```
        // parse = 프로그램 이름과 인자가 저장된 메모리, count = 인자의 개수, rsp = 스택 포인터를 가리키는 주소 값
        /* user stack에 파싱된 토큰을 저장하는 함수 */
        void argument_stack(char **parse, int count, void **rsp)
        {
            char *arg_ptr[count]; // user_stack의 주소 저장할 것 이다.
            size_t len;
            // 파일이름과 인자 push
            for (int i = count - 1; i >= 0; i--) // parse에 담긴 인자를 뒤에서 부터 stack에 넣는다.
            {
                len = strlen(parse[i]) + 1;
                *rsp -= len;
                memcpy(*rsp, parse[i], len);
                arg_ptr[i] = *rsp;
            }

            // 정렬을 위한 패딩 추가
            uintptr_t stack_alignment = (uintptr_t)(*rsp) % 8; // stack_alignment은 8비트(1바이트)
            if (stack_alignment != 0)
            {
                *rsp -= stack_alignment;		  // padding 하나당 1바이트로 정렬을 위해 그만큼 rsp를 감소시킨다.
                memset(*rsp, 0, stack_alignment); // 늘린 rsp만큼의 stack 공간을 0으로 채운다.
            }
            // 문자열이 종료되었음을 알려주는 0 push
            *rsp -= sizeof(char *);		// sizeof(char *) 은 8바이트 (아키텍처 마다 달라질 수 있음)
            *(char **)(*rsp) = 0; 

            // 인자 주소 push
            for (int i = count-1 ; i >= 0; i--)
            {
                *rsp -= sizeof(char *);
                *(char **)(*rsp) = arg_ptr[i];
            }
            // argv 포인터를 push

            // char **argv_ptr = *rsp;
            // *rsp -= sizeof(char **);
            // *(char ***)(*rsp) = argv_ptr;


            // argc push

            // *rsp -= sizeof(int);
            // *(int *)(*rsp) = count;

            // return address(fake address)  0 push
            
            *rsp -= sizeof(void *);
            *(void **)(*rsp) = 0;
        }
        ```     

    
    

