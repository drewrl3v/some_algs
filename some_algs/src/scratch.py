from typing import List, Set, Tuple
def subset_sum(arr: List[int], target: int) -> bool:
    def dfs(i: int, curr_sum: int) -> bool:
        if i == len(arr):
            if curr_sum == target:
                return True
            else:
                return False
        else:
            return dfs(i+1, curr_sum + arr[i]) or dfs(i+1, curr_sum)
    return dfs(0, 0)

print(subset_sum(arr=[2,5,6,9], target=9))

def subset_sum(arr: List[int], target: int) -> bool:
    def dfs(i: int, target: int) -> bool:
        if i == len(arr):
            return target == 0
        else:
            return dfs(i+1, target - arr[i]) or dfs(i+1, target)
    return dfs(0, target)
print(subset_sum(arr=[2,5,6,9], target=9))
print(subset_sum(arr=[2,5], target=9))


def choose(n: int, k: int) -> List[List[int]]:
    ls = [i for i in range(1, n+1)]
    res = []
    tmp = []
    def dfs(i: int, depth: int) -> None:
        if depth == k:
            res.append(tmp.copy())
            return
        else:
            for j in range(i, n):
                # add an element
                tmp.append(ls[j])
                # call the function again, we still need to add elements
                dfs(j+1, depth+1)
                tmp.pop()
    dfs(0, 0)
    return res
print(choose(4,2))

def combination_sum(nums: List[int], target: int) -> List[List[int]]:
    res = []
    tmp = []
    def dfs(i: int, cur_sum: int) -> None:
        if cur_sum == target:
            res.append(tmp.copy())
            return
        if i == len(nums) or cur_sum > target:
            return
        tmp.append(nums[i])
        dfs(i, cur_sum + nums[i])
        tmp.pop()
        dfs(i+1, cur_sum)
    dfs(0,0)
    return res

grid = [[0,0,0,0],
        [1,1,0,0],
        [0,0,0,1],
        [0,1,0,0]]

def count_paths(grid: List[List[int]]) -> int:

    #count = [0]
    ROWS, COLS = len(grid), len(grid[0])
    path = set()
    def dfs(r: int, c: int) -> int:
        if (min(r,c) < 1 or
            r >= ROWS or
            c >= COLS or
            (r,c) in path or
            grid[r][c] == 1
        ):
            return 0
     
        if (r,c) == (ROWS-1, COLS-1):
            return 1

       
        visit.add((r,c))
        count = 0
        count += dfs(r+1, c)
        count += dfs(r-1, c)
        count += dfs(r, c+1)
        count += dfs(r, c-1)
        
        visit.remove((r,c))
        return count

    return dfs(0,0)
print(count_paths(grid))




def cut_rod(n: int, p: List[int]) -> int:
    if n == 0:
        return 0
    res = -1 * float('inf')
    for i in range(1, n+1):
        res = max(res, p[i-1] + cut_rod(n=n-i, p=p))
    return res

p = [1,5,8,9,10,17,17,20,24,30]
print(cut_rod(n=4, p=p))

# memoized cut-rod

def memoized_cut_rod(n: int, p: List[int]) -> int:
    computed = [-1 * float('inf')] * len(p)
    computed[0] = 0
    def mem(n: int, p: List[int]) -> int:
        if n == 0:
            print("Called 0")
            return 0
        elif computed[n] >= 0:
            print(f"Called: {n}")
            return computed[n]
        else:
            res = -1 * float('inf')
            for i in range(1, n+1):
                print(n)
                res = max(res, p[i-1] + mem(n=n-i, p=p))
        computed[n] = res
        return res
    return mem(n, p)
p = [1,5,8,9,10,17,17,20,24,30]
print(memoized_cut_rod(n=4, p=p))

print("============")

def bottom_up_cut_rod(n: int, p: List[int]) -> int:
    computed = [0] + [-1 * float('inf')] * n
    for j in range(1, n+1):
        best = -1 * float('inf')
        for i in range(1, j+1):
            best = max(best, p[i-1] + computed[j-i])
        computed[j] = best
    return computed[n]

p = [1,5,8,9,10,17,17,20,24,30]
print(bottom_up_cut_rod(n=4, p=p))




'''
n! = n*(n-1) * .... * 3 * 2 * 1

'''

def fact(n):
  if n == 0:
    return 1
  else:
    return n * fact(n-1)
































