# 문서 검색

# import sys
# input = sys.stdin.readline

# book = str(input().strip())
# word = str(input().strip())

# result = 0
# for i in range(len(book)-len(word)+1):
#     count = 0 
#     answer = i
#     while answer < len(book)-len(word)+1:
#         if book[answer:answer+len(word)] == word:
#             count+=1
#             answer+=len(word)
#         else:
#             answer+=1
#     result = max(result,count)
# print(result)

# 초기 답안이 너무 느려서 다시 풀이 
import sys
input = sys.stdin.readline

book = str(input().strip())
word = str(input().strip())

answer = 0
count = 0
while answer < len(book)-len(word)+1:
    # 단어를 찾았을 경우, 단어의 길이 answer에 더하기 
    if book[answer:answer+len(word)] == word:
        count+=1
        answer+=len(word)
    else:
        answer+=1
print(count)