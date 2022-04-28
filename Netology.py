def quick_merge():
    my_list = []
    for _ in range(int(input())):
        s = int(input())
        my_list.extend(s)
        a = sorted(my_list)
    return a

print(*quick_merge())
