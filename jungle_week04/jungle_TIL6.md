## 4주차 c언어 stack, queue, 알고리즘 풀이(python)   

* 2024 - 04 -16 (30일차)   

#### 퀴즈 리뷰  

* dp를 사용해서 피보나치 구현하기  
    * 상향식 접근법   
        ```
        # 피보나치 구현 (dp 상향식 접근) 

        def fibo(n):
            if n<=1:
                return n
            dp=[0]*n
            dp[0]=1
            dp[1]=1
            for i in range(2,n):
                dp[i] = dp[i-1] + dp[i-2]
            return dp[n-1]

        print(fibo(5))      # 5 출력 
        ```   
    * 하향식 접근법   
        ```
         # 피보나치 구현 (dp 하향식 접근)
        def fibo(n,dp=[]):
            if dp == []:            # dp가 비었을 첫경우에만 dp를 0으로 초기화  
                dp =[0]*(n+1)
            if n<=1:
                return n
            if dp[n] != 0:          # dp테이블에 값이 들어가 있으므로 그 값을 return    
                return dp[n]
            
            dp[n] = fibo(n-1) + fibo(n-2)
            return dp[n]
        print(fibo(5))      # 5 출력 
        ```    
#### c언어 과제 풀이(이진트리)   
* [c언어로 이진트리 구현하기(BT_Q1 ~ BT_Q8)](https://github.com/dongyeoppp/Data-Structures/tree/master/Binary_Tree)     

* 이진 트리 비교하기  (재귀로 구현)    
    ```
    int identical(BTNode *tree1, BTNode *tree2)     // 두개의 트리가 같은지 비교하기  

    {
        if (tree1 == NULL && tree2 == NULL){        // 두 개의 리스트 같을 경우  (둘다 null에 도착)
            return 1; 
        }
        if (tree1 == NULL){             // 두 개의 리스트가 다를 경우 (tree1에 노드만 null에 도착한 경우)
            if(tree2 !=NULL){
                return 0;
            }
        }
        if (tree2 == NULL){         // 두 개의 리스트가 다를 경우 (tree2에 노드만 null에 도착한 경우)
            if(tree1 !=NULL){
                return 0;
            }
        }
        if (tree1->item != tree2->item){        // 노드 안에 들어있는 값이 다를 경우  
            return 0;
        }
        int a = identical(tree1->left,tree2->left);     // 왼쪽으로 재귀 
        int b = identical(tree1->right,tree2->right);       // 오른쪽으로 재귀   
        if(a==1 && b==1){       // a,b모두 1이 return 된 경우 -> 두 리스트는 같다.  
            return 1;
        }
        else{
            return 0;
        }
    }
    ```   
* 이진 트리 깊이 구하기   
    ```
    int maxHeight(BTNode *node)     // 이진트리 깊이 구하기

    {
        int cnt = 1;        // 스택의 길이를 담음 
        int count = 0;      // 이진트리의 depth 값을 담음   
        int max = 0;        // depth값 저장   
        BTNode *removed;        // stack에서 pop을 한 값을 저장  
        BTNode *node1 = node;       // 루트 노드를 저장   
        Stack ss = { NULL };        // 비어있는 스택 생성 
        push(&ss,node);             // 루트 노드 먼저 스택에 넣어주기  
        while(1){
            if (cnt ==0){       // 스택이 비어있을 경우 break
                break;
            }
            removed = pop(&ss);     
            cnt--;      // cnt로 스택에 몇개의 요소가 들어있는지 알 수 있음   
            if (removed == node1->left || removed == node1->right){     // 스택에서 루트노드와 연결된 노드가 나왔을 경우 원래 count값 max에 저장 이후 , count 값 1로 재설정 (오른쪽 노드들 다 돌고 왼쪽노드로 간다.)
                max =count;
                count = 1;
            }
            if (removed->left != NULL){     // 왼쪽 노드가 null이 아닐 경우 push
                push(&ss,removed->left);        
                cnt++;          // push에 값을 넣어줄 때마다 cnt +1
            }
            if(removed ->right != NULL){        // 오른쪽 노드가 null이 아닐 경우 push
                push(&ss,removed->right);
                cnt++;
            }
            if (removed->right == NULL &&  removed->left == NULL)       // leaf node 일 경우 push 하지 않기 (count도 하지 않아야 함)
            {
                continue;
            }   
            count++;        // count +1 
        }
        if(max>=count){     // 오른쪽 노드, 왼쪽 노드의 depth를 비교하여 큰 값을 return    
            return max;
            }
        else{
            return count;
        }
    }
    ```   

* 자녀 노드가 한개인 노드 찾기   
    ```
    int countOneChildNodes(BTNode *node)        // 자녀노드를 한개 가지고 있는 노드 찾기  

    {
        Stack ss = {NULL};      // 새로운 스택 생성   
        push(&ss,node);     //  루트 노드 스택에 push
        int cnt = 1;
        int count = 0;      // 자녀 노드를 하나만 가지고 있는 노드의 개수 담기  
        BTNode *removed ;
        while(1){
            if(cnt==0){
                break;
            }
            removed = pop(&ss);
            cnt--;
            if((removed->left != NULL && removed->right == NULL)||(removed->left == NULL && removed->right != NULL)){       // 노드를 하나만 가지고 있을 경우 
                count++;
            }
            if(removed->left != NULL){      // removed->left 값이  null이 아닐 경우 push
                push(&ss,removed->left);
                cnt++;
            }
            if (removed->right != NULL){        // removed->right 값이 null이 아닐 경우 push
                push(&ss,removed->right);
                cnt++;
            }
        }
        return count;

    }
    ```   

* 이진 트리의 홀수 값 모두 더하기   
    ```
    int sumOfOddNodes(BTNode *node)     // 이진트리의 홀수 값 모두 더하기

    {
        Stack ss = {NULL};      // 새로운 stack 생성  
        BTNode *removed;        
        push(&ss,node);
        int cnt =1;
        int count = 0;
        while(1){
            if(cnt ==0){        // 스택에 값이 없을때까지 
                break;
            }
            removed = pop(&ss);
            cnt--;
            if (removed->item % 2 == 1){        // pop한 값이 홀수일 경우 count에 해당 노드 item 값 더하기
                count += removed->item;
            }
            if (removed->left != NULL){
                push(&ss,removed->left);
                cnt++;
            }
            if (removed->right != NULL){
                push(&ss,removed->right);
                cnt++;
            }
        }
        return count;
    }
    ```    
* 이진 트리 좌우 바꾸기   
    ```
    void mirrorTree(BTNode *node)       // 이진트리 좌우 위치 바꾸기 
    {
        Stack ss = {NULL};      // 빈 스택ss 생성    
        BTNode *removed;
        BTNode *save;
        push(&ss,node);
        int cnt = 1;
        int count = 0;
        while(1){
            if(cnt==0){
                break;
            }
            removed = pop(&ss); 
            cnt--;
            save = removed->left;
            removed->left = removed->right;     // left 노드와 right노드 바꾸기  
            removed->right = save;
            if(removed->left != NULL){
                push(&ss,removed->left);
                cnt++;
            }
            if(removed->right != NULL){
                push(&ss,removed->right);
                cnt++;
            }
        }

    }
    ```   
* m보다 작은 값 출력하기  
    ```
    void printSmallerValues(BTNode *node, int m)        // m 보다 작은 값 전부 출력하기  
    {
        Stack ss ={NULL};
        BTNode *removed;
        int cnt =1;
        push(&ss,node);
        while(1){
            if(cnt==0){
                break;
            }
            removed = pop(&ss);
            if(removed->item< m){
                printf("%d ",removed->item);        // pop 한 노드의 값이 m보다 작을경우 printf로 출력   
            }
            cnt--;
            if (removed->right != NULL){
                push(&ss,removed->right);
                cnt++;
            }
            if (removed->left != NULL){
                push(&ss,removed->left);
                cnt++;
            }
        }
    }
    ```    
* 이진 트리에서 가장 작은 값 찾기   
    ```
    int smallestValue(BTNode *node)         // 이진트리에서 가장 작은 값 찾기   
    {
        Stack ss ={NULL};
        BTNode *removed;
        int cnt=1;
        int mini = node->item;      // mini에 가장 작은 값 담기  
        push(&ss,node);
        while(1){
            if(cnt==0){
                break;
            }
            removed = pop(&ss);
            cnt--;
            if(removed->item < mini){
                mini = removed->item;       // pop한 노드의 값이 mini에 담겨 있던 값보다 작을 경우 mini 값 갱신   
            }
            if(removed->left != NULL){
                push(&ss,removed->left);
                cnt++;
            }
            if(removed->right != NULL){
                push(&ss,removed->right);
                cnt++;
            }
        }
        return mini;
    }
    ```    
* 이진트리에서 증손자 노드 찾기 (재귀로 구현)   
    ```
    int hasGreatGrandchild(BTNode *node)        // 증손자를 가진 노드 찾기 (해당 노드 -> 자녀노드 -> 손자 노드 -> 증손자 노드) 
    {
        BTNode *save = node;
        if(node ==NULL){
            return;
        }
        int count = 0 ;
        if (node->right==NULL && node->left==NULL){
            return count;
        }
        count++;        // 자녀노드가 있을 경우 count =1 
        int a= hasGreatGrandchild(node->left);      // 재귀   
        int b = hasGreatGrandchild(node->right); 
        if (a>=b){      // 해당 노드와 연결된 자녀노드들의 깊이 중 가장 큰 깊이를 구해야하기 때문에 a,b값을 비교하여 큰 값을 사용한다. 
            if(a+count>=3){         // a+count 값이 3이상일 경우 증손자 노드가 존재하는 것이므로 item 값 출력    
                printf("%d \n",node->item);
            }
            return a+count;     // 출력이후 return하여 값이 계속 재귀로 갱신되도록 해준다.  
        }
        if (a<b){
            if(b+count>=3){
                printf("%d\n",node->item);
            }
            return b+count;
        }

    }
    ```
#### 알고리즘 풀이   
* 2493번 [탑](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week04/bk_2493.py)   



