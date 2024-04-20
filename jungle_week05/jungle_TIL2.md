## 5주차 Red-Black Tree 및 알고리즘 문제 풀이  

* 2024 - 04 -20 (34일차)     

#### RB - Tree 구현   
* calloc() : 메모리를 동적으로 할당하며, 할당된 메모리를 모두 0 으로 초기화 한다.   
    * 두개의 인자를 받으며 첫번째 인자는 할당하고자 하는 객체의 개수, 두 번째 인자는 각 객체의 크기를 나타낸다.   
    * ```calloc(1,sizeof(rbtree))``` : 할당하고자 하는 객체의 개수는 1개이고, 각 객체의 크기는 sizeof(rbtree)이다.    

* enum   
    * 어떤 유사한 성질을 갖는 변수를 정수로 표현할때 유용하다.   
    * ```enum { RBTREE_RED, RBTREE_BLACK }``` :  첫번째 요소는 0, 두번째 요소는 1로 사용 가능   

#### RB TREE 구현 코드    

* [RB TREE 구현하기](https://github.com/dongyeoppp/rbtree-lab/blob/main/src/rbtree.c)   

* RB TREE 구조체 생성   
    ```
    rbtree *new_rbtree(void) {    // rb tree 구조체 생성   
    rbtree *p = (rbtree *)calloc(1, sizeof(rbtree));
    // nil_node 생성, calloc을 사용하여 모든 node값에 null(=0)로 초기화 해줄 수 있다. 포인터 변수는 0으로 초기화하면 null 포인터를 나타낸다.      
    node_t *nil_node = (node_t *)calloc(1, sizeof(rbtree));   // 1 -> 할당하고자 하는 객체의 개수 , sizeof(rbtree)-> 각 객체의 크기
    // nil_node는 모두 black  
    nil_node->color = 1;    // 1 -> rbtree_black을 뜻함, nil-node는 모두 black   

    p->nil = nil_node;  // nilnode 붙여주기   
    p->root = nil_node;   // tree가 비어있을 경우 root는 nil   

    return p;
    }
    ```   

* RB TREE 삽입 (KEY 추가하기)    
    ```
    node_t *rbtree_insert(rbtree *t, const key_t key) {   // key 추가 (rb tree 삽입) 
    node_t *new_node = (node_t *)calloc(1, sizeof(rbtree)); 
    node_t *pre_node = t->nil;       // 새로 삽일 할 노드가 들어갈 위치에 부모노드를 저장
    node_t *cur_node = t->root;     // 새로 삽입할 key값을 넣을 노드의 위치 저장
    new_node->key = key;    // 삽입할 노드에 키 값 설정  
    while (cur_node != t->nil){
        pre_node = cur_node;      // 현재노드를 pre노드에 저장  
        if(key < cur_node->key){    // 삽입할 key값이 현재 노드보다 작을 경우 현재 노드에서 left로 
        cur_node = cur_node->left;
        }
        else{
        cur_node = cur_node->right;   // 삽일할 key값이 현재 노드보다 클 경우 현재 노드에서 right로
        }
    }
    new_node->parent = pre_node;   // 새로운 노드의 부모노드 저장   
    // 현재 노드의 부모노드로 이전 노드 연결  
    if (pre_node == t->nil){    // 트리에 노드가 없을 경우 , 삽입할 노드가 root 노드가 된다.  
        t->root = new_node;
    }
    else if( key < pre_node->key){   // 이전 노드의 key값이 현재 노드보다 클 경우  
        pre_node->left = new_node;      // 현재 노드를 이전 노드의 왼쪽에 위치하게 한다.
    }
    else{
        pre_node->right = new_node;   // 현재 노드를 이전 노드의 오른쪽에 위치하게 한다.  
    }
    // 이전 노드의 자녀노드로 현재노드를 연결
    new_node->left = t->nil;    // 올바른 트리 구조를 유지하기 위해 삽입된 노드의 위치는 leaf-node에 위치하며, 자녀노드로 nil_node를 가진다.
    new_node->right = t->nil;
    new_node->color = 0;    // 삽인된 노드의 컬러는 red
    rbtree_insert_fixup(t,new_node);  
    return new_node;
    }
    ```    
* RB TREE 삽입 이후 속성을 맞족시키기 위한 재조정    
    ```
    void rbtree_insert_fixup(rbtree *t, node_t *cur_node){    // 삽입 이후 rb tree 속성을 만족시키기 위한 재조정
    node_t *uncle;    // cur_node의 부모의 형제 노드를 저장   
    while (cur_node->parent->color == 0){     // cur_node의 부모가 red일 경우 (red가 아닐때까지 while문 반복)
        if (cur_node->parent == cur_node->parent->parent->left){    // cur_node가 left쪽에 있을 경우 
        uncle = cur_node->parent->parent->right;      // uncle은 cur_node 부모의 형제 노드 
        if (uncle->color == 0){           // cur_node의 부모와 uncle 모두 red일 경우 (case 3) 
            cur_node->parent->color = 1;    // cur_node의 부모의 색을 black으로  바꿈
            uncle->color = 1;               // cur_node의 uncle의 색을 black으로 바꿈
            cur_node->parent->parent->color = 0;      // cur_node의 부모의 부모의 색 red로 바꿈
            cur_node = cur_node -> parent -> parent;      // cur_node 와 cur_node의 부모의 부모 연결   
        }
        else {          // cur_node의 부모 노드만 red일 경우 (uncle은 black) -> LR 케이스 
            if(cur_node == cur_node->parent->right){    // cur_node 가 부모의 오른쪽 자식일 경우 
            cur_node = cur_node -> parent;    // cur_node의 기준을 cur_node의 부모로 바꾼후 left rotate
            left_rotate(t,cur_node);    
            }                           // cur_node의 부모 노드만 red이고, cur_node가 부모의 왼쪽 자식일 경우  -> LL 케이스 (LR 케이스를 수정하면 LL케이스가 된다.)
            cur_node->parent->color = 1;      // cur_node의 부모의 색을 black으로 바꿈
            cur_node->parent->parent->color = 0;    // cur_node의 부모의 부모의 색을 red로 바꿈  
            right_rotate(t,cur_node->parent->parent);     // 오른쪽 회전 기준을 cur_node의 부모의 부모로 바꿈     
        }
        }
        else{                                     // cur_node가 right쪽에 있을 경우 // 위와 방향만 바꾸고 동일   
        uncle = cur_node->parent->parent->left;
        if (uncle->color == 0){
            cur_node->parent->color = 1;
            uncle->color = 1;
            cur_node->parent->parent->color = 0;
            cur_node = cur_node -> parent -> parent;
        }
        else {
            if(cur_node == cur_node->parent->left){
            cur_node = cur_node -> parent;
            right_rotate(t,cur_node);
            }
            cur_node->parent->color = 1;
            cur_node->parent->parent->color = 0;
            left_rotate(t,cur_node->parent->parent);
        }
        }
    }
    t->root->color = 1;
    }
    ```    

* RB TREE 왼쪽으로 회전   
    ```
    void left_rotate(rbtree *t, node_t * cur_node){     // cur_node를 기준으로 왼쪽으로 회전   
    node_t *new_parent = cur_node->right;   //  new_parent를 curnode의 오른쪽 자녀 노드로 설정   
    cur_node->right = new_parent->left;     //  cur_node의 오른쪽 자녀에 new_parent의 왼쪽 자녀 붙이기
    if (new_parent -> left != t->nil){      //  new_parent의 왼쪽 자녀가 nil이 아닐때만  -> nil 노드에는 부모를 설정하면 안되기 때문  
        new_parent->left->parent = cur_node;    // new_parent의 왼쪽자녀의 부모를 cur_node로 설정  
    }
    new_parent->parent = cur_node->parent;    // cur_node가 가지고 있던 부모를 new_parent의 부모로 설정  
    if (cur_node->parent == t->nil){    // cur_node의 부모가 null인 경우 new_parent가 root 노드가 됨
        t->root = new_parent;
    }
    else if (cur_node == cur_node -> parent ->left){       // parent의 왼쪽 자녀가 cur_node일 경우   
        cur_node->parent->left = new_parent;          // parent의 왼쪽 자녀노드를 new_parent로 변경
    }
    else{
        cur_node->parent->right = new_parent;     // parent의 오른쪽 자녀가 cur_node일 경우   
    }                                           // parent의 오른쪽 자녀를 new_parent로 변경  
    new_parent->left = cur_node;        
    cur_node -> parent = new_parent;      // cur_node의 부모를 new_parent로, new_parent의 왼쪽 자녀를 cur_node로 설정   
    }
    ```   
* RB TREE 오른쪽으로 회전   
    ```
    void right_rotate(rbtree *t,node_t * cur_node){   // cur_node를 기준으로 왼쪽으로 회전   

    node_t *new_parent = cur_node->left;   //  new_parent를 curnode의 왼쪽 자녀 노드로 설정   
    cur_node->left = new_parent->right;     //  cur_node의 왼쪽 자녀에 new_parent의 오른쪽 자녀 붙이기
    if (new_parent -> right != t->nil){      //  new_parent의 오른쪽 자녀가 nil이 아닐때만  -> nil 노드에는 부모를 설정하면 안되기 때문  
        new_parent->right->parent = cur_node;    // new_parent의 오른쪽자녀의 부모를 cur_node로 설정  
    }
    new_parent->parent = cur_node->parent;    // cur_node가 가지고 있던 부모를 new_parent의 부모로 설정  
    if (cur_node->parent == t->nil){    // cur_node의 부모가 null인 경우 new_parent가 root 노드가 됨
        t->root = new_parent;
    }
    else if (cur_node == cur_node -> parent ->right){       // parent의 오른쪽 자녀가 cur_node일 경우   
        cur_node->parent->right = new_parent;          // parent의 오른쪽 자녀노드를 new_parent로 변경
    }
    else{
        cur_node->parent->left = new_parent;     // parent의 왼쪽 자녀가 cur_node일 경우   
    }                                           // parent의 왼쪽 자녀를 new_parent로 변경  
    new_parent->right = cur_node;        
    cur_node -> parent = new_parent;      // cur_node의 부모를 new_parent로, new_parent의 오른쪽 자녀를 cur_node로 설정   
    }
    ```   

