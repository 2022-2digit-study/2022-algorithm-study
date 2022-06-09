# 프로그래머스 - 스택,큐 - 프린터:https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    answer = 0
    max_priorities = max(priorities)
    while True:
        val = priorities.pop(0)
        if max_priorities == val:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
            max_priorities = max(priorities)
        else:
            priorities.append(val)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer