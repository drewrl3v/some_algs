# Chapter 3

In the previous section you will have noticed that I provided
recursive and iterative versions to each example. To newcombers 
recursion may lok like magic, because the function is self-referential. 

We'll take a step back from recusion and look at the `data structure` that makes recursion possible in the first place. 
It's called the `stack`.

Think of it like a stack of plates. You can place them on top 
of each other, one-by-one. If you want to remove a plate, you 
are only allowed to move the top-most plate. 

When we place a plate on the stack we `append` it to the stack. 

When we remove a plate from the top of the stack we `pop` it off the stack.

We will show how to solve a variety of problems using stacks.

## Recursively Remove Elements From A Stack

You are given a stack of integers called `nums`. Write a function 
that recursively removes all the elements from `nums`.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def rec_remove_from_stack(nums: List[int]) -> None:
    if nums: # returns True if nums is not empty
        nums.pop() # remove plate from top of stack
        return rec_remove_from_stack(nums)

nums = [3,4,5,1]
print(nums)

rec_remove_from_stack(nums)
print(
    nums
)
</code></pre>
</details>

## Iteratively Remove Elements From A Stack

You are given a stack of integers called `nums`. Write a function 
that iteratively removes all the elements from `nums`.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def iter_remove_from_stack(nums: List[int]) -> None:
    while nums:
        nums.pop()

nums = [3,4,5,1]
print(nums)

iter_remove_from_stack(nums)
print(
    nums
)
</code></pre>
</details>

Okay from here on out, I won't provide recursive and iterative implementations. We just use whatever is natural for the problem

## Reverse A Stack

You have a stack of integers, `nums`. Write a function that 
reverses the order of `nums`. You may use and return an auxillary stack

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def reverse_stack(nums: List[int]) -> List[int]:
    tmp_stack = []
    while nums:
        x = nums.pop()
        tmp_stack.append(x)
    return tmp_stack

nums = [1,2,3,4]
print(nums)
print(reverse_stack(nums))
print(nums)
</code></pre>
</details>

## Simple Valid / Balanced Parenthesis

You are give a string of parenthesis. For example `())))()()` or `(()` or `()` or `()()` or `(()())`, ect.

A string is called `valid` if for each open parenthesis, `(` there is a corresponding closed parenthesis, `)`.

So `())))()()` and `(()` are invalid, but the following are valid: `()` , `()()` , `(()())`

Write a function that takes in a string of parenthesis and returns `True` if the string is valid and `False` otherwise.

<details>
<summary>Solution</summary>

The idea is that we read a string from left-to-right. If we see a `(`, we append this to a stack.
If we encounter a `)` then we need to check if there is a corresponding left parenthesis in the stack. If there isn't or if the stack is empty, we can return False because it's impossible to
match the right parenthesis with a corresponding left one. Othewise, the pair is matched, we pop
what we had in the stack and continue scanning the string. 

If we made it to the very end and the stack is empty, this must mean every left parenthesis had 
a vlide corresponding right parenthesis and we can return True. Otherwis we return False.

<pre><code class="language-python">
def is_valid(s: str) -> bool:
    stack = []
    for tok in s:
        if tok == '(':
            stack.append(tok)
        if tok == ')':
            if not stack: # if the stack is empty
                return False
            elif stack[-1] != '(': # check if the corresponding left parenthesis exists.
                return False
            else:
                stack.pop()
    return not stack # if the stack is empty, then the string was balanced.

print(
    is_valid('()'), '\n',
    is_valid('())'), '\n',
    )
</code></pre>
</details>


## Convert Decimal To Binary

Recall that to convert a decimal number to binary you:

1. Divide the number by 2 and record the remainder.
2. Keep the integer part of the divided number and go back to step 2.
3. Repeat this process until the number is 0.

Here is a simple example, consider the decimal number 10:

```
Remainders:            0     1     0     1
                10 --> 5 --> 2 --> 1 --> 0
```

So the binary representation of 10 is (when you read the remainders from right-to-left) 1010.
The trick here is that this problem is basically the base 2 logrithm from the recursion 
chapter. Also for ease, we will represent the binary number as a string.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def decimal_to_binary(n: int) -> str:
    remainder_stack = []
    while n > 0:
        remainder = n % 2
        remainder_stack.append(str(remainder))
        n = n // 2

    # the answer is in the remainder stack, but it's reversed
    # so we should reverse the stack (an earlier problem in this section)
    ans = []
    while remainder_stack:
        x = remainder_stack.pop()
        ans.append(x)
    
    return ''.join(ans) # fancy way to concatenate all the characters in the ans list.

print(
    decimal_to_binary(42)
)
</code></pre>
</details>



