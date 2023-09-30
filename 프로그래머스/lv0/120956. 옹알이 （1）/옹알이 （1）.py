import re
def solution(babbling):
    count = 0
    p = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for pattern in p:
            i = re.sub(pattern, ' ', i)
            print(i)
        if i.replace(' ', '') == '':
            count += 1
    return count