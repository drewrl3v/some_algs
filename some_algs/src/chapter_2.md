# Recursion

## Factorial (Linear Recursive)

Write a recursive function for the factorial function. You may assume that the input `n` is greater or equal to `0`.


<details>
<summary>Solution</summary>

<pre><code class="language-python">
def rec_factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * rec_factorial(n-1)

print(
    rec_factorial(5),
    rec_factorial(3),
    rec_factorial(0),
)
</code></pre>
</details>

## Factorial (Linear Iterative)

Write an iterative function for the factorial. You may assume that the input `n` is 
greater or equal to `0`.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def iter_factorial(n: int) -> int:
    res = 1
    if n == 0: return res
    for i in range(1, n+1):
        res *= i
    return res

print(
    iter_factorial(5),
    iter_factorial(3),
    iter_factorial(0),
)
</code></pre>
</details>

## Length of List (Linear Recursive)

Write a recursive function that computes the length of a list.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def rec_len(nums: List) -> int:
    if nums == []:
        return 0
    else:
        return 1 + rec_len(nums[1:])

print(
    rec_len([1,2,3])
)
</code></pre>
</details>


## Length of List (Linear Iterative)

Write an iterative function that computes the length of a list.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def iter_len(nums: List) -> int:
    res = 0
    if nums == []:
        return res

    for _ in nums:
        res += 1
    return res

print(
    iter_len([1,2,3])
)
</code></pre>
</details>

## Multiply Two Positive Integers (Linear Recursive)

Give two positive integers, implement a recursive function that computes their product.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def rec_mul(x: int, y: int) -> int:
    if y == 1:
        return x
    else:
        return x + rec_mul(x, y-1)

print(
    rec_mul(3,4),
    rec_mul(4,3),

)

</code></pre>
</details>

## Multiply Two Positive Integers (Linear Iterative)

Give two positive integers, implement an iterative function that computes their product.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def iter_mul(x: int, y: int) -> int:
    res = 0
    for _ in range(y):
        res += x
    return res

print(
    iter_mul(3,4),
    iter_mul(4,3),
)
</code></pre>
</details>

## Reversing A Sequence (Linear Recursive)

Write a recursive function that takes a list of integers, `nums`, and reverses the list.
Mutate the list, don't return a new list.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def rec_reverse(nums: List[int], left: int, right: int) -> None:
    if left == right:
        return
    else:
        nums[left], nums[right] = nums[right], nums[left]
        return rec_reverse(nums, left+1, right-1)

nums = [1,2,3]
print(nums)
rec_reverse(nums,0, len(nums)-1)
print(nums)

</code></pre>
</details>


## Reversing A Sequence (Linear Iterative)

Write an iterative function that takes a list of integers, `nums`, and reverses the list.
Mutate the list, don't return a new list.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def iter_reverse(nums: List[int]) -> None:
    left, right = 0, len(nums)-1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
    return

nums = [1,2,3]
print(nums)
iter_reverse(nums,0, len(nums)-1)
print(nums)

</code></pre>
</details>



















