# Dynamic Programming


## Cut Rod

You have a rod of length `n` and a list of prices `p` indicating for length `i`
the price `p[i]` you may sell a rod of length `i` at. Find the best way to 
cut the rod so that you maximize your revenue. Report only the max possible 
revenue.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def cut_rod(n: int, p: List[int]) -> int:
    if n == 0:
        return 0
    res = -1 * float('inf')
    for i in range(1, n+1):
        res = max(res, p[i-1] + cut_rod(n=n-i, p=p))
    return res

p = [1,5,8,9,10,17,17,20,24,30]

print(cut_rod(n=4, p=p))
</code></pre>
</details>

## Cut Rod (Top-Down)

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def memoized_cut_rod(n: int, p: List[int]) -> int:
    computed = [-1 * float('inf')] * len(p)
    computed[0] = 0
    def mem(n: int, p: List[int]) -> int:
        if n == 0:
            return 0
        elif computed[n] >= 0:
            return computed[n]
        else:
            res = -1 * float('inf')
            for i in range(1, n+1):
                res = max(res, p[i-1] + mem(n=n-i, p=p))
        computed[n] = res
        return res
    return mem(n, p)

p = [1,5,8,9,10,17,17,20,24,30]
print(memoized_cut_rod(n=4, p=p))
</code></pre>
</details>
