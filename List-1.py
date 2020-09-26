#first_last6
#Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
#first_last6([1, 2, 6]) → True
#first_last6([6, 1, 2, 3]) → True
#first_last6([13, 6, 1, 2, 3]) → False
def first_last6(nums):
  if nums[0] ==6 or nums[-1] ==6:
    return True
  else:
    return False
  
#same_first_last
#Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
#same_first_last([1, 2, 3]) → False
#same_first_last([1, 2, 3, 1]) → True
#same_first_last([1, 2, 1]) → True
def same_first_last(nums):
  if len(nums) >= 1:
    if nums[0] == nums[-1]:
      return True
    else:
      return False
  else:
    return False
