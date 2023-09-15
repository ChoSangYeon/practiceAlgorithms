def solution(my_string):
    table = str.maketrans('', '','aeiuo')
    answer = my_string.translate(table)
    return answer