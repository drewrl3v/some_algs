# Depth First Search (DFS)

## Subsets (Recursive $O(2^n)$)

Give a list of distinct integers, `nums`, return the list of all subsets of `nums`.

The basic idea for most Depth First Search Problems is as follows:

1. During each function call if you're done, there is nothing to do.
2. Otherwise you can choose 1 of finitely many decisions.
3. Keep exploring until you are done. 
4. Then go back and check the other decision you can make.

(It's easier to see the above thought process in action.)

Suppose we have the list nums = [1,2,3].

We start with an empty subset and decide what we'd like to inclue in it.

1. For example, at first we can include the element at index 0 (i.e. nums[0]) or not. Let's choose not to, so we currently have:

```
[]
```

2. Now we can choose to include nums[1] or not. Let's choose to include. Now we have: 

```
[2]
```

3. Again we can choose to include nums[2] or not. Let's choose to include, and the resulting subset is:

```
[2,3]
```

The idea is that we can undo a decision and then check the other decisions.
Implicitly we traversed a tree of decisions:

```
         []
        /  \
      [1]  *[]
           /  \
         *[2]  []
        /    \
     *[2,3]  [2]
```
**Note:** This is not the full decision tree, I only showed a portion of it and 
highlight the path traversed with `*`'s

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def subsets(nums: List[int]) -> List[List[int]]:
    res = [] # the result is going to be list of subsets
    subset = [] # a specific subset we'll construct

    dfs(i: int) -> None:
        ''' 
        At index i, we make a choice to add nums[i] to subset or not
        '''
        if i == len(nums): # if you reached the end of nums
            res.append(subset.copy())
            return
        else:              # you didn't exhause all your choices yet
            subset.append(nums[i])
            dfs(i+1)       # go to the next index: i+1

            # this gets called once dfs(i+1) returned. 
            # so undo adding nums[i]
            subset.pop() 

            # now we are on the path where we decided not to include nums[i]
            dfs(i+1) 
    dfs(0) # start the algorithm as index 0

    return res # dfs(0) has finished and res is populated with all the subsets of nums
print(subsets([1,2,3]))
</code></pre>
</details>

## Subsets (Recursive $O(2^n)$) - For Loop Version

Take the above solution. In the else statement can you write a for-loop to 
go over the indices of decisions? **Note:** The for-loop in this case will 
be redundant, however it's useful in problems where instead of two decisions 
you may have sever decisions you need to iterate through. To solve this problem take the above solution and in the `else` statement you can write 
a trivial and redundat for loop.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    subset = []

    dfs(i: int) -> None:
        if i == len(nums):
            res.append(subset.copy())
            return
        else:
            for j in range(i+1, i+2):
                subset.append(nums[i])
                dfs(j)
                subset.pop() 
                dfs(j) 
    dfs(0)
    return res
print(subsets([1,2,3]))
</code></pre>
</details>

## Subsets (Recursive $O(2^n)$) - For Loop & Depth

Now in addition to our for-loop version of the DFS for subsets, you should 
now define an equivalent versoin of the `dfs` function, namely: `dfs(i: int, depth: int)`. The depth starts at 0, and instead of using `if i == len(nums)` 
as the stop condition, you must now use the `depth` parameter to determine 
when to stop. **Note:** Once again, this is redundant, but this formulation 
is helpful when for example we want a stop condition based on the depth. 
For example produces all subsets of a set that have no more than 3 elements.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    subset = []
    dfs(i: int, depth: int) -> None:
        if depth == len(nums):
            res.append(subset.copy())
            return
        else:
            for j in range(i+1, i+2):
                subset.append(nums[i])
                dfs(j, depth+1)
                subset.pop() 
                dfs(j, depth+1) 
    dfs(0, 0)
    return res
print(subsets([1,2,3]))
</code></pre>
</details>

## Subsets II

Give a list of (not necessarily integers), `nums`, return the list of all subsets of `nums`.
Your solution may not contain duplicate subsets.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def subsets_no_dup(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    tmp = []
    def dfs(i: int) -> None:
    if i == len(nums):
        if tmp not in res:
            res.append(tmp.copy())
            return
        else:
            return
    else:
        tmp.append(nums[i])
        dfs(i+1)
        tmp.pop()
        dfs(i+1)
    dfs(0)
    return res
</code></pre>
</details>



## Subset Target Sum (Recursive O($2^n$))

Given an array of integers, `arr`, is there a subset that sums to a `target` integer? (Return True of False)

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def subset_sum(arr: List[int], target: int) -> bool:
    def dfs(i: int, curr_sum: int) -> bool:
        if i == len(arr):
            return curr_sum == target
        else:
            return dfs(i+1, curr_sum + arr[i]) or dfs(i+1, curr_sum)
    return dfs(0, 0)
print(subset_sum(arr=[2,5,6,9], target=9))
print(subset_sum(arr=[2,5], target=9))
</code></pre>
</details>

<details>
<summary>Alt Solution</summary>
Note that in the previous solution we had curr_sum which if we increment to 
the target we return True. A completely equivalent way of doing this is 
to pass in target and decrement and if we hit 0 we return True.
<pre><code class="language-python">
def subset_sum(arr: List[int], target: int) -> bool:
    def dfs(i: int, target: int) -> bool:
        if i == len(arr):
            return target == 0
        else:
            return dfs(i+1, target - arr[i]) or dfs(i+1, target)
    return dfs(0, target)
print(subset_sum(arr=[2,5,6,9], target=9))
print(subset_sum(arr=[2,5], target=9))
</code></pre>
</details>

## Target Sum

Given and array of integers, `nums` and an integer `target`, you want to consider the weighted 
sums:

 $$\sum_{n \in nums} \pm n$$

How many of these `+/-` weighted sums add up to `target`?

<details>
<summary>Solution</summary>
<pre><code class="language-python">
def target_sum(nums: List[int], target: int) -> int:
    count = [0]
    def dfs(i: int, cur_sum: int) -> None:
        if i == len(nums):
            if cur_sum == target:
                count[0] += 1
                return
        else:
            dfs(i+1, cur_sum + nums[i])
            dfs(i+1, cur_sum - nums[i])
    dfs(0,0)
    return count[0]
</code></pre>
</details>



## Combination Sum

Given an array of distinct integers `nums` and a target integer `target`, return a list of all 
unique combinations of `nums` where the chosen numbers sum to `target`. You may return the 
combinations in any order. 

**Note:** The same number may be chosen an unlimited number of times from 'nums'. 

**Note:** Two combinations are unique if the frequency of at least one of the chosen numbers is 
different.

<details>
<summary>Solution</summary>
<pre><code class="language-python">
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
print(combination_sum([2,3,6,7], 7))
</code></pre>
</details>

## Combination Sum II

Given an array of (not necessarily distinct) integers `nums` and a target integer `target`, return a list of all unique combinations of `nums` where the chosen numbers sum to `target`. You may return the combinations in any order.

<details>
<summary>Solution</summary>
<pre><code class="language-python">
def combination_sum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    res = []
    tmp = []
    def dfs(i: int, cur_sum: int) -> None:
        if cur_sum == target and tmp not in res:
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
print(combination_sum([2,3,6,7], 7))
</code></pre>
</details>

## Combinations (Recursive $O(kn^k)$)

Given a positive integer `n` and `k` with `k` $\leq$ `n`, implement a function 
called `choose` to return all the `k` combinations of the list of integers from `1` to `n`. Recall that the order of the combinations does not matter. Note, this will be our first example where we'll use a depth term and a for-loop.

<details>
<summary>Solution</summary>
<pre><code class="language-python">
# The problem is equivalent to the subset problem if k = n.
# But if k is less than n, we need to limit the depth so that we construct
# subsets of size no larger than 
# But to ensure that the subsets have no less than k elements, we must run 
# a for-loop to keep adding elements to our set until we reach the desired 
# size, k.
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
</code></pre>
</details>

## Beautiful Subsets (Construct Them)
You are given an array `nums` of positive integers and a positive integer `k`. 
A subset of `nums`is **beautiful** if it does not contain two integers with an 
absolute difference equal to `k`. 

Return the number of non-empty beautiful subsets of the array `nums`.

<details>
<summary>Solution</summary>
<pre><code class="language-python">
def beautiful_subsets(nums: List[int], k: int) -> List[List[int]]:
    # helper function
    def absolute_check(arr: List[int], element: int, k: int) -> bool:
        for a in arr:
            if abs(a - element) == k:
                return False
        return True
    # The DFS
    res = []
    tmp = []
    def dfs(i: int):
        if i == len(nums):
            if tmp == []:
                return
            else:
                res.append(tmp.copy())
                return
        else:
            if absolute_check(tmp, nums[i], k):
                tmp.append(nums[i])
                dfs(i+1)
                tmp.pop()
                dfs(i+1)
            else:
                dfs(i+1)
    dfs(0)
    return res
</code></pre>
</details>

## Beautiful Subsets (Count Them)
You are given an array `nums` of positive integers and a positive integer `k`. 
A subset of `nums`is **beautiful** if it does not contain two integers with an 
absolute difference equal to `k`. 

Return the number of non-empty beautiful subsets of the array `nums`.

<details>
<summary>Solution</summary>
<pre><code class="language-python">
# TODO
def count_beautiful_subsets(nums: List[int], k: int) -> int:
    # helper function
    def absolute_check(arr: List[int], element: int, k: int):
        for a in arr:
            if abs(a - element) == k:
                return False
        return True
    # The DFS
    tmp = []
    cur_count = [0]
    def dfs(i: int) -> None:
        if i == len(nums):
            if tmp == []:
                return
            else:
                cur_count[0] += 1
                return
        else:
            if absolute_check(tmp, nums[i], k):
                tmp.append(nums[i])
                dfs(i+1)
                tmp.pop()
                dfs(i+1)
            else:
                dfs(i+1)
    dfs(0)
    return cur_count[0]
</code></pre>
</details>







