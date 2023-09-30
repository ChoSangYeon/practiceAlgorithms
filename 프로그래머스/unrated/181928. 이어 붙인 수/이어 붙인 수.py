def solution(num_list):
    even_lst = []
    odd_lst = []
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            even_lst.append(num_list[i])
        else:
            odd_lst.append(num_list[i])
    even_num = ''.join(map(str, even_lst))
    odd_num = ''.join(map(str, odd_lst))
    add_num = int(even_num) + int(odd_num)
    return add_num