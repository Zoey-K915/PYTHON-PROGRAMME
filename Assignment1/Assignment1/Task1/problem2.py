from typing import List

# do not modify this function
def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

def sol():
    """Find a list integers such that the integer i occurs i times, for i = 0, 1, 2, ..., 9."""
    # TODO: your implementation here
    return [1]*1 + [2]*2 + [3]*3 + [4]*4 + [5]*5 + [6]*6 + [7]*7 + [8]*8 + [9]*9


print(sat(sol()))
