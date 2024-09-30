# 행렬 테두리 회전하기
def solution(rows, columns, queries):
    new = []
    count = 0
    # 1부터 (rows) x (columns) 까지의 행렬을 만듬 
    for i in range(rows):
        answer = []
        for j in range(columns):
            count +=1
            answer.append(count)
        new.append(answer)
    
    last = []
    for i in queries:
        result = float('inf')
        # 테두리에 가장 왼쪽 위에 있는 숫자를 change1에 저장 
        change1 = new[i[0]-1][i[1]-1]
        # 테두리의 가장 윗행의 왼쪽 기준 두번째 숫자부터 change1에 저장된 숫자로 바꿈 , change1은 반복문을 지날 때마다 갱신, result에 최소값 갱신 
        for j in range(i[1],i[3]):
            change2 = new[i[0]-1][j]
            new[i[0]-1][j] = change1
            change1 = change2
            result = min(result,new[i[0]-1][j])
        # 테두리의 가장 오른쪽 열의 윗쪽 기준 두번째 숫자부터 change1에 저장된 숫자로 바꿈 
        for k in range(i[0],i[2]):
            change2 = new[k][i[3]-1]
            new[k][i[3]-1] = change1
            change1 = change2
            result = min(result,new[k][i[3]-1])
        # 테두리의 가장 아랫 행의 오른쪽 기준 두번째 숫자부터 change1에 저장된 숫자로 바꿈 
        for h in range(i[3]-2,i[1]-2,-1):
            change2 = new[i[2]-1][h]
            new[i[2]-1][h] = change1
            change1 = change2
            result = min(result,new[i[2]-1][h])
        # 테두리의 가장 왼쪽 열의 아랫쪽 기준 두번째 숫자부터 change1에 저장된 숫자로 바꿈 
        for q in range(i[2]-2,i[0]-2,-1):
            change2 = new[q][i[1]-1]
            new[q][i[1]-1] = change1
            change1 = change2
            result = min(result,new[q][i[1]-1])
        # last에 최솟값 추가 
        last.append(result)
    return last