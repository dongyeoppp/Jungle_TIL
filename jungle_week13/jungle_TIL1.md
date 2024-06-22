## 13주차 알고리즘 및 실력다지기 

- 2024 - 06 -14 (89일차)

#### 알고리즘 문제풀이  

* 1684번 [같은 나머지](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week12/bk_1684.py)  

* 9935번 [문자열 폭발](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week12/bk_9935.py)  

#### 스프링 입문  
* 빌드하고 실행하기  
    * cmd창에서 해당 파일로 이동 후 ```gradlew.bat build```   
    * ```cd build/libs```로 이동  
    * ```dir```로 hello-spring-0.0.1.snapshot.jar파일이 생성됨을 확인   
    * ```java -jar hello-spring-0.0.1.snapshot.jar``` 입력  
    * 실행 확인  

* Controller   
    ```
    package hello.hello_spring.controller;

    import org.springframework.stereotype.Controller;
    import org.springframework.ui.Model;
    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.RequestParam;

    @Controller
    public class HelloController {
        // 정적 컨텐츠 
        @GetMapping("hello")
        public String hello(Model model){
            model.addAttribute("data","hello!!");
            return "hello";
        }
        // mvc와 템플릿 엔진  
        @GetMapping("hello-mvc")    // "hello-mvc" url 경로 
        public String hellomvc(@RequestParam("name") String name, Model model){       // hellomvc는 메서드 이름, 이 메서드는 GET 요청을 처리
            model.addAttribute("name",name);        // model을 통해 변수 전달  
            return "hello-template";        // hello-template 파일과 매핑  
        }
        // @RequestParam("name") -> 쿼리파라미터 값을 받아 string 변수에 저장 -> http://localhost:8080/hello-mvc?name=John  --> name변수에 John 저장   

        // api
        @GetMapping("hello-string")
        @ResponseBody
        public String helloString(@RequestParam("name") String name){
            return "hello "+name;
        }

        // api/ 객체를 json으로 반환 
        @GetMapping("hello-api")
        @ResponseBody
        public Hello helloApi(@RequestParam("name") String name){
            Hello hello = new Hello();      // 클래스의 인스턴스 생성 
            hello.setName(name);            
            return hello;
        }

        static class Hello {
            private String name;        // name은 Hello 객체의 속성

            public String getName() {
                return name;
            }

            public void setName(String name) {
                this.name = name;
            }
        }
    }
    ```   
    