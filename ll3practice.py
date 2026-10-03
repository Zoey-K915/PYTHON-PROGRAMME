def sum_to(n):
    if n <= 0:
        return 0
    else:
        return n + sum_to(n - 1)
    end

n=int(input("请输入一个正整数："))
print(sum_to(n))