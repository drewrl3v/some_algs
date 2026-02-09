from typing import List, Set, Tuple
def subset_sum(arr: List[int], target: int) -> bool:
    def dfs(i: int, curr_sum: int) -> bool:
        if i == len(arr):
            if curr_sum == target:
                return True
            else:
                return False
        else:
            return dfs(i+1, curr_sum + arr[i]) or dfs(i+1, curr_sum)
    return dfs(0, 0)

print(subset_sum(arr=[2,5,6,9], target=9))

def subset_sum(arr: List[int], target: int) -> bool:
    def dfs(i: int, target: int) -> bool:
        if i == len(arr):
            return target == 0
        else:
            return dfs(i+1, target - arr[i]) or dfs(i+1, target)
    return dfs(0, target)
print(subset_sum(arr=[2,5,6,9], target=9))
print(subset_sum(arr=[2,5], target=9))


def choose(n: int, k: int) -> List[List[int]]:
    ls = [i for i in range(1, n+1)]
    res = []
    tmp = []
    def dfs(i: int, depth: int) -> None:
        if depth == k:
            res.append(tmp.copy())
            return
        else:
            for j in range(i, n):
                # add an element
                tmp.append(ls[j])
                # call the function again, we still need to add elements
                dfs(j+1, depth+1)
                tmp.pop()
    dfs(0, 0)
    return res
print(choose(4,2))

def combination_sum(nums: List[int], target: int) -> List[List[int]]:
    res = []
    tmp = []
    def dfs(i: int, cur_sum: int) -> None:
        if cur_sum == target:
            res.append(tmp.copy())
            return
        if i == len(nums) or cur_sum > target:
            return
        tmp.append(nums[i])
        dfs(i, cur_sum + nums[i])
        tmp.pop()
        dfs(i+1, cur_sum)
    dfs(0,0)
    return res

grid = [[0,0,0,0],
        [1,1,0,0],
        [0,0,0,1],
        [0,1,0,0]]

def count_paths(grid: List[List[int]]) -> int:

    #count = [0]
    ROWS, COLS = len(grid), len(grid[0])
    path = set()
    def dfs(r: int, c: int) -> int:
        if (min(r,c) < 1 or
            r >= ROWS or
            c >= COLS or
            (r,c) in path or
            grid[r][c] == 1
        ):
            return 0
     
        if (r,c) == (ROWS-1, COLS-1):
            return 1

       
        path.add((r,c))
        count = 0
        count += dfs(r+1, c)
        count += dfs(r-1, c)
        count += dfs(r, c+1)
        count += dfs(r, c-1)
        
        path.remove((r,c))
        return count

    return dfs(0,0)
print(count_paths(grid))




def cut_rod(n: int, p: List[int]) -> int:
    if n == 0:
        return 0
    res = -1 * float('inf')
    for i in range(1, n+1):
        res = max(res, p[i-1] + cut_rod(n=n-i, p=p))
    return res

p = [1,5,8,9,10,17,17,20,24,30]
print(cut_rod(n=4, p=p))

# memoized cut-rod

def memoized_cut_rod(n: int, p: List[int]) -> int:
    computed = [-1 * float('inf')] * len(p)
    computed[0] = 0
    def mem(n: int, p: List[int]) -> int:
        if n == 0:
            print("Called 0")
            return 0
        elif computed[n] >= 0:
            print(f"Called: {n}")
            return computed[n]
        else:
            res = -1 * float('inf')
            for i in range(1, n+1):
                print(n)
                res = max(res, p[i-1] + mem(n=n-i, p=p))
        computed[n] = res
        return res
    return mem(n, p)
p = [1,5,8,9,10,17,17,20,24,30]
print(memoized_cut_rod(n=4, p=p))

print("============")

def bottom_up_cut_rod(n: int, p: List[int]) -> int:
    computed = [0] + [-1 * float('inf')] * n
    for j in range(1, n+1):
        best = -1 * float('inf')
        for i in range(1, j+1):
            best = max(best, p[i-1] + computed[j-i])
        computed[j] = best
    return computed[n]

p = [1,5,8,9,10,17,17,20,24,30]
print(bottom_up_cut_rod(n=4, p=p))




'''
n! = n*(n-1) * .... * 3 * 2 * 1

'''

def fact(n):
  if n == 0:
    return 1
  else:
    return n * fact(n-1)

print("=============")

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

print("=============")

def rec_len(nums: List) -> int:
    if nums == []:
        return 0
    else:
        return 1 + rec_len(nums[1:])

print(
    rec_len([1,2,3])
)

print("=============")
def rec_mul(x: int, y: int) -> int:
    if y == 1:
        return x
    else:
        return x + rec_mul(x, y-1)

print(
    rec_mul(3,4),
    rec_mul(4,3),

)

print("=============")

def iter_mul(x: int, y: int) -> int:
    res = 0
    for _ in range(y):
        res += x
    return res

print(
    iter_mul(3,4),
    iter_mul(4,3),
    iter_mul(4,1),
    iter_mul(1,4),
)

print("=============")

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


print("=============")
def iter_reverse(nums: List[int]) -> None:
    left, right = 0, len(nums)-1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return

nums = [1,2,3]
print(nums)
iter_reverse(nums)
print(nums)


print("=============")
def rec_log2(number: int) -> int:
    if number == 1:
        return 0
    else:
        return 1 + rec_log2(number // 2)

print(
    rec_log2(100)
)

print("=============")
def iter_log2(number: int) -> int:
    res = 0
    while number > 1:
        res += 1
        number = number // 2
    return res

print(
    iter_log2(100)
)

print("=============")
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

print("=============")
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
    iter_is_palindrome(word1),
    iter_is_palindrome(word2),
    iter_is_palindrome(word3),

)


print("====================")
vowels = "aeiou"
def more_vowels_than_consonants(s: str, cur_index: int, cons_count: int, vows_count: int) -> bool:
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

        return more_vowels_than_consonants(s, cur_index-1, cons_count, vows_count)


word1 = "hello"
word2 = "see"
print(
    more_vowels_than_consonants(word1, cur_index = len(word1)-1, cons_count=0, vows_count=0),
    more_vowels_than_consonants(word2, cur_index = len(word2)-1, cons_count=0, vows_count=0),
)


print("====================")
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

print("==========================")
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

print("======================")
def iter_even_before_odd(nums: List[int]) -> None:
    f, s = 0, 1
    while s < len(nums):
        if nums[f] % 2 == 1 and nums[s] % 2 == 0:
            nums[f], nums[s] = nums[s], nums[f]
            f += 1
            s += 1
        elif nums[f] % 2 == 1 and nums[s] % 2 == 1:
            s += 1
        elif nums[f] % 2 == 0 and nums[s] % 2 == 1:
            f += 1
            s += 1
        else: # both are even
            f += 1
            s += 1

nums = [1,2,3]
print(nums)
iter_even_before_odd(nums)
print(nums)

nums = [1,3,2,4]
print(nums)
iter_even_before_odd(nums)
print(nums)



### RECURSION
print("=====================")
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

print("====================")
def iter_remove_from_stack(nums: List[int]) -> None:
    while nums:
        nums.pop()

nums = [3,4,5,1]
print(nums)

iter_remove_from_stack(nums)
print(
    nums
)


print("=============")
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

print("==================")
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
    is_valid('()'),
    is_valid('())'),
    )

print("===============")
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

print("==============")
def base_convert(dec_number: int, base: int) -> str:
    digits = "0123456789ABCDEF"
    remainder_stack = []
    while dec_number > 0:
        rem = dec_number % base
        remainder_stack.append(rem)
        dec_number = dec_number // base

    ans = []
    while remainder_stack:
        ans.append(digits[remainder_stack.pop()])
    return ''.join(ans)

print(base_convert(42, 2))
print(base_convert(42, 16))

print("==================")
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

ls           = ListNode(0)
ls.next      = ListNode(1)
ls.next.next = ListNode(2)
print(ls.next.next.val)


print("====================")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#ls           = ListNode(0)
#ls.next      = ListNode(1)
#ls.next.next = ListNode(2)
#print(ls.next.next.val)

def search_list(L: ListNode, key: int) -> ListNode:
    while L and L.val != key:
        L = L.next
    return L

ls = ListNode(0)
ls.next = ListNode(1)
ls.next.next = ListNode(2)

found = search_list(ls, 2)  
print(found.val)

print("====================")
def insert_after(node: ListNode, new_node: ListNode) -> None:
    new_node.next = node.next
    node.next = new_node

ls = ListNode(0)
ls.next = ListNode(1)
ls.next.next = ListNode(2)

insert_after(ls.next, ListNode(4))
print(
    ls.val,
    ls.next.val,
    ls.next.next.val,
    ls.next.next.next.val,
)





print("=================TREE==============")
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

def insert_left(root: Node, new_node: Node) -> None:
    while root.left: # Traverse the left-half of the tree.
        root = root.left
    root.left = new_node

def insert_right(root: Node, new_node: Node) -> None:
    while root.right: # Traverse the left-half of the tree.
        root = root.left
    root.right = new_node

tree = Node(val = 0, left = Node(1), right = Node(2))
print(tree.val)
print(tree.left.val)
print(tree.right.val)
new_node = Node(val = 4)
insert_left(tree, new_node)

print("---")
print(tree.val)
print(tree.left.val)
print(tree.left.left.val)
print(tree.right.val)

print("====================================")
class Node:
    def __init__(self, val='', left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

def insert_left(root: Node, new_node: Node) -> None:
    while root.left: # Traverse the left-half of the tree.
        root = root.left
    root.left = new_node

def insert_right(root: Node, new_node: Node) -> None:
    while root.right: # Traverse the left-half of the tree.
        root = root.right
    root.right = new_node

def build_parse_tree(expr: str) -> Node:
    '''
    Input: a string for a mathematical expression
    Returns: the root node of the expression parsed
    '''

    # TODO: Make sure to handle spaces
    expr = list(expr)
    tree = Node(val='')
    p_stack = []
    p_stack.append(tree)
    cur_tree = tree

    for char in expr:
        if char == '(':
            insert_left(cur_tree, Node(''))
            p_stack.append(cur_tree)
            cur_tree = cur_tree.left
        elif char not in '+-*/)':
            cur_tree.val = char
            parent = p_stack.pop()
            cur_tree = parent
        elif char in '+-*/':
            cur_tree.val = char
            insert_right(cur_tree, Node(''))
            p_stack.append(cur_tree)
            cur_tree = cur_tree.right
        elif char == ')':
            p_stack.pop()

    return tree



'''
This should build the following tree:

(3+(4*5))

      +
   3    *
      4   5
'''

expression_tree = build_parse_tree("(3+(4*5))")
print(expression_tree.val)
print(expression_tree.left.val)
print(expression_tree.right.val)
print(expression_tree.right.left.val)
print(expression_tree.right.right.val)


print("Tree Traversal ========================")

def preorder(tree: Node) -> None:
    if tree:
        # visit the root node first and do something with it
        # in our case let's print the value of the node
        print(tree.val)

        # then preorder traverse the left sub-tree
        preorder(tree.left)

        # then preorder traverse the right sub-tree
        preorder(tree.right)

    return None

print('preorder')
preorder(expression_tree)


def inorder(tree: Node) -> None:
    if tree:
        # first inorder traverse the left sub-tree
        inorder(tree.left)

        # now let's check the root node after inorder
        # traversing the left sub-tree
        print(tree.val)

        # then inorder traverse the right sub-tree
        inorder(tree.right)

    return None

print("inorder")
inorder(expression_tree)


def postorder(tree: Node) -> Node:
    if tree:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.val)

    return None

print("postorder")
postorder(expression_tree)



print("====================OPTIMIZATION==================")
nums = [0.3, 4, -2]
def cumulative_sum(nums: List[float]) -> List[float]:
    cum_sum = 0
    res = [0] * len(nums)
    for i in range(len(nums)):
        cum_sum += nums[i]
        res[i] = cum_sum
    return res
print(cumulative_sum(nums))

print("--------------")
def prefix_sum(nums: List[float], i: int) -> List[float]:
    cum_sum = 0
    for j in range(len(nums)):
        cum_sum += nums[j]
        if j == i:
            break
    return cum_sum

nums = [0.3, 4, -2]
print(prefix_sum(nums, 1))

print("================GRAPH BFS=====================")
graph = {
    1: [2,3],
    2: [1,3,4,5],
    3: [1,2,5,7,8],
    4: [2,5],
    5: [2,3,4,6],
    6: [5],
    7: [3,8],
    8: [3,7],
}

from collections import defaultdict
def bfs_no_queue(s, graph):
    discovered = set()
    discovered.add(s)
    current_layer = [s]

    while current_layer:
        print(current_layer)
        next_layer = []
        for node in current_layer:
            for next_node in graph[node]:
                if next_node not in discovered:
                    discovered.add(next_node)
                    next_layer.append(next_node)
        current_layer = next_layer

bfs_no_queue(1, graph)















