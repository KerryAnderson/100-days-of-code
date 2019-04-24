#Day 7: Code Challenge (Loops)
#Test 1
def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count
  
print(divisible_by_ten([20, 25, 30, 35, 40]))

#Test 2
def add_greetings(names):
  greetings = []
  for name in names:
    greetings.append("Hello, " + name)
  return greetings

print(add_greetings(["Owen", "Max", "Sophie"]))

#Test 3
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

#Test 4

def odd_indices(lst):
  new_lst = []
  for index in range(1, len(lst), 2):
    new_lst.append(lst[index])
  return new_lst

print(odd_indices([4, 3, 7, 10, 11, -2]))

#Test 5
def exponents(bases, powers):
  new_lst = []
  for base in bases:
    for power in powers:
      new_lst.append(base ** power)
  return new_lst

#Test 6
print(exponents([2, 3, 4], [1, 2, 3]))

def larger_sum(lst1, lst2):
  if sum(lst1) > sum(lst2):
    return lst1
  elif sum(lst2) > sum(lst1):
    return lst2
  else:
    return lst1

print(larger_sum([1, 9, 5], [2, 3, 7]))

#Test 7
def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum

print(over_nine_thousand([8000, 900, 120, 5000]))

#Test 8
def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum

print(max_num([50, -10, 0, 75, 20]))

#Test 9
def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

#Test 10
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

