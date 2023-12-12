def jiange_zhucha(list):
    num = len(list)
    if num <= 1:
        return 0
    num_half = num // 2
    cha = sum(list[num - num_half:num]) - sum(list[0:num_half])
    result = cha / (num_half * math.ceil(num / 2))
    return result
