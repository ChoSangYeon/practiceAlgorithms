def solution(sides):
    tri_list = sorted(sides)
    if tri_list[2] < tri_list[0] + tri_list[1]:
        return 1
    else:
        return 2