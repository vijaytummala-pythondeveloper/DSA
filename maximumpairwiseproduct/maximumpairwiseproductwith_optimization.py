# n = int(input("enter numbers count : "))
# numbers = input("enter numbers seprated with space : ")
# numbers_list = []
# for i in numbers.split(" "):
#     numbers_list.append(int(i))
# print(numbers_list)
import time

numbers_list = [i for i in range(1,10000)]
begin = time.time()
bignum = 0
for i in numbers_list:
    if i > bignum:
        bignum = i

secondbig = 0
for i in numbers_list:
    if i != bignum and i > secondbig:
        secondbig = i

print(bignum * secondbig)
end = time.time()
print(end - begin)
