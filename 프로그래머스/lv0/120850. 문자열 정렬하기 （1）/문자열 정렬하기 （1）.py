import re
def solution(my_string):
    p = re.compile('[0-9]')
    answer = list(sorted(map(int, p.findall(my_string))))
    return answer