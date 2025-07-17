# Depth First Search (DFS)

## Subsets (Recursive $O(2^n)$)

Give a list of integers, `nums`, return the list of all subsets of `nums`.

The basic idea for most Depth First Search Problems is as follows:

1. During each function call if you're done, there is nothing to do.
2. Otherwise you can choose 1 of finitely many decisions.
3. Keep exploring until you are done. 
4. Then go back and check the other decision you can make.

(It's easier to see the above thought process in action.)

Suppose we have the list nums = [1,2,3].

We start with an empty subset and decide what we'd like to inclue in it.

1. For example, at first we can include the element at index 0 (i.e. nums[0]) or not. Let's choose not to, so we currently have:

```
[]
```

2. Now we can choose to include nums[1] or not. Let's choose to include. Now we have: 

```
[2]
```

3. Again we can choose to include nums[2] or not. Let's choose to include, and the resulting subset is:

```
[2,3]
```

The idea is that we can undo a decision and then check the other decisions.
Implicitly we traversed a tree of decisions:

```
         []
        /  \
      [1]  *[]
           /  \
         *[2]  []
        /    \
     *[2,3]  [2]
```
**Note:** This is not the full decision tree, I only showed a portion of it and 
highlight the path traversed with `*`'s

