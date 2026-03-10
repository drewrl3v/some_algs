# Basics


Let's consider the grade school strategy for multiply two many-digit numbers.
The key here is that we're only allowed to use multiply for single digit numbers.



<details>
<summary>Solution</summary>

## Grade School Multiplication

<pre><code class="language-python">

# TODO: Just my scratch work, all needs to be cleaned and corrected later.
'''                                                                          
Actually just precompute a multiplicaiton table                              
'''                                                                          
def multiply(x: int, y: int) -> int:                                         
  '''                                                                        
  For simplicity we keep them positive                                       
  '''                                                                        
  #if  x > 10 or y > 10:                                                     
  #  raise ValueError("Too large of an input")                               
  res = 0                                                                    
  for _ in range(y):                                                         
    res += x                                                                 
  return res                                                                 
                                                                             
print(multiply(3, 4))                                                        
print(multiply(10, 0))                                                       
print(multiply(0,5))                                                         
print(multiply(1,2))                                                         
                                                                             
def expoentiate(num: int, power: int) -> int:                                
  '''                                                                        
  Only takes integer values, and require power >= 0                          
  '''                                                                        
  res = 1                                                                    
  for _ in range(power):                                                     
    res = multiply(res, num)                                                 
  return res                                                                 
                                                                             
print(expoentiate(3,2))                                                      
print(expoentiate(1,8))                                                      
                                                                             
def listify_integer(num: int):                                               
  res = []                                                                   
  remainder = num % 10                                                       
  while num != 0:                                                            
    remainder = num % 10                                                     
    res.append(remainder)                                                    
    num = num // 10                                                          
  return reversed(res)                                                       
                                                                             
                                                                             
def many_digit_multiply(x: List[int], y: List[int]) -> List[int]:            
  res = 0                                                                    
  for i, num1 in enumerate(reversed(y)):                                     
    basei = expoentiate(10, i)                                               
    summand = 0                                                              
    for j, num2 in enumerate(reversed(x)):                                   
      basej = expoentiate(10, j)                                             
      summand += multiply(multiply(num2, num1), basej)                       
      #summand += many_digit_multiply(many_digit_multiply(num2, num1), basej)
      #lnum1  = listify_integer(num1)                                        
      #lnum2  = listify_integer(num2)                                        
      #lbasej = listify_integer(basej)                                       
      #ltmp   = many_digit_multiply(lnum2, lnum1)                            
      #summand += many_digit_multiply(ltmp, lbasej)                          
    summand = multiply(summand, basei)                                       
    #summand = many_digit_multiply(summand, basei)                           
    #lsummand = listify_integer(summand)                                     
    #lbasei   = listify_integer(basei)                                       
    #summand = many_digit_multiply(lsummand, lbasei)                         
                                                                             
    res += summand                                                           
  return res                                                                 
</code></pre>
</details>


## Longest Consecutive Sqeuence

Given an array `nums`, return the length of the longest consecutive sequence of elements that can be formed.

<details>

<pre><code class="language-python">

def longest_consecutive(nums: List[int]) -> int:
    '''
    Naive sorting solution.
    '''
    if not nums: return 0
    nums = sorted(list(set(nums)))
    res_max = 1
    cur_max = 1
    i, j = 0, 1
    while j != len(nums):
        if nums[i] + 1 == nums[j]:
            cur_max += 1
            res_max = max(res_max, cur_max)
            i += 1
            j += 1
        else:
            cur_max = 1
            i += 1
            j += 1
    return res_max
</code></pre>
</details>


