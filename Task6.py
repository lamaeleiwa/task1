#Q1
lst = [30, 75, 9, 97, 50, -4, 70, 59]
largest_num = lst[0]
smallest_num = lst[0]
for num in lst:
    if num > largest_num:
        largest_num = num
    if num<smallest_num:
        smallest_num=num
lst.remove(smallest_num)
print("The largest number is:", largest_num)
print("List after removing the smallest number:", lst)
lst.sort()
print(f'The list after rerange in ascending',lst)
print(f'the last 4 numbers in the list',lst[:-5:-1])

 #Q2
main_lst = [["python", 3], [5, 7.8], ["python", 11], ["python",1]]
count = 0
x='python'
for i in range(len(main_lst)):
        if x in main_lst[i]:
            count+= 1
print(f'the number how python write',count)

#Q3
my_lst = ["I", "LOvE", "GAZa", "sKy", "GEEks"]
lst= ""
for word in my_lst:
   lst+= word + " "

list= lst.rstrip()
print(list)

#Q4
my_lst = [12, 3.8, "GSG", ["sKy", "zak"]]
copied_lst=my_lst[:len(my_lst)]
print(f'The copied list is :',copied_lst)

#Q5
my_lst = ["GSG", "zakaria", 19, 9.8, "Omar"]
my_lst[2], my_lst[4] = my_lst[4], my_lst[2]
print(my_lst)

#Q6
nums = [33, 5.9, 6, -43, 9, 7, 39, 0, -40]
sum = 0
for num in nums:
    sum+= num

print("The sum of the numbers is:", sum)

#Q7
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple2 = tuple1 + (9,)

print(tuple2)

#Q8
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple2 = ('Java', 'C++', 7.8)
new_tuple = tuple1 + tuple2
print(new_tuple)
