def solution(n):
    pizza = 6
    for i in range(max(n, pizza), (n*pizza)+1):
        if i % n == 0 and i % pizza == 0:
            result = i//pizza
            return result