## 8주차 pintos 및 알고리즘 문제 풀이

- 2024 - 05 -15 (59일차)

#### 알고리즘 문제 풀이

- 1697번 [숨바꼭질](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week08/bk_1697.py)
- 20922번 [겹치는건 싫어](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week08/bk_20922.py)

#### pintos 구현 - priority sort

- keypoint
  - condition->waiter와 semaphore->waiter 정렬 적용하기
- chellenge
  - sema_up,cond_signal 에서 왜 정렬을 하고 unblock을 해주는가
    - thread_set_priority()를 호출했을 경우 waiter리스트의 우선순위가 오름차순으로 정렬되어 있지 않을 수 있다.
    - 그러므로 list_sort를 한 이후에 list_pop_front()로 우선순위가 가장 큰 값을 빼줘야한다.
  - new_cmp_priority에서 sema_waiter_a도 포인터인데 왜 주소값을 전달해주지않는가
    - head.next 값이 포인터이므로 주소값을 전달하지 않아야 한다.
      ```
      struct list_elem *new_list_a = sema_waiter_a->head.next;
      struct list_elem *new_list_b = sema_waiter_b->head.next;
      ```
    - waiter의 경우 포인터가 아니다.
      ```
      struct list *sema_waiter_a = &new_a->waiters;
      struct list *sema_waiter_b = &new_b->waiters;
      ```
- sema_up

  ```
  /* 세마포어를 해제하고 값을 1 증가시킨다.*/
  void sema_up(struct semaphore *sema)
  {
      enum intr_level old_level;

      ASSERT(sema != NULL);

      old_level = intr_disable();
      if (!list_empty(&sema->waiters)) // sema->waiter 리스트가 비어있지 않을 경우
      {
          list_sort(&sema->waiters, cmp_priority, NULL);
          thread_unblock(list_entry(list_pop_front(&sema->waiters),
                                  struct thread, elem));
      }
      sema->value++;
      thread_preemtive(); // wait_list에서 ready_list로 넣어준 thread의 우선순위가 현재 실행중인 thread의 우선순위 보다 높을 수 있으므로 context_switching이 일어나는지 확인한다.
      intr_set_level(old_level);
  }
  ```

- cond_signal

  ```
  void cond_signal(struct condition *cond, struct lock *lock UNUSED)
  {
      ASSERT(cond != NULL);
      ASSERT(lock != NULL);
      ASSERT(!intr_context());
      ASSERT(lock_held_by_current_thread(lock));

      if (!list_empty(&cond->waiters))
      {
          list_sort(&cond->waiters, new_cmp_priority, NULL);
          sema_up(&list_entry(list_pop_front(&cond->waiters),
                              struct semaphore_elem, elem)
                      ->semaphore);
      }
  }
  ```

- new_cmp_priority

  - condition 구조체 안에 있는 waiters 리스트의 list_elem이 주어지기 때문에 thread의 priority바로 알 수 없다.
  - list_entry 함수를 사용해서 해당 구조체를 포함하고 있는 구조체를 가르키면서 thread의 priority를 찾는다.

  ```
  bool new_cmp_priority(struct list_elem *a_, struct list_elem *b_,
  				  void *aux UNUSED)
  {
      struct semaphore_elem *a = list_entry(a_, struct semaphore_elem, elem);
      struct semaphore_elem *b = list_entry(b_, struct semaphore_elem, elem);
      struct semaphore *new_a = &a->semaphore;
      struct semaphore *new_b = &b->semaphore;

      struct list *sema_waiter_a = &new_a->waiters;
      struct list *sema_waiter_b = &new_b->waiters;
      struct list_elem *new_list_a = sema_waiter_a->head.next;
      struct list_elem *new_list_b = sema_waiter_b->head.next;

      struct thread *t_a = list_entry(new_list_a, struct thread, elem);
      struct thread *t_b = list_entry(new_list_b, struct thread, elem);

      return t_a->priority > t_b->priority;
  }
  ```
