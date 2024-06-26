## 13주차 알고리즘 및 실력다지기

- 2024 - 06 -17 (92일차)

* 13335번 [트럭](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week12/bk_13335.py)

#### 스프링 db 접근 기술

- JDBC

  - Java Database Connectivity
  - 자바에서 데이터베이스를 연결하고 쿼리를 실행하기 위한 표준 api
  - 스프링 jdbc template과 같은 라이브러리는 jdbc api의 반복 코드를 대부분 제거해준다. 하지만 sql은 직접 작성해야 한다.

- JPA

  - Java Persistence API
  - JPA는 기존의 반복코든느 물론이고, 기본적인 SQL도 JPA가 직접 만들어서 실행해준다.
  - JPA를 사용하면 SQL과 데이터 중심의 설계에서 객체 중심의 설계로 패러다임을 전환할 수 있다.
  - JPA를 사용하면 개발 생산성을 크게 높일 수 있다.

- 스프링 데이터 JPA

  - 스프링 데이터 JPA는 JPA를 편리하게 사용하도록 도와주는 기술이다.
  - 스프링 부트와 JPA만 사용해도 개발 생산성이 정말 많이 증가한다. 여기에 스프링 데이터 JPA를 사용하면 기존의 한계를 넘어 리포지토리에 구현 클래스 없이 인터페이스 만으로 개발을 완료할 수 있다.
  - 실무에서 관계형 데이터베이스를 사용한다면 스프링 데이터 JPA는 선택이 아닌 필수가 된다.

- AOP

  - Aspect Oriented Programming
  - 반복되는 코드를 여러 군데에 찍어봐야 할때 필요할 수 있다.
  - 공통 관심 사항과 핵심 관심 사항을 분리하여 원하는 곳에만 공통 관심 사항을 적용한다.

- Spring Boot

  - 웹 프로그램을 쉽고 빠르게 만들수 있도록 도와주는 자바의 웹 프레임워크이다.
    - spring은 전반전인 프레임워크를 의미하고, spring boot는 spring을 사용하여 빠르고 간편하게 애플리케이션을 개발할 수 있도록 도와주는 도구이다.
  - 스프링부트는 스프링 프레임워크에 `톰캣(Tomcat)`이라는 서버를 내장하고 여러 편의 기능들이 추가되어 있다.
    - `톰캣(Tomcat)`은 클라이언트의 요청을 해석하여 그에 맞는 자바 프로그램을 실행한 후 그 결과를 응답해주는 웹 애플리케이션 서버이다.

- WAS란

  - WAS는 웹 애플리케이션과 서버 환경을 연결하는 중간 역할을 하는 소프트웨어 플랫폼이다.
    - 사용자가 웹 브라우저로 서버에 요청을 보내면 WAS는 사용자의 요청을 해석하여 그에 맞는 서버 프로그램을 구동한 후 그 결과를 사용자에게 보여준다.
    - 스프링 부트는 내장된 웹 서버인 Tomcat을 제공하기 때문에 애플리케이션을 별도의 was없이도 실행할 수 있다.

- ORM
  - SQL을 사용하지 않고 데이터베이스를 관리할 수 있는 도구이다.
  - ORM은 데이터베이스의 테이블을 자바 클래스로 만들어 관리할 수 있다.
