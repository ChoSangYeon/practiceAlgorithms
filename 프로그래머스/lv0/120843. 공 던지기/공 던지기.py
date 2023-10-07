def solution(numbers, k):
    numbers *= k
    new_numbers = []
    for i in range(0, len(numbers), 2):
        new_numbers.append(numbers[i])
    return new_numbers[k-1]