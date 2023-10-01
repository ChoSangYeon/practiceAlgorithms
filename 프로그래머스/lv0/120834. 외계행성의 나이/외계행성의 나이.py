def solution(age):
    table = str.maketrans("0123456789", "abcdefghij")
    str_age = str(age)
    result = str_age.translate(table)
    return result