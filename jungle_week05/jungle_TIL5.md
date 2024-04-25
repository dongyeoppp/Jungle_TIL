## 5주차 Red-Black Tree 

* 2024 - 04 -23 (37일차)    

#### RB TREE 구현  

* [RB TREE 구현하기](https://github.com/dongyeoppp/rbtree-lab/blob/main/src/rbtree.c)  

* RB Tree 삭제하기   
    ```
    void delete_rbtree_node(rbtree *t, node_t *node)
    { // 노드 삭제
    if (node == t->nil)
    {
        return;
    }
    delete_rbtree_node(t, node->left);      // 재귀   
    delete_rbtree_node(t, node->right);
    free(node); // 해당 node 할당 해제
    }

    void delete_rbtree(rbtree *t) // rb tree 구조체가 차지했던 메모리 반환
    {
    if (t == NULL)
    {
        return;
    }
    delete_rbtree_node(t, t->root); // root 노드 부터 차례대로 할당 해제
    free(t->nil);                   // nil 노드 할당 해제
    free(t);                        // rb tree 할당 해제
    }
    ```    
* RB Tree 해당 키 값 검색하기  
    ```
    node_t *rbtree_find(const rbtree *t, const key_t key)
    { // rb tree 내에 해당 key가 있는지 탐색하여 있으면 해당 node pointer 반환
    node_t *node = t->root;
    while (node != t->nil)
    {
        if (node->key == key)
        {
        return node; // 주어진 key값을 찾으면 해당 노드 반환
        }
        else if (node->key > key) // 주어진 key 값이 더 작을 경우 left 탐색
        {
        node = node->left;
        }
        else if (node->key < key) // 주어진 key 값이 더 클 경우 right 탐색
        {
        node = node->right;
        }
    }
    return NULL; // key값이 없을 경우 null 반환
    }
    ```    

* RB Tree 최솟값 찾기   
    ```
    node_t *rbtree_min(const rbtree *t)
    { // rb tree 중 최소 값을 가진 node pointer 반환

    node_t *node = t->root;
    if (node == NULL)
    {
        return NULL;
    }
    while (node->left != t->nil)
    {
        node = node->left; // 가장 왼쪽에 있는 노드를 반환 (nil을 만나기 전까지 계속 left)
    }
    return node;
    }
    ```   

* RB Tree 최댓값 찾기   
    ```
    node_t *rbtree_max(const rbtree *t)
    { // rb tree 중 최대 값을 가진 node pointer 반환
    node_t *node = t->root;
    if (node == NULL)
    {
        return NULL;
    }
    while (node->right != t->nil)
    {
        node = node->right; // 가장 오른쪽에 있는 노드를 반환 (nil을 만나기 전까지 계속 right)
    }
    return node;
    }
    ```   

* RB Tree 노드 삭제하기
    * 노드 삭제 함수   
        ```
        int rbtree_erase(rbtree *t, node_t *p) // ptr로 지정된 node를 삭제하고 메모리 반환
        {
        node_t *change_node = p;         // 전임자를 받을 노드
        color_t save_color;              // 삭제되는 색을 저장
        node_t *child_node;              // 전임자 노드의 자녀 노드
        save_color = change_node->color; // 여기선 삭제될 노드의 색을 save_color에 저장 (삭제되는 노드의 색 = 삭제되는 색)
        if (p->left == t->nil)           // 삭제될 노드의 자녀가 오른쪽에 하나 있을 경우 (두 자녀 모두 nil일 경우 nil노드가 삭제될 노드의 부모노드에 자녀노드가 된다. )
        {
            child_node = p->right;         // 삭제될 노드의 오른쪽 자녀노드 -> child_node
            rb_transplant(t, p, p->right); // 삭제될 노드(p)의 오른쪽자녀 노드가 삭제될 노드의 자리를 대체한다.
        }
        else if (p->right == t->nil) // 삭제될 노드의 왼쪽 자녀노드 -> child_node
        {
            child_node = p->left;
            rb_transplant(t, p, p->left);
        }
        else // 삭제될 노드의 자녀가 두개 이상일 경우
        {
            change_node = tree_minimum(t, p->right); // minimum함수를 통해 전임자(change_node)를 찾는다.
            save_color = change_node->color;         // 전임자의 색을 save_color에 저장한다.
            child_node = change_node->right;         // 전임자 자리에 있는 노드 -> change_node, change_node의 오른쪽 노드 -> child 노드
            if (change_node->parent == p)            // 삭제되는 노드의 전임자가 삭제되는 노드의 오른쪽 자녀노드 일때
            {
            child_node->parent = change_node;
            }
            else
            {
            rb_transplant(t, change_node, change_node->right); // 전임자에 위치한 노드가 사라지므로 전임자의 오른쪽 자녀를 해당 자리로 위치시킨다.
            change_node->right = p->right;                     // 삭제된 노드의 오른쪽 자녀노드와 전임자 노드 연결
            change_node->right->parent = change_node;
            }
            rb_transplant(t, p, change_node); // 삭제되는 노드자리에 전임자를 대체한다.
            change_node->left = p->left;
            change_node->left->parent = change_node;
            change_node->color = p->color; // 전임자 노드의 색을 삭제되는 노드의 색을 가진다.
        }
        if (save_color == 1) // 없어진 노드 자리의 color가 black일 경우 레드블랙트리의 속성을 위배할 수 있음으로 fixup 함수를 호출
        {
            rb_delete_fixup(t, child_node); // child노드는 삭제된 노드의 자리르 대체하므로 doubly black이 붙는 노드이다. doubly black을 기준으로 fixup함수를 실행한다.
        }
        free(p);
        return 0;
        }
        ```    
    * 노드 삭제 이후 트리 재조정 함수  
        ```
        void rb_delete_fixup(rbtree *t, node_t *child_node)
        { // case에 따라 doubly black을 해결하는 함수
        while (child_node != t->root && child_node->color == 1)
        { // childe_node -> doubly black이 붙어있는 상태라고 생각
            if (child_node == child_node->parent->left)
            {                                                   // child node가 부모 노도의 왼쪽에 위치할 경우
            node_t *brother_node = child_node->parent->right; // brother 노드는 child node의 형제 노드
            if (brother_node->color == 0)                     // 형제노드의 color가 red일 경우  -> case1
            {
                brother_node->color = 1;
                child_node->parent->color = 0;
                left_rotate(t, child_node->parent);
                brother_node = child_node->parent->right;
            }
            if (brother_node->left->color == 1 && brother_node->right->color == 1) // 형제 노드가 black이면서 형제 노드의 자녀노드가 모두 black일 경우 -> case2
            {
                brother_node->color = 0;
                child_node = child_node->parent;
            }
            else
            {
                if (brother_node->right->color == 1)
                { // 형제 노드의 오른쪽 자녀 노드가 black, 왼쪽 자녀 노드가 red인 경우 -> case3
                brother_node->left->color = 1;
                brother_node->color = 0;
                right_rotate(t, brother_node);
                brother_node = child_node->parent->right;
                } // 형제 노드의 왼쪽 자녀 노드만 red인경우 -> case4
                brother_node->color = child_node->parent->color;
                child_node->parent->color = 1;
                brother_node->right->color = 1;
                left_rotate(t, child_node->parent);
                child_node = t->root;
            }
            }
            else // child node가 부모 노도의 오른쪽에 위치할 경우
            {
            node_t *brother_node = child_node->parent->left;
            if (brother_node->color == 0) // 형제노드의 color가 red일 경우  -> case1
            {
                brother_node->color = 1;
                child_node->parent->color = 0;
                right_rotate(t, child_node->parent);
                brother_node = child_node->parent->left;
            }
            if (brother_node->right->color == 1 && brother_node->left->color == 1) // 형제 노드가 black이면서 형제 노드의 자녀노드가 모두 black일 경우 -> case2
            {
                brother_node->color = 0;
                child_node = child_node->parent;
            }
            else
            {
                if (brother_node->left->color == 1) // 형제 노드의 오른쪽 자녀 노드가 black, 왼쪽 자녀 노드가 red인 경우 -> case3
                {
                brother_node->right->color = 1;
                brother_node->color = 0;
                left_rotate(t, brother_node);
                brother_node = child_node->parent->left;
                } // 형제 노드의 왼쪽 자녀 노드만 red인경우 -> case4
                brother_node->color = child_node->parent->color;
                child_node->parent->color = 1;
                brother_node->left->color = 1;
                right_rotate(t, child_node->parent);
                child_node = t->root;
            }
            }
        }
        child_node->color = 1;
        }
        ```    

    * 노드 이식 함수   
        ```
        void rb_transplant(rbtree *t, node_t *change_node, node_t *new_node)
        {                                    // change 노드를 대신해서 new 노드를 그 자리에 넣는 함수
        if (change_node->parent == t->nil) // 대체되는 노드의 부모가 없을 경우
        {
            t->root = new_node; // 삭제한 노드이 자녀가 부모가 노드가 된다.
        }
        else if (change_node == change_node->parent->left) // 대체되는 노드가 부모노드의 왼쪽에 위치할 경우
        {
            change_node->parent->left = new_node; // 대체되는 노드의 자녀노드를 부모노드의 왼쪽에 연결
        }
        else
        {                                        // 대체되는 노드가 부모노드의 오른쪽에 위치할 경우
            change_node->parent->right = new_node; // 대체되는 노드의 자녀노드를 부모노드의 오른쪽에 연결
        }
        new_node->parent = change_node->parent; // 새로운노드의 부모노드를 대체되는 노드의 부모노드로 바꿔준다.
        }
        ```      

    * 전임자 찾는 함수   
        ```
        node_t *tree_minimum(rbtree *t, node_t *cur_node) // 삭제 과정에서 삭제노드의 자녀노드가 두개일때 successor(후임자)로 대체
        {
        while (1)
        {
            if (cur_node->left == t->nil) // cur_node의 왼쪽 자녀노드가 nil일 경우 cur_node 반환
            {
            return cur_node;
            }
            cur_node = cur_node->left;
        }
        }
        ```   





