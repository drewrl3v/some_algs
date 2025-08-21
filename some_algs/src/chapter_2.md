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


