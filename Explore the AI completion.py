# 定义一个函数，接收一个整数列表，返回其中的偶数
def get_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]

# 示例用法
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)
print(even_numbers)  # 输出: [2, 4, 6, 8, 10]