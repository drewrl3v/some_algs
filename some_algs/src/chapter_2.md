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


## Base-2 Integer-Logarithm (Log Recursive)

Write a recursive function that computes the base 2 log of an integer:

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def rec_log2(number: int) -> int:
    if number == 1:
        return 0
    else:
        return 1 + rec_log2(number // 2)

print(
    rec_log2(100)
)

</code></pre>
</details>

## Base-2 Integer-Logarithm (Log Iterative)

Write an iterative function that computes the base 2 log of an integer:

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def iter_log2(number: int) -> int:
    res = 0
    while number > 1:
        res += 1
        number = number // 2
    return res

print(
    iter_log2(100)
)

</code></pre>
</details>

## Determine If Palindrome (Linear Recursive)

Implement a recursive function to determine if a string is a palindrome or not.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def rec_is_palindrome(word: str, left: int, right: int) -> bool:
    if left == right:
        return True
    else:
        current_check = (word[left] == word[right])
        return current_check and rec_is_palindrome(word, left+1, right-1)

word1 = "racecar"
word2 = "a"
word3 = "hello"
print(
    rec_is_palindrome(word1, 0, len(word1)-1),
    rec_is_palindrome(word2, 0, len(word2)-1),
    rec_is_palindrome(word3, 0, len(word3)-1),

)

</code></pre>
</details>

Note we can have another variation of this recursive function that returns False, the moment
we see that the word[left] and word[right] don't match.


<details>
<summary>Solution</summary>

<pre><code class="language-python">
def rec_is_palindrome(word: str, left: int, right: int) -> bool:
    if left == right:
        return True
    else:
        if word[left] != word[right]:
            return False
        return rec_is_palindrome(word, left+1, right-1)

word1 = "racecar"
word2 = "a"
word3 = "hello"
print(
    rec_is_palindrome(word1, 0, len(word1)-1),
    rec_is_palindrome(word2, 0, len(word2)-1),
    rec_is_palindrome(word3, 0, len(word3)-1),

)

</code></pre>
</details>

## Determine If Palindrome (Linear Iterative)

Implement an iterative function to determine if a string is a palindrome or not.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def iter_is_palindrome(word: str) -> bool:
    left, right = 0, len(word)-1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -=1
    return True


word1 = "racecar"
word2 = "a"
word3 = "hello"
print(
    iter_is_palindrome(word1, 0, len(word1)-1),
    iter_is_palindrome(word2, 0, len(word2)-1),
    iter_is_palindrome(word3, 0, len(word3)-1),

)

</code></pre>
</details>


## Consonants And Vowels (Linear Recursive)

Determine if a string has more vowels than consonants.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
vowels = "aeiou"
def rec_more_vowels_than_consonants(s: str, 
                                cur_index: int, 
                                cons_count: int, 
                                vows_count: int) -> bool:
    if cur_index == 0:
        if s[cur_index] in vowels:
            vows_count += 1
        else:
            cons_count += 1

        return vows_count > cons_count
    else:
        if s[cur_index] in vowels:
            vows_count += 1
        else:
            cons_count += 1

        return more_vowels_than_consonants(s, 
                                            cur_index-1, 
                                            cons_count, 
                                            vows_count)


word1 = "hello"
word2 = "see"
print(
    rec_more_vowels_than_consonants(word1, 
                                cur_index = len(word1)-1, 
                                cons_count=0, 
                                vows_count=0),
    rec_more_vowels_than_consonants(word2, 
                                cur_index = len(word2)-1, 
                                cons_count=0, 
                                vows_count=0),
)
</code></pre>
</details>


## Consonants And Vowels (Linear Iterative)

Determine if a string has more vowels than consonants.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
vowels = "aeiou"
def iter_more_vowels_than_consonants(s: str) -> bool:
    vow_count, con_count = 0, 0
    for char in s:
        if char in vowels:
            vow_count += 1
        else:
            con_count += 1
    return vow_count > con_count

word1 = "hello"
word2 = "see"
print(
    iter_more_vowels_than_consonants(word1),
    iter_more_vowels_than_consonants(word2),
)
</code></pre>
</details>

## Even Before Odd (Recursive)

Write a recursive function that rearranges a sequence of integer values so that all the even
values appear before all the odd values.

<details>
<summary>Solution</summary>

The trick is to keep track of two indices. Denote f the first index
and s the second index. If you encounter an odd element, hold the f index
and keep advancing the s index until you see an even number. Once you see 
an even number, swap the elements and advance the first index and the second
index. See below with the list [1,3,2,4]:

```
1 3 2 4
f s
f   s 
2 3 1 4
  f   s
2 4 1 3
    f s -> Done

the cases to consider is when when the corresponding elements num[f], num[s]
are the following (even, even), (eve, odd), (odd, even), (odd, odd). How you 
advance the pointer in each case.
```

<pre><code class="language-python">
def recur_even_before_odd(nums: List[int], f: int, s: int) -> None:
    if s == len(nums):
        return 
    else:
        if nums[f] % 2 == 1 and nums[s] % 2 == 0:
            nums[f], nums[s] = nums[s], nums[f]
            recur_even_before_odd(nums, f+1, s+1)
        elif nums[f] % 2 == 1 and nums[s] % 2 == 1:
            recur_even_before_odd(nums, f, s+1)
        elif nums[f] % 2 == 0 and nums[s] % 2 == 1:
            recur_even_before_odd(nums, f+1, s+1)
        else: # both are even
            recur_even_before_odd(nums, f+1, s+1)

nums = [1,2,3]
print(nums)
recur_even_before_odd(nums, 0, 1)
print(nums)

nums = [1,3,2,4]
print(nums)
recur_even_before_odd(nums, 0, 1)
print(nums)
</code></pre>
</details>




























