nums = [1,2,3,4,5]
names = ["Hammad","Ali","Ahmed"]

# empty = []


# characters = list("Hammad")

# numbers = list((10,20,30))

# print(nums)
# print(names)
# print(characters)
# print(numbers)

# numbers = list(range(1,6))
# print(numbers)

# print(list(range(1,10,2)))

# reversed_list = numbers[::-1]
# print(reversed_list)
# numbers.reverse()
# print(numbers)

# print(nums)
# nums.remove(5)
# print(nums)

# removed = nums.pop()
# print(removed)
# nums.pop(0)
# print(nums)

# del nums[1]
# print(nums)

# nums.clear()
# print(nums)

# students = [
#     {"name": "Ali", "marks": 85},
#     {"name": "Ahmed", "marks": 92},
#     {"name": "Sara", "marks": 78}
# ]
# sorted_student = sorted(
#     students,
#     key=lambda student:student["marks"]
# )
# for student in sorted_student:
#     print(student)

# students.sort(key=lambda student:student["marks"])
# for student in students:
#     print(student)


# squares = []

# for number in nums:
#     squares.append(number ** 2)

# print(squares)

# squares2 = [number ** 3 for number in nums]
# print(squares2)

# numbers = [1,2,3,4,5,6,7,8,9,10]

# even_numbers = [
#     number
#     for number in numbers
#     if number % 2 == 0
# ]
# print(even_numbers)

# labels = [
#     "Even" if n%2 == 0 else "Odd"
#     for n in numbers
# ]
# print(labels)

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# flattened = [
#     number
#     for row in matrix
#     for number in row
# ]
# print(flattened)

# samples = list(range(1,101))

# batch_size = 10

# for i in range(0,len(samples),batch_size):
#     batch = samples[i:i+batch_size]
#     print(batch)


def find_largest(nums):
    largest = float("-inf")

    for num in nums:
        if num > largest:
            largest = num

def find_smallest(nums):
    smallest = float("inf")

    for num in nums:
        if num < smallest:
            smallest = num

def calculate_sum_and_average(nums):
    sum = 0
    average= 0.0

    for num in nums:
        sum += num

    print(f"Sum is {sum} \n Average is{sum/len(nums)}")

def count_even_and_odd(nums):
    even_counter = 0
    odd_counter = 0

    for num in nums:
        if num % 2 == 0:
            even_counter +=1
        else:
            odd_counter +=1

    print(f"Even count: {even_counter} \n Odd count: {odd_counter}")

def reverse_list(nums):

    left = 0
    right = len(nums)-1
    while left < right:
        nums[left],nums[right] = nums[right],nums[left]


    return nums

def remove_duplicates(nums):

    seen = set()
    unique_list=[]
    print("received: ",nums)
    for num in nums:
        if num not in seen:
            seen.add(num)
            unique_list.append(num)
        
        
            
    print("removed duplicates: ",unique_list)

    return nums
            
def common_elements(list1,list2):
    common = []

    for i in range(len(list1)):
        for j in range(i,len(list2)):

            if list1[i] == list2[j]:
                common.append(list1[i])

    print(common)

    return common


def find_elements(nums):
    pass

def move_all_zeros(nums):

    write = 0
    zero_counter = 0
    
    for num in nums:
        if num != 0:
            nums[write] = num
            write +=1
        else:
            zero_counter +=1
    while zero_counter > 0:
        nums[write] = 0
        zero_counter -=1
        write +=1

    print(nums)
    return nums
n = [1,2,3,0,5,0]
# move_all_zeros(n)


    
nums = [1,1,2,3,4,5,5,5]
nums2 = [1,3,6,7]

def find_frequencies(nums):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num,0) +1

    print(freq)
    return freq



        

find_frequencies(nums)


# remove_duplicates(nums)
# common_elements(nums,nums2)