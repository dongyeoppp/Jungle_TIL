## 7주차 웹 서버 만들기 키워드 정리 및 알고리즘 문제 풀이

- 2024 - 05 - 09 (53일차)

#### 알고리즘 문제 풀이

- 5430번 [AC](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week07/bk_5430.py)

#### tiny 서버   
* [tiny 서버 구현](https://github.com/dongyeoppp/webproxy-lab/tree/main/tiny)   


* HTTP 트랜 잭션 처리   
    ```
    void doit(int fd)
    {
    int is_static;
    struct stat sbuf;
    char buf[MAXLINE], method[MAXLINE], uri[MAXLINE], version[MAXLINE];
    char filename[MAXLINE], cgiargs[MAXLINE];
    rio_t rio;

    Rio_readinitb(&rio, fd);                // rio 구조체를 초기화, fd에 대한 읽기작업을 수행할 수 있도록 설정 (confd를 연결하여 rio에 저장)
    if (!Rio_readlineb(&rio, buf, MAXLINE)) // 요청 라인 읽기
        return;
    printf("Request headers:\n");
    printf("%s", buf);
    sscanf(buf, "%s %s %s", method, uri, version);
    if (strcasecmp(method, "GET") & strcasecmp(method, "HEAD"))
    { // GET 메서드만 지원   // 다른 메서드를 요청하면 error 메시지를 출력
        clienterror(fd, method, "501", "Not implemented", "Tiny does not implement this method", version);
        return;
    }

    read_requesthdrs(&rio); // http 요청 메시지의 헤더 부분을 읽어드린다. (return x)

    is_static = parse_uri(uri, filename, cgiargs); // uri를 파일 이름과 인자 스트링으로 분석  // is_static => 동적인지 정적인지를 확인 .. // cgiargs : cgi 인자 스트링
    if (stat(filename, &sbuf) < 0)
    { // filename -> 해당 파일이 디스크 상에 있지 않을 경우 error 출력
        clienterror(fd, filename, "404", "Not found", "Tiny couldn't find this file", version);
        return;
    }

    if (is_static)
    { // 정적 컨텐츠일 경우
        if (!(S_ISREG(sbuf.st_mode)) || !(S_IRUSR & sbuf.st_mode))
        { // 보통 파일 이라는 것 or 읽기 권한 있는지 검증 .. 하나라도 false라면 error 출력
        clienterror(fd, filename, "403", "Forbidden", "Tiny couldn't read the file", version);
        return;
        }
        serve_static(fd, filename, sbuf.st_size, version, method); // 정적 컨텐츠 client에 제공
    }
    else
    { // 동적 컨텐츠일 경우
        if (!(S_ISREG(sbuf.st_mode)) || !(S_IXUSR & sbuf.st_mode))
        { // 보통 파일 이라는 것 or 실행 권한 있는지 검증 .. 하나라도 false라면 error 출력
        clienterror(fd, filename, "403", "Forbidden", "Tiny couldn't run the CGI program", version);
        return;
        }
        serve_dynamic(fd, filename, cgiargs, version, method); // 동적 컨텐츠 client에 제공
    }
    }
    ```   
* HTTP URI 분석  
    ```
    int parse_uri(char *uri, char *filename, char *cgiargs) // 주어진 uri를 filename과 cgiargs로 분석
    {
    char *ptr;

    if (!strstr(uri, "cgi-bin"))
    {                      // 정적 컨텐츠일 경우  // strstr(a,b) -> a 문자열에서 b문자열 있는지 검색
        strcpy(cgiargs, ""); // cgi 인자 스트링 지워주기  // strcpy(a,b) -> a는 b 문자열을 복사한 값이 들어가게 된다.
        strcpy(filename, ".");
        strcat(filename, uri);           // strcat(a,b) -> a문자열에 b문자열 이어붙이기   // 현재 작업 디렉토리를 기준으로 상대적인 경로를 찾는다.
        if (uri[strlen(uri) - 1] == '/') // '/'으로 uri문자열이 끝날 경우 기본파일 "home.html"을 filename에 붙여준다.
        strcat(filename, "home.html");
        return 1;
    }
    else
    {                        // 동적 컨텐츠
        ptr = index(uri, '?'); // uri에서 특정문자 '?'가 처음으로 나타나는 위치를 찾아준다.
        if (ptr)               // ptr이 null이 아닐경우
        {
        strcpy(cgiargs, ptr + 1); // ptr 이후의 문자열을 cgiargs에 복사한다.
        *ptr = '\0';              // ptr이 가리키고 있는 '?' 문자열을 '\0' 문자열로 바꿔주어 해당 위치를 기준으로 문자열을 나눈다.
        }
        else                   // ptr이 null일 경우
        strcpy(cgiargs, ""); // cgiargs를 빈 문자열로 설정
        strcpy(filename, "."); // 상대 경로 찾기
        strcat(filename, uri); // uri는 널 문자를 기준으로 나눈 앞 부분이 filename에 이어 붙는다. (쿼리 문자열은 들어가지 않는다.)
        return 0;
    }
    }
    ```   
* 정적 컨텐츠를 클라이언트에게 서비스 하기   
    ```
    /* 정적 컨텐츠를 클라이언트에게 서비스 하기*/
    void serve_static(int fd, char *filename, int filesize, char *version, char *method)
    {
    int srcfd;
    char *srcp, filetype[MAXLINE], buf[MAXBUF];

    /*클라이언트에게 응답 헤더 보내기*/
    get_filetype(filename, filetype);       // file type 결정하기
    sprintf(buf, "%s 200 OK\r\n", version); // sprintf()는 buf
    sprintf(buf, "%sServer: Tiny Web Server\r\n", buf);
    sprintf(buf, "%sConnection: close\r\n", buf);
    sprintf(buf, "%sContent-length: %d\r\n", buf, filesize);
    sprintf(buf, "%sContent-type: %s\r\n\r\n", buf, filetype);

    Rio_writen(fd, buf, strlen(buf)); // client에게 buf 데이터 전송
    printf("Response headers:\n");
    printf("%s", buf);

    /*클라이언트에게 응답 body 보내기*/
    if (strcasecmp(method, "HEAD"))
    {
        srcfd = Open(filename, O_RDONLY, 0);                        // 지정된 파일을 읽기모드(O_RDONLY: 읽기 전용 파일 열기)로 전환하고, 해당 파일의 식별자 받아오기 // Open(열려고 하는 대상 파일 이름, 파일을 열 때 적용되는 열기 옵션, 파일 열때 접근 권한 설명)
        srcp = Mmap(0, filesize, PROT_READ, MAP_PRIVATE, srcfd, 0); // 파일을 메모리에 매핑  // srcp = 매핑된 메모리의 시작 주소
        Close(srcfd);
        Rio_writen(fd, srcp, filesize); // 매핑된 파일의 내용 클라이언트에 전송
        Munmap(srcp, filesize);         // 메모리 매핑해제
    }

    /*숙제 11.9 malloc, rio_readn, rio_writen 사용하기*/
    // 원래 코드는 파일을 메모리에 매핑하여 전송하지만 이 코드에선 파일을 메모리로 읽어들인 후 전송한다.
    // srcfd = Open(filename, O_RDONLY, 0);
    // srcp = (void*)malloc(sizeof(void) *filesize);
    // Rio_readn(srcfd,srcp,filesize);    // rio_readlineb는 파일에서 한줄 씩 데이터를 읽어 버퍼(메모리)에 저장하는 반면, rio_readn은 정확한 바이트 수만큼 데이터를 읽어 버퍼(메모리)에 저장한다.
    // Close(srcfd);
    // Rio_writen(fd, srcp, filesize);
    // free(srcp);
    }
    ```   

* 동적 컨텐츠를 클라이언트에 제공   
    ```
    /* 동적 컨텐츠를 클라이언트에 제공 */
    // 자식 프로세스를 fork하고, 그 후에 cgi 프로그램을 자식의 컨텍스트에서 실행하며 모든 종류의 동적 컨텐츠를 제공한다.
    void serve_dynamic(int fd, char *filename, char *cgiargs, char *version, char *method)
    {
    char buf[MAXLINE], *emptylist[] = {NULL};
    // 클라이언트에 성공 응답
    sprintf(buf, "%s 200 OK\r\n", version);
    Rio_writen(fd, buf, strlen(buf));
    sprintf(buf, "Server: Tiny Web Server\r\n");
    Rio_writen(fd, buf, strlen(buf)); // buf에 데이터는 클라이언트에 전송
    // fork : 현재 프로세스의 복제본 생성, 부모 프로세스와 자식 프로세 두 개의 별도의 프로세스를 동시에 실행시키는 시스템 콜
    // 부모 프로세스는 자식의 PID(Process ID)를, 자식 프로세스는 0을 반환한다.
    if (Fork() == 0)
    {                                     // cgiargs에는 '?'이후의 문자열이 들어온다.
        setenv("QUERY_STRING", cgiargs, 1); // 환경 변수 설정 // QUERY_STRING은 설정하려는 환경 변수의 이름, cgiarfs는 설정할 환경 변수의 값, 마지막 매개변수는 덮어쓰기 여부를 나타내는 플래그로 이 값이 1일 경우 해당 변수가 이미 설정되어 있더라도 덮어쓰게 된다.
        setenv("REQUEST_METHOD", method, 1);
        Dup2(fd, STDOUT_FILENO);              // 파일 디스크립터를 복제하는 함수  // 표준 출력(STDOUT_FILENO)을 클라이언트 소켓으로 재지정한다. -> CGI 프로그램이 생성하는 모든 표준 출력은 클라이언트로 전송된다.
        Execve(filename, emptylist, environ); // cgi 프로그램을 로드하고 실행 , 프로그램의 출력은 바로 클라이언트로 감
    }
    Wait(NULL); // 부모 프로세스가 자식 프로세스가 종료 될 때까지 대기한다.
    }
    ```   

