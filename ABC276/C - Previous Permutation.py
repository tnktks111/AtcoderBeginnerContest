N = int(input())
P = list(map(int, input().split()))

def prev_permutation(n_list:list[int]):
    l, r = 0, 0
    change = 0
    for i in range(len(n_list) - 1):
        if n_list[i] > n_list[i + 1]:
            l = i
            change = i + 1
        if n_list[l] > n_list[i + 1] and n_list[change] < n_list[i + 1]:
            change = i + 1
    # print(change, l)
    n_list[change], n_list[l] = n_list[l], n_list[change]
    # print(n_list)
    for i in range((len(n_list) - l) // 2):
        n_list[l + i + 1], n_list[len(n_list) - i - 1] = n_list[len(n_list) - i - 1], n_list[l + i + 1]
    return n_list

print(*prev_permutation(P))
