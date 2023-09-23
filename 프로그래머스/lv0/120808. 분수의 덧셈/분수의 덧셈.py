def find_gcd(a,b):
    while b:
        a,b = b, a%b
    return a

def simplify_fraction(numer, denom):
    common_divisor = find_gcd(numer, denom)
    simplified_numer = numer // common_divisor
    simplified_denom = denom // common_divisor
    return simplified_numer, simplified_denom

def solution(numer1, denom1, numer2, denom2):
    common_denominator = denom1 * denom2
    new_numer1 = numer1 * denom2
    new_numer2 = numer2 * denom1 
    result_numer = new_numer1 + new_numer2

    simplified_result = simplify_fraction(result_numer, common_denominator)
    return simplified_result
