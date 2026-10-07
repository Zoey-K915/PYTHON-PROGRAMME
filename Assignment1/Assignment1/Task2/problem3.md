# Problem 3

## Your prompt to generate solution

```plain
# your AI model here
豆包
# your prompt here
根据截图里 python 代码，补全 sol () 函数。需要生成 [0,1,…,998] 的一个排列，满足对每一个下标 i，li [i] != i（错位排列）。只写 sol ()，不要修改 sat () 函数。
```

## Initial AI-generated solution

```python
# AI-generated solution here
lst = list(range(999))
    # 循环右移一位：最后一个元素放到最前面
    return [lst[-1]] + lst[:-1]
```

## (optional) Your edited solution

Note: you may skip this section if AI-generated solution is correct.

The errors found in the AI-generated solution:
1. to be filled here
2. 
3.

Your edited solution:

```python
# your solution after debugging here
```

## Screenshots of interaction with AI

Please capture the screenshot and paste it here.
![problem3_ss](image-2.png)
