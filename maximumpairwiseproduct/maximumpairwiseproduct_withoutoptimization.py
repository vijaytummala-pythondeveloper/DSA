import time




# n = int(input("enter numbers count : "))
# numbers = input("enter numbers seprated with space : ")
numbers_list = [i for i in range(1,2000)]
# for i in numbers.split(" "):
#     numbers_list.append(int(i))

begin = time.time()
res = 0
for i in range(0,len(numbers_list)):
    for j in range(1,len(numbers_list)):
        if i != j:
            if (numbers_list[i] * numbers_list[j] > res):
                res = numbers_list[i] * numbers_list[j]

print(res)

end = time.time()

print(end - begin)