def solution(my_string):
    table = str.maketrans('', '', 'abcdefghijklnmopqrstuvwxyz')
    result = my_string.translate(table)
    lst = []
    for i in result:
        lst.append(int(i))
    return sorted(lst)