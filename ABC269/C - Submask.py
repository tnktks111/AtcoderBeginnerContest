N = int(input())

check_bit_list = []
for i in range(N.bit_length()):
    if (N >> i) & 1:
        check_bit_list.append(i)

res = []
for i in range(1 << len(check_bit_list)):
    tmp = 0
    for j in range(len(check_bit_list)):
        if (1 << j) & i:
            tmp += (1 << check_bit_list[j])
    res.append(tmp)

print(*res, sep="\n")