## 8주차 pintos 및 알고리즘 문제 풀이, quiz 리뷰

- 2024 - 05 -14 (58일차)

#### 8주차 퀴즈 리뷰

- 응용 프로그램을 구현할 때 multiprocess와 multithread 중 하나를 선택하는 기준

  - 안정성 vs 자원사용 : 시스템의 안정성이 매우 중요한 경우, `멀티 프로세스`가 선호된다. 리소스가 제한적인 환경에서는 `멀티 스레드`가 더 효율적일 수 있다.
  - 구현의 복잡성 : 스레드는 공유 메모리로 인해 동기화 문제가 복잡해질 수 있으므로, 개발자의 동시성 제어에 대한 이해가 중요
  - 응답 시간 : 멀티스레드는 컨텍스트 스위칭이 빠르기 때문에, 더 빠른 응답 시간을 요구하는 경우 유리할 수 있다.
  - 플랫폼 및 언어 지원 : 사용 중인 프로그래밍 언어나 플랫폼이 멀티 스레드 또는 멀티 프로세스 중 어느 쪽을 더 잘 지원하는지도 중요한 요소가 됨

- 데드락 해결 전략

  - 데드락 예방
    - 데드락이 발생하는 필수조건 (상호배제, 점유와 대기, 비선점, 순환 대기)중 적어도 하나를 제거함으로써 데드락 방지
  - 데드락 회피
    - 프로세스에 리소스를 할당하기 전에 안전 상태를 체크한다. 만약 할당으로 인해 데드락이 발생할 위험이 있다면, 할당하지 않는다.
  - 데드락 탐지 및 회복
    - 주기적으로 리소스 할당 그래프를 검사하여 순환 대기 조건을 찾는다. 데드락이 탐지 될 경우, 시스템은 프로세스를 중지하거나 리소스 할당을 롤백하여 데드락을 해결한다.
  - 자원의 상호 배제 제거
    - 리소스가 복사 가능하거나 공유가 가능한 경우, 여러 프로세스가 동시에 해당 리소스를 사용할 수 있다. 이러한 방식으로 상호배제 조건을 제거하여 데드락 발생 가능성을 줄일 수 있다.

- mutex와 semaphore

  - mutex
    - 공유 자원에 대한 접근을 단일 스레드에게만 허용한다.
    - 잠금을 건 스레드만이 잠금을 해제할 수 있다.
  - semaphore

    - 공유 자원에 대한 접근을 제한하는데 사용되며, 특정 숫자로 초기화 된다. 이 특정 숫자는 동시에 해당 자원에 접근할 수 있는 스레드의 최대 수를 나타낸다.
    - semaphore는 스레드가 자원을 사용할 때마다 감소하고, 자원을 해제할 때마다 증가한다.

  - mutex와 semaphore 비교
    - 모두 동시성을 관리하고, 데이터 무결성을 보장하는데 필수적이다.
    - 더 엄격한 제어가 필요할 경우 mutex를 사용하고, 동시 접근을 허용할 때 semaphore를 사용한다.

#### pintos - alarm

- 목표
  - sleep_list를 활용하여 busy waiting을 없애기
- add function

  - thread를 sleep_list에 삽입하는 함수
    ```
    void thread_sleep(int64_t ticks)
    {
        struct thread *curr = thread_current(); // 현재 실행중인 쓰레드
        enum intr_level old_level;
        old_level = intr_disable(); // 인터럽트를 비활성화 하고 old_level에 이전 인터럽트 상태 저장
        if (curr != idle_thread)	// curr 쓰레드가 idle 쓰레드가 아닐 경우
        {
            curr->local_tick = ticks;										// 먼저 tick값을 해당 쓰레드의 local_tick값에 저장
            list_insert_ordered(&sleep_list, &curr->elem, find_less, NULL); // 오름차순으로 정렬하면서 sleep_list에 해당 쓰레드를 삽입한다.
            struct thread *new_first = list_entry(list_begin(&sleep_list),
                                                struct thread, elem); // sleep_list에 존재하는 쓰레드 중 첫번째 쓰레드의 local_tick값을 global_tick에 저장
            global_tick = new_first->local_tick;						// sleep_list는 오름차순으로 정렬되어 있으므로, global_tick 값에 저장되는 값은 sleep_list의 local_tick값 중 최소값이 된다.
            thread_block();												// curr 스레드의 상태를 block 해주고 schedule()을 실행한다.
        }
        intr_set_level(old_level); // 인터럽트 활성화
    }
    ```
  - 리스트에서 값 크기 비교하기

    ```
    static bool
    find_less(const struct list_elem *a_, const struct list_elem *b_,
            void *aux UNUSED) // list_insert_ordered 함수에 사용한다.
    {
        const struct thread *a = list_entry(a_, struct thread, elem);
        const struct thread *b = list_entry(b_, struct thread, elem);

        return a->local_tick < b->local_tick; // sleep_list를 돌며 현재 local_tick 값보다 큰 값이 있으면 반복문을 종료하고 그 자리에 현재 쓰레드를 삽입한다.
    }
    ```

  - sleep_list에 있던 thread 깨우기(ready_list로 넣기)
    ```
    void wake_up(int64_t ticks)
    {
        struct thread *new_wake_thread = list_entry(list_pop_front(&sleep_list), struct thread, elem); // new_wak_thread는 ready_list에 넣을 쓰레드(리스트의 가장 앞에 있다.)
        thread_unblock(new_wake_thread);															   // 인터럽트를 비활성화 해준 이후 ready_list에 쓰레드를 넣고, 해당 쓰레드의 상태도 변경해준다. 이후 인터럽트를 다시 활성화한다.
        struct thread *new_first = list_entry(list_begin(&sleep_list), struct thread, elem);		   // sleep_list가 갱신 되었으므로 global_tick을 초기화한다.
        global_tick = new_first->local_tick;														   // new_first의 local_tick값이 최솟값으로 설정한다.
                                                                                                    // schedule()함수는 실행시키지 않아도 된다.
    }
    ```
  - global_tick 값을 넘겨주기 위한 함수
    ```
    int64_t get_global_tick(void)
    {
        return global_tick;
    }
    ```

- modify function

  - timmer_sleep

    ```
    void
    timer_sleep (int64_t ticks) {
        int64_t start = timer_ticks ();

        ASSERT (intr_get_level () == INTR_ON);
        /* add code - gdy*/
        // busy waiting  수정
        // while (timer_elapsed (start) < ticks)
        // 	thread_yield ();
        //start 값이 유효하지 않을 수 있음을 유의한다.
        if (timer_elapsed (start) < ticks){
            thread_sleep(start + ticks);
        }
        /* add code - gdy*/
    }
    ```

  - timmer_interrupt (handler)
    ```
    static void
    timer_interrupt (struct intr_frame *args UNUSED) {
        ticks++;
        thread_tick ();
        /* add code - gdy*/
        while ( ticks >= get_global_tick())
            wake_up(ticks);
        /* add code - gdy*/
    }
    ```

- chellenge
  - 정렬된 sleep_list에 global_tick이 필요한가
    - sleep_list에 들어있는 thread 중 local_tick 값이 가장 작은 thread는 리스트에 첫번째 요소가 되므로 globla_tick과 같은 값을 찾으려고 반복문에 넣을 필요는 없다.
    - global_tick이 없다면, sleep_list에서 thread를 깨울때마다 sleep_list -> thread -> local_tick값에 접근해야하므로 연산이 더 많아질 수 있다고 생각함
  - thread를 sleep_list에서 넣고 뺄 때 왜 interrupt를 비활성화해주고 다시 활성화 해주는가
    - interrupt를 비활성화하는 주요 이유는 커널 thread를 외부 인터럽트 핸들러와 동기화하기 위함이다. 외부 인터럽트 핸들러는 sleep할 수 없으므로 대부분의 다른 동기화 형태를 사용할 수 없다.
    - thread와 interrupt handler간의 `race condition`을 방지하기 위해서 interrupt disable을 사용하여 동기화한다.
    - interrupt를 비활성화하지 않으면 thread를 작업하는 동안에도 interrupt가 매틱마다 발생하여 진행하는 작업이 완전히 실행되지 않을 수 있을 것 같다.
  - local_tick값이 서로 같은 thread들이 sleep_list에 들어갈 경우
    - 기존 코드
      ```
      static void
      timer_interrupt (struct intr_frame *args UNUSED) {
         ticks++;
         thread_tick ();
         /* add code - gdy*/
         if ( ticks >= get_global_tick())
             wake_up(ticks);
         /* add code - gdy*/
      }
      ```
    - 수정 코드
      ```
      static void
      timer_interrupt (struct intr_frame *args UNUSED) {
          ticks++;
          thread_tick ();
          /* add code - gdy*/
          while( ticks >= get_global_tick())		// local_tick이 같은 경우도 처리해줘야하므로 반복문을 실행한다.
          {
              wake_up(ticks);
          }
          /* add code - gdy*/
      }
      ```
