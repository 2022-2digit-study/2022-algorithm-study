# 프로그래머스 - 스택,큐 - 주식가격: https://programmers.co.kr/learn/courses/30/lessons/42584

# 꾸역꾸역 풀었던 문제
# O(N^2) 시간복잡도를 가지고 있음.

def solution(prices):
    answer = [0 for _ in range(len(prices))]

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]:
                break

    return answer


# 정답을 참고한 풀이 스택 사용
def solution2(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        while stack != [] and stack[-1][1] > prices[i]:
            past, _ = stack.pop()
            answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer
