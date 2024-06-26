## 14주차 알고리즘 및 기획 + spring 부트, jpa

- 2024 - 06 -21 (96일차)

#### 알고리즘 문제 풀이   

* 1911번 [흙길 보수하기](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week14/bk_1911.py)

#### spring + jpa   
*  ``` git pull origin main --allow-unrelated-histories ```  : git pull origin main 을 받을 때 read.me가 있으면 에러가 난다. 해당 명령어를 사용하여 해결할 수 있다.  

* spring + jpa  
    * test할때 ```@Transactional``` 애노테이션을 통해 test이후 rollback (db데이터도 원상태로)   
        * ```@Rollback(false)``` 애노테이션을 추가할 경우 db에 데이터를 남겨 잘 들어갔는지 확인 가능   

* 엔티티 설계시 주의 사항  
    * 엔티티에는 가급전 setter를 사용하지 말자  
    * 모든 연관관계는 지연로딩으로 설정  
        * ```OneToMany```는 디폴트가 lazy인데 ```ManyToOne```은 디폴트가 lazy가 아니므로 다시 설정해줘야 함   

    
        