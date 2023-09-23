from math import gcd

def solution(numer1, denom1, numer2, denom2):
    answer = []
    if denom1 == denom2:
        numer3 = numer1+numer2
        denom3 = denom1
    else:
        numer3 = numer1*denom2+numer2*denom1
        denom3 = denom1*denom2
    
    check_gcd = gcd(numer3, denom3)
    answer.append(numer3/check_gcd)
    answer.append(denom3/check_gcd)    
    
    return answer