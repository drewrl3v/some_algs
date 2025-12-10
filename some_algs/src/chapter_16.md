# Optimization

The following are classic programming problems (we've encounted some before).

However we look at them from the lense of optimization when solving them.

## Cumulative Sums:

Given an array of numbers, `nums`, write a function that returns an array of 
the cummulative sums of the numbers of nums. For example if 
`nums = [0.3, 4, -2]`, then you should return `[0.3, 4.3, 2.3]`.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def cumulative_sum(nums: List[float]) -> List[float]:
    cum_sum = 0
    res = [0] * len(nums)
    for i in range(len(nums)):
        cum_sum += nums[i]
        res[i] = cum_sum
    return res

nums = [0.3, 4, -2]
print(cumulative_sum(nums))
</code></pre>
</details>


## Prefix Sums:

Given an array of numbers, `nums`, and an index `i`, return the cummulative 
sum of the array up to (and including) `nums[i]`.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def prefix_sum(nums: List[float], i: int) -> List[float]:
    cum_sum = 0
    for j in range(len(nums)):
        cum_sum += nums[j]
        if j == i:
            break
    return cum_sum

nums = [0.3, 4, -2]
print(prefix_sum(nums, 1))
</code></pre>
</details>




