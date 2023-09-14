def solution(numbers):
    new_num = sorted(numbers, reverse=True)
    return new_num[0] * new_num[1]