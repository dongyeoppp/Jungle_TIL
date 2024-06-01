## 9주차 pintos USER PROGRAMS 및 알고리즘 문제 풀이

- 2024 - 05 -23 (67일차)    

#### 알고리즘 문제 풀이   
* 2004번 [조합 0의 개수](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week09/bk_2004.py)   
* 1339번 [단어 수학](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week09/bk_1339.py)   
* 14501번 [퇴사](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week09/bk_14501.py)   
* 5427번 [불](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week09/bk_5427.py)     

#### pintos system call   
* kernel 모드 : 메모리, 하드웨어 및 해당 리소스에 직접 액세스 할 수 있다.   
* 프로그램이 커널 모드에서 실행 될 때 해당 프로그램이 실행중에 충돌이 발생하면 전체 시스템이 충돌하거나 정지된다.   
* 프로그램이 사용자 모드에서 실행 될 때 충돌이 발생하더라도 프로그램이 사용자 모드에서 실행 중이면 전체 시스템이 충돌하지 않거나 전체 시스템이 정지되지 않는다.    
* 프로그램은 사용자 모드에서 더 안전하므로 대부분의 프로그램은 사용자 모드에서 실행된다.   
* 사용자 모드에서 커널 모드로 전환되는 것과 커널 모드에서 사용자 모드로 다시 전환하는 경우 에도 이를  ```context switching```이라고 한다.   
* 프로그램이 해당 리소스에 액세스하거나 커널 모드로 들어가기 위해 호출하는 호출을 ```system call```이라고 한다.   

* pid와 tid   
    * pid   
        * 프로세스를 고유하게 식별하는 번호 (프로세스를 생성하면 운영체제는 해당 프로세스에 유일한 'pid'를 할당)   
    * tid       
        * 스레드를 고유하게 식별하는 번호 (각각의 스레드에는 고유한 'tid'를 할당)   
    * pintos 운영체제에서의 pid와 tid   
        * 프로세스와 스레드는 동일한 'struct thread' 구조체로 표현되므로 'pid'와 'tid'는 동일한 값으로 사용될 수 있다.         

