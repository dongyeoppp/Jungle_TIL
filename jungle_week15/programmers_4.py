def solution(tickets):
    # 모든 공항을 담은 airport 리스트 생성
    airport = []
    for i in tickets:
        if i[0] not in airport:
            airport.append(i[0])
        if i[1] not in airport:
            airport.append(i[1])
    # 사전 순으로 공항 정렬 
    airport.sort()
    new_airport = {}
    number = 1
    start = 0
    # 공항 이름을 키값으로 하고 해당 index를 value값으로 가지는 new_airport 사전 생성
    for i in airport:
        new_airport[i] = number
        if i == "ICN":
            start = number
        number+=1
    graph = [[] for i in range(number)]
    # 항공권 리스트로 graph 생성 
    for i in tickets:
        graph[new_airport[i[0]]].append(new_airport[i[1]])
    # new_airport 사전의 key값과 value값을 거꾸로 바꾸어 re_airport라는 사전 생성
    re_airport = {v:k for k,v in new_airport.items()}
    # graph의 각 리스트를 내림차순으로 정렬 
    for i in graph:
        i.sort(reverse = True)
    
    result = []
    def dfs(graph,start):
        # 재귀를 이용한 dfs
        while graph[start]:
            next = graph[start].pop()
            dfs(graph,next)
        result.append(re_airport[start])
        
    dfs(graph,start)
    return result[::-1]