## 나만무 기간 정리

#### 알고리즘 풀이
* 1449번 [수리공 항승](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week14/bk_1449.py)  
* 1431번 [시리얼 번호](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week14/bk_1431.py)   
* 11652번 [카드](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week14/bk_11652.py)   
* 30804번 [과일 탕후루](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week14/bk_30804.py)    

#### 나만무
* 테스트 코드 적용   
    * 통합 테스트   
        * 여러 기능을 조합하여 전체 비지니스 로직이 제대로 동작하는지 확인하는 것을 의미한다.  
        * ```@SpringBootTest``` : ```@SpringBootApplication```을 찾아가서 모든 Bean을 로드하게 된다.  
        * 대규모 프로젝트에 이 방법을 사용할 경우, 테스트를 실행할 때마다 모든 빈을 스캔하고 로드하는 작업이 반복되어 매번 무거운 작업을 수행해야 한다.   
    * 단위 테스트   
        * 단위 테스트는 프로젝트에 필요한 모든 기능에 대한 테스트를 각각 진행하는 것을 의미한다.   
        * 일반적으로 스프링 부트에서는 ```org.springframework.boot:spring-boot-starter-test``` 디펜던시만으로 의존성을 모두 가질 수 있다.   
        