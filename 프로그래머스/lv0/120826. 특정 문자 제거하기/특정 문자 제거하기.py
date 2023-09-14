def solution(my_string, letter):
    table = str.maketrans('', '', letter)
    result = my_string.translate(table)
    return result