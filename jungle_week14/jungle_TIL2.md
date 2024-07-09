## 14주차 알고리즘 및 기획 + spring 부트, jpa

- 2024 - 06 -22 (97일차)

#### 알고리즘 문제 풀이

- 1303번 [전쟁 - 전투](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week14/bk_1303.py)
- 1963번 [소수 경로](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week14/bk_1963.py)
- 1057번 [토너먼트](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week14/bk_1057.py)
- 1389번 [케빈 베이컨의 6단계 법칙](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week14/bk_1389.py)

#### spring

- EntityManager
  - JPA의 핵심 인터페이스로 엔티티 객체와 데이터베이스 간의 상호작용을 관리하는데 사용된다.

* 변경 감지(dirty checking)와 병합

  - 준영속 엔티티
    - 영속성 컨텍스트가 더는 관리하지 않는 엔티티
    - 임의로 만들어낸 엔티티도 기존 식별자를 가지고 있으면 준영속 엔티티라고 할 수 있다.
    - 엔티티를 변경할 때는 항상 변경 감지를 사용하는 것이 좋다. (merge보단 변경감지를 사용하는게 좋다.)

* API

  - @Controller + @ResponseBody -> @RestController

* DTO를 RequestBody에 매핑

  - 요청 값으로 Member 엔티티 대신에 별도의 DTO를 받는다.
  - 엔티티와 API 스펙을 명확하게 분리할 수 있다.
  - 엔티티가 변해도 API 스펙이 변하지 않는다.
  - 실무에서는 엔티티를 API 스펙에 노출하면 안된다.

* Rest Api
  - GET : 조회
  - POST : 등록
  - PUT : 수정
    - PUT 요청 시 요청을 일부분만 보낸 경우 나머지는 default 값으로 수정됨
    - PATCH는 새롭게 바뀐 부분만 반영
    - 자원의 일부를 수정할 때는 PATCH를, 전체적인 수정이 필요한 경우는 PUT을 이용하는 것이 적절하다.
  - DELETE : 삭제

* ```@JsonIgnore```
  * 해당 애노테이션을 적용하면 해당 정보를 json에서 제외시킬 수 있음     


