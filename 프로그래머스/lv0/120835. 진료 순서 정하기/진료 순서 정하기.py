def solution(emergency):
    emgc_squence = sorted(emergency, reverse=True)
    return [emgc_squence.index(degree) + 1 for degree in emergency]