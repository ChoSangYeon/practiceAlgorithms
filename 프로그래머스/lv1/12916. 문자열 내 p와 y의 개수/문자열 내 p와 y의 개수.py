def solution(s):
    str = s.lower()
    if str.count('p') == str.count('y'):
        return True
    elif str.count('p') != str.count('y'):
        return False
    else:
        return True