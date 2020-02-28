"""
arr = [-8,0,2,5]

# middle = 3/2 = #1
  #1 == 0

# middle = (2+3)/2 = #2
    #2 == 2


arr = [-1,0,3,6]

- middle = (0+3)/2 = 1
 #1 = 0
 since value  (0) is smaller than index(1) --> right


[0, 2, 3, 5]

- middle = #1
  #1 is 2
  since the value(2) is bigger than the index(1):
  so I go to left

- middle = 0+0 /2 = 0
  #0 == 0
  since 0 == 0. I found my target

  as long as the value is NOT smaller than the index ---> I should keep go into the left side to check
  if there is a better answer with lower index


不存在的情况：
（1）
假设 位置#2 = 3， 位置#4有可能等于4吗？
不肯能。
所以：if value > index, then answer is impossible at the right side.
"""

def index_equals_value_search(arr):
  """
  input type: arr
  output index: int
  """

  target_index = -1

  start = 0
  end = len(arr) - 1


  while start <= end:
    middle = (start + end) // 2
    print("middle", middle)

  # I found an ppossible answer
    if arr[middle] == middle:
      if target_index == -1:
        target_index = middle
        print("1 target index", target_index)
      elif middle < target_index:
        target_index = middle
        print("2 target index", target_index)

      # value = arr[middle]
      # go to left side see if better answer exist
      while arr[middle] >= middle:
        if start < end:
            """
            Cautious: this line might went into infinite loop.
            1)
            - Start only be EQUAL to end.
            - start cannot <= start: this might goes into infinite loop

            2)
            - can only is IF statement
            - NOT WHERE statement, this cause cause inifite loop
            """
            end = middle - 1
            print("1)start:{}, end{}".format(start, end))
        else:
            break

    else:
      if arr[middle] > middle:
        # go to the left
        end = middle - 1
        print("2)start:{}, end{}".format(start, end))

      elif arr[middle] < middle:
        # go to right
        start = middle + 1
        print("3)start:{}, end{}".format(start, end))

  return target_index

arr1 = [-8,0,2,5]
arr2 = [-1,1,2,5]
print("target index", index_equals_value_search(arr2))
