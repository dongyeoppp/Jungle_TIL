## 9주차 pintos VIRTUAL MEMORY 및 알고리즘 문제 풀이

- 2024 - 06 - 02 (77일차)     

#### 알고리즘 문제 풀이   
* 2410번 [2의 멱수의 합]()   

#### pintos VIRTUAL MEMORY    
* page table의 크기가 너무 클 경우     
    * page table이 크면 많은 메모리 공간을 차지하게 된다.   
* 멀티 레벨 페이지 테이블   
    * 페이지 테이블을 페이지 크기 단위로 나눈다.   
    * 페이지 테이블의 페이지가 유효하지 않은 항목만 있다면 해당 페이지를 할당하지 않는다.   
    * ```페이지 디렉토리```라는 자료구조를 사용하여 페이지 테이블의 각 페이지의 할당 여부(valid)와 위치를 파악한다.   
        * 페이지 디렉토리는 valid와 PFN을 가진다.   
* 메모리가 참조되는 과정   
    * 프로세스가 가상메모리 참조를 생성   
    * 하드웨어가 가상주소에서 vpn을 추출한 후 TLB에 해당 정보가 있는지 검사한다.  
        * TLB에 해당 페이지가 있을 경우 (TLB 히트)    
            * 물리 주소를 얻은 후 메모리로 가져온다.  (매우 빠름)   
        * TLB에 해당 페이지가 없을 경우 (TLB 미스)   
            * VPN을 인덱스로 하는 page table 메모리에서 PTE를 추출한다.  
            * 해당 페이지 테이블 항목이 유효하고, 해당 페이지가 물리 메모리에 존재하면 (present bit가 1일 경우) 하드웨어는 PTE에서 PFN을 추출하여 TLB에 탑재한다.   
            * TLB 탑재 후 명령어를 재실행하면 TLB 히트가 발생하여 메모리를 참조할 수 있게 된다.   
* 물리 메모리에 해당 페이지가 없을 경우   
    * present bit가 0일 경우 해당 페이지가 물리 메모리에 존재하지 않음을 알 수 있다. (디스크 어딘가에 존재)    
    * 물리 메모리에 없는 페이지를 접근한 경우 ```page fault```가 발생한다.   

* page fault        
    * page fault가 발생하면 page fault를 처리하기 위해 운영체제로 제어권이 넘어가고, page fault handler가 실행된다.   

* supplemental page table   
    * 보조 페이지 테이블은 각 페이지에 대한 추가 데이터를 이용해서 페이지 테이블을 보조한다.   
    * 보조 페이지 테이블의 목적   
        * 페이지 폴트가 발생했을 때 페이지 폴트가 발생한 가상 페이지를 보조 페이지 테이블을 통해 탐색한다.  
        * 프로세스가 종료 될 때 커널이 어떤 자원을 free할지 고르기 위해 보조 페이지 테이블을 조사한다.   
        