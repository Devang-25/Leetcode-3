"""
Question:

arr1 = [1, 2, 4, 8]
arr2 = [2, 8, 9]

return [2, 8]
"""

# build a iterator-like object
class myIter:
    def __init__(self, arr):
        self.arr = arr
        self.i = 0

    def has_next(self):
        return self.i < len(self.arr)
        # if self.i < len(self.arr):
        #     return True
        # return False

    def next(self):
        """
        when object.next() is called,
        return the next ele in the iterable
        if no next: raise Error (that is the behavior of iterable)
        """
        cur = self.arr[self.i]
        self.i += 1
        return cur


#######################

arr1 = [1, 2, 4, 8]
object1 = myIter(arr1)
results = []
while object1.has_next():
  results.append(object1.next())
print(results)
print(bool(results == [1, 2, 4, 8]))


########################
# build a CommonElement class that has 1) next and has_next fuction for iterators

class commonElement:
  def __init__(self, arr1, arr2):
    """
    input: 2 list or array, turn them into interator using class myInter
    """
    self.arr1 = myIter(arr1)
    self.arr2 = myIter(arr2)

    # self.arr1 and self.arr2 has behaviro of an iterators
    # call its next value by arr.next()
    self.v1 = self.arr1.next()
    self.v2 = self.arr2.next()

    # keep track of the next_common_ele
    self.next_common_ele = self._find_next()

  def _find_next(self):
    while self.v1 is not None and self.v2 is not None:
      if self.v1 == self.v2:
        cur = self.v1
        self.v1 = self.arr1.next() if self.arr1.has_next() else None
        self.v2 = self.arr2.next() if self.arr2.has_next() else None
        return cur
      elif self.v1 > self.v2:
        self.v2 = self.arr2.next() if self.arr2.has_next() else None
      else: # self.v1 < self.v2:
        self.v1 = self.arr1.next() if self.arr1.has_next() else None

  def next(self):
    """
    return the next ele if has
    raise error message if not (behavior of iterable)
    """
    if self.next_common_ele is None:
      raise Exception("Iterator has reached the end")

    cur = self.next_common_ele
    self.next_common_ele = self._find_next()
    return cur


  def has_next(self):
    # return bool(self.next_common_ele != None)
    return self.next_common_ele is not None

########################

arr1 = [1, 2, 4, 8]
arr2 = [2, 8, 9]
object2 = commonElement(arr1, arr2)
print("1", object2.next())
print("2", object2.has_next())
print("3", object2.has_next())
print("4", object2.next())
print("5", object2.has_next())
print("6", object2.next())

########################
