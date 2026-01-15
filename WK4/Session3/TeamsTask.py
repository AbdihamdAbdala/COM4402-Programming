# Task 1
nums = [3, 6, 9, 12]
#print(nums[0])
#print(nums[len(nums) - 1])

# Task 2
colors = ["orange", "green", "blue"]
colors.append("yellow")

# Task 3
fruits = ["apple","banana","cherry"]
fruits[1] = "orange"

# Task 4
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
list3 = []

for i in range(len(list1)):
    list3.append(list1[i])

for i in range(len(list2)):
    list3.append(list2[i])

list3.pop(1)
list3.pop(1)
list3.pop(1)

list3.insert(1, 99)
list3.insert(2, 100)

for i in range(len(list3)):
    list3[i] = list3[i] * 2

print(list3)