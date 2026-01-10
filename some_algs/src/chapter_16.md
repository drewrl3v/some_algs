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


## Maximum Sum Subarray

Given and array of integers `nums`, find the contiguous subarray with maximum
sum.

<details>
<summary>Solution</summary>

A common trick when optimizing over an array (or areas and volumes) that maintain order is to 
use a cummulative function (i.e. a prefix sum). So for example, if we let $S_i, S_j$ be 
prefix sums upto (and including) the i-th and i-th element of nums, notice that if $i < j$, that 
the contiguous sum of the subarray is simply $S_j - S_i$


So for example if we denote the $S$ to be 
an array of cummulative sums of integers: i.e. $S[3]$ is the sum of the first $3$ elements 
of nums, then the sum of any contiguous subarray: `nums[i:j+1]` may be written as 
$S[j] - S[i]$. We may view this problem as the following optimization problem:

$$
\max_{0 \leq i < j \leq n} S_j - S_i
$$

Now let's conceptually think about what makes a sum larger or smaller.

1. If $i$ is fixed, then we want $S_j$ to be as large as possible.
2. If $j$ is fixed, then we want $S_i$ to be as small as possible.

This is sometimes called `separation of variables`, (thinking about our calculus days). 
Imagine we have a multivariable function $f(i, j) = S_j - S_i$. And we want to find the maximum. 

If we stretch our imagination a little bit, pretend that $f(i, j)$ is like a two variable differentiable 
function. Then in calculus, we compute the gradient $\nabla_{(i,j)} f(i,j)$ set to $0$ and solve for $i$ and 
$j$. 

However the problem we have here is that:

1. $f$ is definitely not differentiable everywhere.

But we made a powerful observation. We found out that if $j$ is fixed, then picking $i$ so that $S_i$ is as small
as possible increases $f(i,j)$. Likewise, fixing $i$, then picking $j$ so that $S_j$ is as large as possible also 
increase $f(i,j)$. Since there is no dependence of $S_i$ and $S_j$ as long as we keep a variable fixed, we may 
re-write the optimization problem as follows:


$$
\max_{0 \leq j \leq n} (S_j - \min_{0 \leq i < j} (S_i))
$$

This may take some getting used-to. However if you look at the fomulation of the optimization problem, 
you can get a sense that you can iterate through $j$, then on a particular $j$, we then iterate through $i$, 
to see if we can make $S_i$ smaller. With some practice you look at such optimization problems and see that 
there are two for-loops. Let's implement the solution:

<pre><code class="language-python">
# TODO
def maximum_subarray(nums: List[float]) -> float:
    S = []
    for j in range(len(nums)):
        for i in range(j):
            current_sum = 
</code></pre>
</details>

