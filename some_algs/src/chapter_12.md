# Greedy

## Non-operlapping Intervals

Given an array of intervals `intervals` where `intervals[i] = [start_i, end_i]`, determine the 
largest number of intervals that are non-overlapping. 
(we allow the end time of one meeting to match the start time of another)

To solve thie problem let's condier the following intuition: If we were choosing the intevals 
to construct a non-overlapping subset of intervals, then we'd like the first interval to finish
as early as possible. 

Because this leaves us with the largest number of intervals to then choose from. This is the 
essence of a greedy strategy. We typically want to choose the largest quantity first to maximize 
an outcome (alternatively choose the smallest quantity to minimze a cost).

Also usually to take full advantage of a greedy strategy is that we need to structure the problem 
to utilize choosing the next largets (or next smallest) choice/element/thing/ect.

In our case we want the first choice to be the interval with the smallest end time, this mazimizes 
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


