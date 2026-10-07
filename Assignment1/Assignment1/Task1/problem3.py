from typing import List

# do not modify this function
def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))

def sol():
    """Find a permutation of [0, 1, ..., 998] such that the ith element is *not* i, for all i=0, 1, ..., 998."""
    # TODO: your implementation here
    odds = list(range(1,999,2))
    evens = list(range(0,999,2))
    li = odds + evens
    li[0], li[-1] = li[-1], li[0]
    return li  # return a list


print(sat(sol()))
