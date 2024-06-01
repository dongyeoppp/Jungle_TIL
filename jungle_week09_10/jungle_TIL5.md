## 9주차 pintos USER PROGRAMS 및 알고리즘 문제 풀이

- 2024 - 05 -29 (73일차)   

#### 프로세스 계층 구조

- 프로세스 간의 부모 자식 관계를 구현하고, 부모가 자식 프로세스의 종료를 대기하는 기능 구현
- 프로세스 디스크립터에 부모와 자식 필드를 추가하고, 이를 관리하는 함수 구현

- 프로세스 디스크립터(thread 구조체) 정보 추가

  - pintos 운영체제는 하나의 프로세스의 하나의 스레드만을 가지고 있기 때문에 프로세스와 스레드의 구분이 없다고 봐도 무방하다. (프로세스 디스크립터 = 스레드)

    ```
    struct thread{
        struct thread *parent_process; // 부모 프로세스 디스크립터를 가리키는 필드 추가
        struct list_elem c_elem;	   // 자식 리스트 element
        struct list child_list;		   // 자식 리스트
        bool is_program_loaded;		   // 프로세스의 프로그램 메모리 적재 유무
        bool is_program_exit;		   // 프로세스 종료 유무 확인
        struct semaphore sema_load;	   // load 세마포어
        struct semaphore sema_exit;	   // exit 세마포어
        int exit_status;			   // exit 호출 시 종료 status

        struct file *fd_table[MAX_FD]; // 파일 디스크립터 테이블
        int max_fd;					// 현재 테이블에 존재하는 fd값의 최대값 +1;
    }
    ```

  - 구조체에 선언한 정보 초기화 (thread_create)

    ```
    struct thread *curr = thread_current();			  // 현재 실행중인 프로세스가 부모 프로세스이다.
    t->parent_process = curr;						  // 부모 프로세스 저장
    t->is_program_loaded = 0;						  // 프로그램이 로드되지 않음
    t->is_program_exit = 0;							  // 프로그램이 종료되지 않음
    sema_init(&t->sema_load, 0);					  // load 세마포어 0으로 초기화
    sema_init(&t->sema_exit, 0);					  // exit 세마포어 0으로 초기화
    list_push_back(&curr->child_list, &t->c_elem); // 부모 프로세스의 자식리스트에 추가

    t->max_fd= 3;		// fd 값 초기화

    ```

  - 자식 리스트를 tid로 검색하여 해당 프로세스 디스크립터를 반환            
    ```
    // 자식리스트를 tid로 검색하여 해당 프로세스 디스크립터(thread)를 반환 
    struct thread *get_child_process (int tid){
        struct thread *t = thread_current();
        if(!tid){
            return NULL;
        }
        else{
            struct list_elem *child_list_first = list_begin(&t->child_list);
            while(child_list_first != list_end(&t->child_list)){
                struct thread *first_thread = list_entry(child_list_first, struct thread, c_elem);
                if (first_thread->tid == tid){
                    return first_thread;
                }
                child_list_first = list_next(child_list_first);   
            }
            return NULL;
        }
    }
    ```   
