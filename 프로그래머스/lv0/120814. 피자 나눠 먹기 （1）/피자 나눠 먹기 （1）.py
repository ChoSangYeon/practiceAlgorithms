def solution(n):
    if n/7 != int(n/7):
        return int(n/7+ 1)
    else:
        return int(n/7)