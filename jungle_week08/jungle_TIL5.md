## 8주차 pintos 및 알고리즘 문제 풀이

* 2024 - 05 -18 (62일차)   

##### 알고리즘 문제 풀이   
* 15686번 [치킨 배달]()   

#### pintos 구현 - advenced scheduler (mlfqs)  
* [pintos 구현 project1]()   

* chellenge
    * nice, load_average, recent_cpu 값을 조정할 때 왜 인터럽트를 비활성화 하는가   
        * 해당 작업 중 interrupt가 발생하면 해당 작업이 안전하게 끝나지 않을 수 있기 때문에 값을 조정할 때 intterupt를 비활성화 해준다.  
    * list_remove(&victim->all_elem); : all_list의 all_elem값이 삭제 되는가   
        * all_list는 all_elem으로 연결되어 있다.   
        * 해당 thread의 all_elem을 삭제하면 all_elem으로 연결된 리스트, all_list의 all_elem이 삭제된다.   
    * int temp = TO_INTEGER_ROUND(load_average * 100); : 왜 정수형으로 바꿔주고 반환하는가    
        * temp 값은 출력되는 값으로 이진수로 출력되지 않도록 정수형으로 변환한다.  
        * 정수형으로 변환된 값이 test할때 비교값이 되므로 변환이 필요하다.   

* all_list   
    * 모든 thread를 담고 있는 리스트   
    * 모든 thread의 우선순위를 재계산 해줄 때 필요하다.
    * thread를 초기화(init_thread)해줄 때 all_list에 push하고 do_schedule 해줄 때 all_list에서 제거   
* nice   
    * 각 thread마다 가지고 있는 값으로 nice가 양수일 경우 priority가 낮아지고, nice가 음수일 경우 priority값이 올라간다.   
* load_average   
    * 시스템의 작업 부하를 나타내며 높은 load_average는 실행중이거나 실행 대기 중인 thread가 많다는 것을 의미한다.   
* recent_cpu  
    * 각 thread마다 가지고 있는 값으로, 해당 thread가 얼마나 cpu를 오래 점유하고 있었는지를 확인할 수 있다.  
    * recent_cpu값이 높으면 우선순위가 낮아지고, recent_cpu값이 낮아지면 우선순위가 높아진다.   
* 부동소수점 계산   
    * pintos 구현에서 부동소수점 자료형에 대한 계산을 지원하지 않기 때문에 정확한 계산을 위해 고정 소수점으로 변경하여 연산하여야 한다.   
    * 메크로 파일 (fixed_point.h)
        ```
        // pintos에서는 float 자료형을 지원하지 않는다. 만약 부동 소수점 연산을 사용해야 하는 경우,
        // 고정 소수점 연산을 사용해야한다.
        // 고정 소수점 연산을 위함 메크로를 모아 놓은 파일이다.  

        #define FIXED_POINT_MULTIPLIER (1 << 14) // f의 값에 따라 적절히 조정

        // n을 고정소수점으로 변환
        #define TO_FIXED_POINT(n) ((n) * FIXED_POINT_MULTIPLIER)

        // x를 정수로 변환 (0으로 반올림)
        #define TO_INTEGER_TRUNCATE(x) ((x) / FIXED_POINT_MULTIPLIER)

        // x를 정수로 변환 (가장 가까운 정수로 반올림)
        #define TO_INTEGER_ROUND(x) (((x) >= 0) ? (((x) + FIXED_POINT_MULTIPLIER / 2) / FIXED_POINT_MULTIPLIER) : (((x) - FIXED_POINT_MULTIPLIER / 2) / FIXED_POINT_MULTIPLIER))

        // x와 y를 더함
        #define ADD(x, y) ((x) + (y))

        // x에서 y를 뺌
        #define SUBTRACT(x, y) ((x) - (y))

        // x와 n을 더함
        #define ADD_INT(x, n) ((x) + TO_FIXED_POINT(n))

        // x에서 n을 뺌
        #define SUBTRACT_INT(x, n) ((x) - TO_FIXED_POINT(n))

        // x와 y를 곱함
        #define MULTIPLY(x, y) (((int64_t)(x)) * (y) / FIXED_POINT_MULTIPLIER)

        // x를 n으로 곱함
        #define MULTIPLY_INT(x, n) ((x) * (n))

        // x를 y로 나눔
        #define DIVIDE(x, y) (((int64_t)(x)) * FIXED_POINT_MULTIPLIER / (y))

        // x를 n으로 나눔
        #define DIVIDE_INT(x, n) ((x) / (n))
        ```   
        
* 함수 추가 및 수정   
    * thread의 nice 값 setting   
        ```
        void thread_set_nice(int nice UNUSED)
        {
            enum intr_level old_level;
            old_level = intr_disable(); // interrupt 비활성화
            struct thread *t = thread_current();
            t->nice = nice;		   // 현재 thread의 nice 값 갱신
            calculate_priority(t); // 우선순위 재 계산
            // 우선순위 비교 후 context switching
            struct thread *readey_list_first = list_entry(list_begin(&ready_list), struct thread, elem);
            if (readey_list_first != NULL)
            {
                if (t->priority < readey_list_first->priority)
                {
                    thread_yield();
                }
            }
            intr_set_level(old_level); // interrupt 활성화
        }
        ```    
    * 현재 thread의 nice 값 return   
        ```
        int thread_get_nice(void)
        {
            enum intr_level old_level;
            old_level = intr_disable(); // interrupt 활성화
            int temp = thread_current()->nice;
            intr_set_level(old_level); // interrupt 비 활성화
            return temp;	// 현재 thread의 nice 값 반환 
        }
        ```    
    * load_average에 100을 곱한 값을 리턴   
        ```
        int thread_get_load_avg(void)
        {
            enum intr_level old_level;
            old_level = intr_disable();

            int temp = TO_INTEGER_ROUND(load_average * 100);		// 출력되는 값이므로 정수형으로 바꿔준 후 출력한다.

            intr_set_level(old_level);

            return temp;
        }
        ```   
    * recent_cpu에 100을 곱한 값을 리턴    
        ```
        int thread_get_recent_cpu(void)
        {
            enum intr_level old_level;
            old_level = intr_disable();

            int temp = TO_INTEGER_ROUND(thread_current()->recent_cpu * 100);	// 출력되는 값이므로 정수형으로 바꿔준 후 출력한다.

            intr_set_level(old_level);
            return temp;
        }
        ```   
    * nice와 cpu_recent를 사용하여 우선순위를 계산   
        ```
        void calculate_priority(struct thread *t)
        {
            if (t != idle_thread) // 현재 thread가 ide_thread가 아닐 경우
            {
                t->priority = PRI_MAX - TO_INTEGER_ROUND((t->recent_cpu / 4)) - (t->nice * 2);
            }
        }
        ```   
    * recent_cpu를 계산   
        ```
        void calculate_recent_cpu(struct thread *t)
        {
            if (t != idle_thread)
            {
                // int new_load_average = calculate_load_average();
                // int decay = (2* load_average) / (2* load_average + 1);
                int decay = DIVIDE((2 * load_average), (ADD_INT(2 * load_average, 1)));
                // t->recent_cpu = decay * t->recent_cpu + t->nice;
                t->recent_cpu = ADD_INT(MULTIPLY(decay, t->recent_cpu), t->nice);
            }
        }
        ```    
    * load_avg를 계산  
        ```
        int calculate_load_average()
        {
            int ready_threads;
            if (thread_current() == idle_thread) // 현재 실행준인 thread가 idle_thread일 경우
            {
                ready_threads = list_size(&ready_list); // ready_threads는 ready_list에 들어있는 모든 thread의 개수
            }
            else
            {
                ready_threads = list_size(&ready_list) + 1; // ready_threads는 ready_list에 들어있는 모든 thread의 개수 + 실행중인 thread
            }
            // load_average = (59 / 60) * load_average + (1 / 60) * ready_threads;
            load_average = ADD(MULTIPLY(DIVIDE(TO_FIXED_POINT(59), TO_FIXED_POINT(60)), load_average), MULTIPLY_INT(DIVIDE(TO_FIXED_POINT(1), TO_FIXED_POINT(60)), ready_threads));
            return load_average;
        }
        ```   
    * recent_cpu를 1씩 증가시키는 함수   
        ```
        void up_recent_cpu(struct thread *t)
        {
            if (t != idle_thread)
            {
                return t->recent_cpu = ADD_INT(t->recent_cpu, 1);
            }
        }
        ```     
    * 모든 thread의 우선순위와 recent_cpu 다시 계산    
        ```
        void recalculate_all()
        {
            // all_list라는 새로운 리스트를 만듬, all_list에는 존재하는 모든 thread가 들어가 있다.
            struct list_elem *all_list_first = list_begin(&all_list);
            calculate_load_average(); // load_average를 갱신해 준 이후 pirority와 recent_cpu값을 갱신해준다.
            while (all_list_first != list_end(&all_list))
            {
                struct thread *first_thread = list_entry(all_list_first, struct thread, all_elem);
                calculate_priority(first_thread);	// 수식에 의한 priority값 갱신
                calculate_recent_cpu(first_thread); // recent_cpu 값 갱신
                all_list_first = all_list_first->next;
            }
        }
        ```    
    * 모든 thread의 우선순위를 계산   
        ```
        void recalculate_priority()
        {
            struct list_elem *all_list_first = list_begin(&all_list);
            while (all_list_first != list_end(&all_list))
            {
                struct thread *first_thread = list_entry(all_list_first, struct thread, all_elem); // all_list의 elem 이므로 all_elem을 사용해야한다.
                calculate_priority(first_thread);
                all_list_first = all_list_first->next;
            }
        }
        ```    
    * timer_intterrupt   
        ```
        static void
        timer_interrupt(struct intr_frame *args UNUSED)
        {
            ticks++;
            thread_tick();

            // mlfq
            // wake_up은 mlfq이후에 실행
            if (thread_mlfqs)
            {
                struct thread *t = thread_current();
                up_recent_cpu(t);					 // recent_cput +1
                if (timer_ticks() % TIMER_FREQ == 0) // 1초(100tick)마다 load_avg 갱신한 이후 모든 thread의 recent_cpu, priority 재계산
                {
                    recalculate_all();
                }
                else if (timer_ticks() % 4 == 0) // 4tick 마다 priority 재계산
                {
                    recalculate_priority();
                }
            }
            //
            /* add code - gdy*/
            while (ticks >= get_global_tick()) // local_tick이 같은 경우도 처리해줘야하므로 반복문을 실행한다.
            {
                wake_up(ticks);
            }
            /* add code - gdy*/
        }
        ```   

    


 

