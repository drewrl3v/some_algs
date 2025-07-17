from typing import List
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