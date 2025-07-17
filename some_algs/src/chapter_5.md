# Depth First Search (DFS)

## Subsets (Recursive $O(2^n)$)

Give a list of integers, `nums`, return the list of all subsets of `nums`.

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


