# Python (via Inductive Reasoning)

If you're new to python or inductive reasoning or both then welcome!
Also please try your best to just get through the notes. Follow along by example, and
it's okay to not understand everything and to skip over material that doesn't make sense.

---
### Inductive Reasoning

Some (but not all) algorithms can be intuitively reasoned via induction. I've noticed this connection is usually not directly addressed.

So let's review it before proceeding with the standard Data Structures and Algorithms.

### Warning:

If you're new to this, the induction section will feel like being blasted with a firehose. This might be unpleasant, so here are my suggestions:

1. Just understand the high-level concepts. The `Recursion`, section that proceeds this one has much simpler examples and will ease you into the following sections.

2. Don't get bogged down in the notation, just try to understand the overall concept:

For example, if I asked you what is the integer between 1 and 100? Just say 50.

If I ask whats 423/1658? Just say it's about 400/1600 = 4/16 = 1/4.

If I ask how many times can you divide 100 by 2. Just say 100/2 = 50, then 50/2 = 25, 25/2 is about 24/2 = 12, then 12/2 = 6, 6/2 = 3 and 3/2 is about 1.

So you can divide 100 by 2 about 7 times.

3. Again, don't get caught in the details, try your best to absorb the general idea.

4. Mathematically, induction is typically setup recursively and naturally this leads to recursive implementation of an inductive algorithm. However we will also provide iterative versions of the recursive algorithm, when possible.

## Let's Begin

There are many forms of induction, but we will turn our attention to a few forms and mention others forms as
we go through this notebook.

We let $T$ denote a mathematical statement

`Standard Induction:` 

**Base Case:**  $T$ holds for $n=1$

**Inductive Hypothesis:** Assume $T$ holds for $n-1$, where $n > 1$.

**What you want to prove:** We want to show that the inductive hypothesis implies that $T$ holds for $n$

`Example:`

$T$ is the statement that $1 + 2 + \dots + n = \frac{n(n+1)}{2}$.

Let's check the base case: $n=1$. Notice that simple algebra reveals that $\frac{1(1+1)}{2} = 1$. So the base case is satisfied.

Now for the inductive step. Assume that $T$ holds for $n > 1$, and consider the following sum:

$1 + 2 + \dots + n + (n+1)$. Notice that we can express this as:

$(1 + 2 + \dots + n) + (n+1)$. Now by the inductive hypothesis, we have that the expression
is equivalent to:

$\frac{n(n+1)}{2} + (n+1)$

$=\frac{(n+1)(n+2)}{2}$ as desired.

--

`Strong Induction:`

**Base Case(s):** $T$ holds for $n = 1, 2, 3, \dots, n_0$

**Inductive Hypothesis:** Assume $T$ holds for all $k$ such that $n_0 < k \leq n-1$

**What you want to prove:** We want to show that the inductive hypothesis implies that $T$ holds for $n$

We won't prove anything here, but we demonstrate a familiar recurrence that requires more than a single base case:

The fibonacci numbers are given by: $0,1,1,2,3,5,8,13,\dots$

Which can be expressed via the following recurrence-relation:

$f_0 = 0, f_1 = 1$ can be thought of the base cases and to generate the $n$-th fibonacci number we use:
$f_n = f_{n-1} + f_{n-2}$

--

`Divide and Conquer Induction:`

**Base Case** $T$ holds for $n=1$

**Inductive Hypothesis:** $T$ holds for $n//2$ with $n > 1$. (Note: $n//2$ is defined to be $n/2$ rounded down to the nearest integers.)

**What you want to prove:** We want to show that the inductive hypothesis implies that $T$ holds for $n$

Let's consider powers of $2$. For example computing: $2^3$, $2^8$, ect. 

As you may recall, the exponent informs the reader how many times they must multiply 2 times itself, so naturally you would think that to compute 

$2^8$ that this would require $8$ multiplications. However we can be clever with a Divide-and-Conquer approach:

Let $T$ be the statement that $2^n$ can be computed by knowing how to compute $2^{n//2}$ (and may need an extra multiplication by $2$)

Consider $2^n$. The base case for us will be $n=1$, in which case $2^1 = 2 \times 1 = 2 \times (2^0 \times 2^0) = 2 \times (2^{1//2} \times 2^{1//2})$. 

Now assume we know how to compute $2^n$ given $n//2$ for $n>1$. Now we consider
$2^{n+1}$. Notice that this is equivalent to:

$2^1 \times 2^n$, then by the induction hypothesis, we know how to compute 2^n based on knowing how to compute $2^{n//2}$
(i.e. $2^n = 2^{n//2} \times 2^{n//2}$).

So we just multiply $2^n$ by $2$ to show that $T$ holds for $n+1$ which proves the statement.

What is interesting about this approach is that it suggests that we only need $\log_2(n)$ multiplications to compute the power of 2.

For example, notice that $2^8$, can be computed as follows $2 \times 2 = 4$, then $4 \times 4 = 16$, then $16 \times 16 = 256 = 2^8$.
So we only used $3$ multiplications instead of $8$

---
## Simple Algorithms Constructed via Inductive Reasoning
---

The purpose of this entire notebook is to demonstrate how and when inductive reasoning can assist in
developing an algorithm. 

We will be explicit about our notion of inductive reasoning in the beginning of this notebook, but as
we become familiar with the technique, we use it as an implicit tool.

Psychologically there are some problems while inductive in nature, may be more intuitive to just dive 
into the problem.

So we may outright skip inductive reasoning all together.

## Summing a List of Numbers

We aim to create an algorithm called `sum(nums)`, which takes a list `nums` as input and returns 
the sum of the elements in the list.

`1. Standard Induction:`

We induct on the length of the list, $n$.

**Base Case:** If $n=1$, then return the element in the list, i.e. nums[0].

**Induction Hypothesis:** We assume we know how to sum a list of length $n-1$.

Notice that sum(nums) is equal to the sum of the list from indices $0$ to $n-2$ and the last index $n-1$.

sum(nums[0:n-1]) + nums[n-1]

By the inductive hypothesis we know how to find sum(nums[0:n-1]), so we are done.

```python
# Recursive Implementation
def rec_sum1(nums, nums_len):
    if nums_len == 1:
        return nums[0]
    else:
        return rec_sum1(nums, nums_len-1) + nums[nums_len-1]

nums = [-3,2,5]
print(rec_sum1(nums, len(nums)))
```

`2. Strong Induction:`

It's not really relevant in this case. 

**Base Case:** If $n=1$ return nums[0], if $n=2$, return nums[0] + nums[1]

**Inductive Hypothesis:** Suppose we can compute sum(nums) for nums_len $ \leq n-2$


Consider nums_len = n, then sum(nums, nums_len) = sum(nums, nums_len-2) + nums[nums_len-1] + nums[nums_len-2]

```python
def rec_sum2(nums, nums_len):
    if nums_len == 1:
        return nums[0]
    elif nums_len == 2:
        return nums[0] + nums[1]
    else:
        return rec_sum2(nums, nums_len-2) + nums[nums_len-1] + nums[nums_len-2]
nums = [-3,2,5]
print(rec_sum2(nums, len(nums)))
```

`3. Divide and Conquer Induction`

**Base Case:** If $n=1$, then we return nums[0]

**Inductive Hypothesis:** We know how to sum a list of length $n//2$ 

Now consider:

sum(nums) = sum(nums[0:n//2]) + sum([n//2+1:n-1])

```python
def rec_sum3(nums, low, high):
    if low == high:
        return nums[low]
    else:
        mid = low + (high - low) // 2
        return rec_sum3(nums, low, mid) + rec_sum3(nums, mid+1, high)

nums = [-3,2,5]
print(
    rec_sum3(nums, 0, len(nums) -1)
)
```

```python
def iter_sum3(nums):
    stack = [(0, len(nums) - 1)]
    total = 0

    while stack:
        low, high = stack.pop()
        if low == high:
            total += nums[low]
        else:
            mid = low + (high - low) // 2
            stack.append((low, mid))
            stack.append((mid + 1, high))

    return total

nums = [-3,2,5]
print(
    iter_sum3(nums)
)
```

## Sorting a List

`1. Standard Induction`

**Base Case:** If $n=1$, then just return the list (it is already sorted).

**Inductive Hypothesis:** Assume we know how to sort a list of length $< n$.

Now we consider: sort(nums[0:n]) = sort(nums[0:n-1]) ??? nums[n-1].

So we know how to sort a list of length $n-1$. But we then have to do something with the $n$ th element and
the sorted list of $n-1$ numbers. 

The most intuitive thing I can think of is that we must insert this element into the sorted list. 

So the ??? should be some kind of insert function.

But how do we insert? We need to create an algorithm for it!

## Insert Function

`Structured Induction`

**Base Case:**

If `nums` is empty then there is nothing to insert, so we are done.

If `nums` is not empty but the last element is greater than the second to last, then trivially the last element is inserted in the correct spot.

**Inductive Hypothesis:**

Given a sorted list `nums` where the first $n-1$ are sorted and the $n$ th number is less than the $n+1$ number,
we know how to insert it into its correct spot.


Consider a list of $n+1$ numbers where the fist $n$ are sorted and the $n+1$ number is less than $n$. 

First, let's swap the $n+1$ th and the $n$ th number.

Now we can insert the the $n+1$ th number into the sorted sublist of the $n-1$ numbers by the inductive hypothesis, so we are done.

Basically we performed the following operations

Given nums[0:n+1], swap the values between nums[n] and nums[n+1], then apply the insert function on nums[0:n]. 
Remember that nums[0:n] was already sorted in the first place, so nums[n] was the largest element.

We assumed that nums[n+1] < nums[n] (otherwise we'd have our base case and we'd be done), so with swap between the
elements still preserves order.

```python
def insert_into(nums, n):
    '''
    n := the length of the list num
    nums := the list of numbers to be sorted

    Inserts the last element of the sublist nums[0..n] into its correct position
    so that nums[0..n] is sorted
    '''
    # Base case: If the list is empty or already sorted
    if n == 0 or nums[n] >= nums[n-1]:
        return

    # Swap the last two elements if they are out of order
    nums[n], nums[n-1] = nums[n-1], nums[n]

    # Recursive call for the remaining list
    insert_into(nums, n-1)
```

## Return to Sorting a List

Now with our insert function, we can sort the list by following the base case
and the inductive hypothesis from earlier.

```python
def insertion_sort(nums, high):
    '''
    Sorts nums[0..high] using recursive insertion sort
    '''
    # Base case: If the list has one or no elements
    if high <= 1:
        return

    # Sort the first high-1 elements
    insertion_sort(nums, high-1)

    # Insert the high-th element into its correct position in the sorted array
    insert_into(nums, high-1)

# Test the function
nums2 = [5, 9, 0, -1, 100]
nums2 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Original list:", nums2)
insertion_sort(nums2, len(nums2))
print("Sorted list:", nums2)
```

I provided a recursive version of the insertion sort algorithm. However, below is the iterative version.

You may notice some resemblance when you peer into the iterative algorithm, notice that the while loop is behaving as if we call the insert function many times until the number is in the right spot.

It may take some getting used to, but if you follow the logic, you'll realize that it behaves identically to the recursive function.

```python
def insertion_sort(nums):
    '''
    Sorts an array using iterative insertion sort.
    '''
    # Iterate over the entire array
    for i in range(1, len(nums)):
        key = nums[i]

        # Move elements of nums[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1

        # Insert the key at after the element just smaller than it
        nums[j + 1] = key

# Test the function
nums = [5, 9, 0, -1, 100]
print("Original list:", nums)
insertion_sort(nums)
print("Sorted list:", nums)
```

As a quick note, if you change the form of induction you will obtain a different sorting algorithm.

For example, if you apply divide-and-conquer induction, you get what is known as the `merge sort`.

We cover this algorithm later, but hopefully you'll sense these patterns and when they apply as well as when they don't.