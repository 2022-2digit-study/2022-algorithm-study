# 프로그래머스 (해시) 전화번호 목록: https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    hash = {}
    for i, phone_number in enumerate(phone_book):
        hash[phone_number] = i
    for phone_number in hash.keys():
        first_word = ""
        for number in phone_number:
            first_word += number
            if first_word in hash and first_word != phone_number:
                return False
    return True
