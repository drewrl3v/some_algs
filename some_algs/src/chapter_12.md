# Greedy

## Making Change (Min Coins)

We have an unlimited supply of coins of the following denonminations: 1,2,5,10,20,50,100,1000.
Your task is to find the minimum number of coins that make up a bill of a given amount. 
For example you're handed a 101 bill, then you should return two coins of the following denominations:
`[1,100]`, two coins in total.

<details>
<summary>Solution</summary>


Intuitively to start we should pick the coin of largest denomination. If we made change we're done.
Otherwise, if we can still pick more coins of this amount, then we should. If we no longer can and we 
still haven't made change we should move on to the next largest coin.

`Note:` A common theme in greedy algorithms is we pick the largest or smallest value object/thing/move/strategy, 
so we can either maximize or minimize the number of next moves/objects/things/choices/strategies, ect.

`Warning: ` It just so happens we can solve this problem using a greedy strategy. This is because we 
satisify as so-called `exchangability` property. At the moment we won't explain what this is until 
later. But for coin change problems, the setup is exchangable if each coin is divisible by the previous one.
(This is a sufficient but not necessary condition. For example coins [1,2,5,10] can still be solved with a 
greedy strategy even though 2 does not divide 5.)

So for example if we instead had the following denomniations: 1,3,4 and are then asked to make change for 
a 6 bill, then the greedy strategy would give us the answer: `[4,1,1]` which uses three coins. But the 
optimal solution is: `[3,3]` only using two coins. With this out of the way, let's answer the problem:


<pre><code class="language-python">
def make_change(coins: List[int], amount: int) -> List[int]:
    num_coins = 0
    coins.sort()
    max_coin_index = len(coins) - 1
    while amount:
        while True:
            if coins[max_coin_index] > amount:
                max_coin_inex -= 1
            else:
                break
        amount -= coins[max_coin_index]
        num_coins += 1
</code></pre>
</details>





## Non-operlapping Intervals

Given an array of intervals `intervals` where `intervals[i] = [start_i, end_i]`, determine the 
largest number of intervals that are non-overlapping. 
(we allow the end time of one meeting to match the start time of another)

To solve thie problem let's condier the following intuition: If we were choosing the intevals 
to construct a non-overlapping subset of intervals, then we'd like the first interval to finish
as early as possible. 

This leaves us with the largest number of intervals to then choose from. Since we eant to determine 
the largest number of intervals, the choice of first interval that maximizine the number of choices 
we have left is optimal.

To reiterate, we want the first choice to be the interval with the smallest end time, this mazimizes 
the numebr of next choices we can look at. The next simplest thing we can do is then choose the next 
interval in our list (ordered by end times) that has a start time bigger than the current end time 
of our itnerval.

<details>
<summary>Solution</summary>


<pre><code class="language-python">
intervals = [[1,2],[2,4],[1,4]]
def max_non_overlapping(intervals: List[List[int]]) -> int:
    # First we sort the intervals by end times
    intervals.sort(key = lambda x : x[1])
    count = 1
    cur_end = intervals[0][1]
    for i, (start_i, end_i) in enumerate(intervals):
        if i == 0:
            continue
        else:
            if start_i >= cur_end:
                cur_end = end_i
                count += 1
    return count
</code></pre>
</details>


## Jump Frog

Given an array of nonnegative integers, a frog is initially at the first index of the array.
Each element in the array represents the maximum jump length at that position. Determine 
if the frog can reach the last index.


<details>
TODO: Explain the heuristics for determining the naive algorithm later.

<summary>Solution</summary>

<pre><code class="language-python">
def jump_frog(nums: List[int]) -> bool:
    n = len(nums)
    reachable = [False] * n
    reachable[0] = True
    for i in range(n-1):
        if not reachable[i]:
            continue
    for j in range(i, min(i + nums[i] + 1, n)):
        reachable[j] = True
    return reachable[-1]
</code></pre>


<details>
TODO: Explain the heuristics for determining the efficient algorithm later.

<summary>Alternative Solution</summary>

<pre><code class="language-python">

def jump_frog(nums: List[int]) -> bool:
    max_reachable = 0
    for i in range(len(nums)):
        # if it's impossible to reach the current index,
        # the it's not possible to reach the last index
        if i > max_reachable:
            return False
        max_reachable = max(max_reachable, i + nums[i])

        if max_reachable >= len(nums) - 1:
            return True
</code></pre>










