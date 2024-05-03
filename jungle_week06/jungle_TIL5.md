## 6주차 malloc-lab 구현 및 알고리즘 문제 풀이

- 2024 - 04 -29 (43일차)

#### malloc-lab 구현

- [malloc - lab](https://github.com/dongyeoppp/malloc-lab/blob/main/mm.c)

- 기본 상수 및 매크로

  ```
  /* 기본 상수 및 매크로 */
  /* 기본 size 상수를 정의*/
  #define WSIZE 4                           // 워드 크기 (bytes)
  #define DSIZE 8                           // 더블 워드 (bytes)
  #define CHUNKSIZE (1 << 12)               // 초기 가용 블록과 힙 확장을 위한 기본 크기(1 << 12 는 2의 12승 = 4096-> 약 4kb-> 힙을 늘릴 때 약  4kb 분량을 늘린다. )(bytes)
                                          // 1을 이진수로 표기하면 0000 0000 0000 0001 -> 1 << 12(시프트 연산) -> 0001 0000 0000 0000 -> 2^12
  #define MAX(x, y) ((x) > (y) ? (x) : (y)) // 삼항 연산자를 활용해 ? 앞에 있는 조건인 x가 더 크다는 조건이 참이면 왼쪽 표현식 반환(x를 반환), 조건이 참이 아니라면 그 다음 표현식 반환(y 반환)

  /*하나의 word에 size(메모리 블록의 크기)와 allocated bit (해당 메모리 블록이 할당되었는지 여부를 확인)를 패킹한다. */
  #define PACK(size, alloc) ((size) | (alloc)) // 크기와 할당 비트를 통합해서 헤더와 풋터에 저장할 수 있는 값을 리턴한다.

  /*메모리 주소 'p'가 가리키는 위치에서 메모리를 읽거나 쓰기*/
  #define GET(p) (*(unsigned int *)(p))              // 인자 p가 참조하는 워드를 읽어서 리턴한다. // (unsigned int *)은 주소 'p'를 정수 포인터로 캐스팅하는 것을 의미한다. // unsigned int 자료형은 부호없는 정수를 나타내며 음수값을 허용하지 않는다.
                                                  // 음수를 쓰지 않을 것이므로 같은 공간에 더 많은 양수를 표현할 수 있는 unsigned int를 사용하자
                                                  // 캐스팅이란 변수나 값을 하나의 자료형에서 다른 자료형으로 변환하는 것을 의미한다.  // 인자 p는 대개 (void *) 포인터이며, 이것은 직접적으로 역참조할 수 없다. // 자료형을 변환하여 메모리에 있는 값을 읽거나 쓸 수 있도록 한다.
  #define PUT(p, val) (*(unsigned int *)(p) = (val)) // 인자 p가 가리키는 워드에 val을 저장한다.

  /* 주소 'p'에서 사이즈와 할당 여부를 읽는 것은 해당 주소에서 워드를 읽고, 그 값을 해석한다.*/
  // 각각 주소 p에 있는 헤더 또는 풋터의 size와 할당 비트를 리턴한다.
  #define GET_SIZE(p) (GET(p) & ~0x7) // size만 가져오기
  #define GET_ALLOC(p) (GET(p) & 0x1) // 가용여부만 가져오기

  /* 주어진 블록 포인터 'bp'로부터 해당 블록의 헤더와 풋터의 주소를 계산한다.*/
  // bp는 header와 payload 사이의 경계를 가르키고 있다.
  #define HDRP(bp) ((char *)(bp) - WSIZE)                      // 블록 헤더를 가리키는 포인터를 리턴한다.     // bp를 한 블록 뒤로 옮기면 bp가 header 블록 앞 경계를 가르키게 된다.
  #define FTRP(bp) ((char *)(bp) + GET_SIZE(HDRP(bp)) - DSIZE) // 블록 풋터를 가리키는 포인터를 리턴한다.     // 다음 블록의 header로 bp 이동 (size만큼 뒤로) 이후 더블 워드 만큼 뒤로 가면 footer 블록 앞에 경계로 bp 이동

  /* 주어진 블록 포인터 'bp'로부터 다음 블록과 이전 블록의 주소를 계산한다.*/
  #define NEXT_BLKP(bp) ((char *)(bp) + GET_SIZE(((char *)(bp) - WSIZE))) // 다음 블록의 포인터 주소를 리턴한다.
  #define PREV_BLKP(bp) ((char *)(bp) - GET_SIZE(((char *)(bp) - DSIZE))) // 이전 블록의 포인터 주소를 리턴한다.
  ```

- 할당된 블록 해제하기

  ```
  /*할당된 블록 해제하기*/
  void mm_free(void *bp)
  {
      size_t size = GET_SIZE(HDRP(bp)); // header에 담겨 있는 크기 정보 = size

      PUT(HDRP(bp), PACK(size, 0)); // block header를 업데이트 -> 할당 비트를 0으로
      PUT(FTRP(bp), PACK(size, 0)); // block footer를 업데이트 -> 할당 비트를 0으로
      coalesce(bp);
  }
  ```

- 인접한 블록들과 병합하기

  ```
  /* 인접한 블록들과 병합하기 */
  static void *coalesce(void *bp)
  {
      size_t prev_alloc = GET_ALLOC(FTRP(PREV_BLKP(bp))); // 이전 블록의 footer 정보를 읽어와서 할당여부 저장
      size_t next_alloc = GET_ALLOC(HDRP(NEXT_BLKP(bp))); // 다음 블록의 header 정보를 읽어와서 할당여부 저장
      size_t size = GET_SIZE(HDRP(bp));                   // 현재 블록의 header 정보를 읽어와서 size 저장

      if (prev_alloc && next_alloc) // 둘 다 사용중일 경우 (case1)
      {
          return bp; // 현재 블록의 포인터 return
      }
      else if (prev_alloc && !next_alloc) // 다음 블록만 가용블록 (case2)
      {
          size += GET_SIZE(HDRP(NEXT_BLKP(bp))); // 다음 블록의 header정보를 읽어와서 size값 만큼 +
          PUT(HDRP(bp), PACK(size, 0));          // size값 갱신
          PUT(FTRP(bp), PACK(size, 0));          // header 값 갱신 후 footer size 갱신
      }
      else if (!prev_alloc && next_alloc) // 이전 블록만 가용블록 (case3)
      {
          size += GET_SIZE(HDRP(PREV_BLKP(bp)));   // 이전 블록의 header에서 size값 만큼 +
          PUT(FTRP(bp), PACK(size, 0));            // 현재 블록의 footer에 size값 갱신
          PUT(HDRP(PREV_BLKP(bp)), PACK(size, 0)); // 이전 블록의 header에 size값 갱신
          bp = PREV_BLKP(bp);                      // bp를 이전 블록의 포인터로 변경
      }
      else
      {                                                                          //  이전블록과 다음 볼록이 모두 가용상태일 경우 (case 4)
          size += GET_SIZE(HDRP(PREV_BLKP(bp))) + GET_SIZE(FTRP(NEXT_BLKP(bp))); // size = 이전블록의 header-> size + 다음 블록의 footer -> size
          PUT(HDRP(PREV_BLKP(bp)), PACK(size, 0));                               // 이전 블록의 header에 size값 갱신
          PUT(FTRP(NEXT_BLKP(bp)), PACK(size, 0));                               // 다음 블록의 footer에 size값 갱신
          bp = PREV_BLKP(bp);                                                    // bp를 이전 블록의 포인터로 변경
      }
      return bp; // 현재 블록의 포인터 return
  }
  ```

- 새 가용블록으로 힙 확장하기

  ```
  /* 새 가용블록으로 힙 확장하기 */
  static void *extend_heap(size_t words)
  {
      char *bp;
      size_t size;
      /*만약 words가 홀수라면 한 블록을 추가하여 짝수 개의 words를 할당할 수 있도록 한다.*/
      size = (words % 2) ? (words + 1) * WSIZE : words * WSIZE; // 주어진 words의 크기를 기준으로 size(새로운 블록의 크기)를 결정한다. // 워드 단위의 정렬을 보장하기 위함
      if ((long)(bp = mem_sbrk(size)) == -1)                    // bp는 mem_sbrk 함수에서 반환한 old_brk를 가지고 있다.
          return NULL;

      PUT(HDRP(bp), PACK(size, 0));         // free block header    // 원래있던 epilogue 블록에 덮어씌여져 새로운 블록의 header가 된다.
      PUT(FTRP(bp), PACK(size, 0));         // free block footer
      PUT(HDRP(NEXT_BLKP(bp)), PACK(0, 1)); // new epilogue header      // 가장 마지막 블록은 새로운 epilogue가 된다.

      return coalesce(bp);
  }
  ```

- 할당기 초기화하기

  ```
  // 할당기(힙) 초기화하기(성공이면 0 아니면 -1을 리턴한다.)
  int mm_init(void)
  {
      void *heap_listp;
      if ((heap_listp = mem_sbrk(4 * WSIZE)) == (void *)-1) // mem_sbrk 함수는 memlib.c에서 불러와 사용하고 있다. incur 값이 음수 이거나 mex_heap 범위를 초과하면 -1 return
          return -1;
      PUT(heap_listp, 0);                            // 정렬 요건을 맞추기 위한 1워드(value = 0)(alignment padding)
      PUT(heap_listp + (1 * WSIZE), PACK(DSIZE, 1)); // 다음 블록에 크기(DSIZE=8)와 할당 비트(1)를 통합한 값을 넣는다.(prologue header)
      PUT(heap_listp + (2 * WSIZE), PACK(DSIZE, 1)); // 다음 블록도 동일(prologue footer)
      PUT(heap_listp + (3 * WSIZE), PACK(0, 1));     // 다음 블록은 epilogue header를 나타내며 크기는 0이고 할당비트는 1이다.
      heap_listp += (2 * WSIZE);                     // 포인터를 prologue header와 prologue footer 사이에 위치 시킨다.

      if (extend_heap(CHUNKSIZE / WSIZE) == NULL)
          return -1;
      return 0;
  }
  ```

#### 알고리즘 문제 풀이

- 2230번 [수 고르기](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week06/bk_2230.py)
