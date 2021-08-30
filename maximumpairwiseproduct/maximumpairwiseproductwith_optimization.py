n = int(input("enter numbers count : "))
numbers = input("enter numbers seprated with space : ")
numbers_list = []
for i in numbers.split(" "):
    numbers_list.append(int(i))
print(numbers_list)
import time

# numbers_list = [i for i in range(1,10000)]
begin = time.time()
bignum_index = 0
for i in range(0,len(numbers_list)):
    if numbers_list[i] > numbers_list[bignum_index]:
        bignum_index = i

secondbig = 0
secondbig_index = 0
for i in range(0,len(numbers_list)):
    if i != bignum_index and numbers_list[i] >= secondbig:
        secondbig_index = i
        secondbig = numbers_list[i]

print(numbers_list[bignum_index] * numbers_list[secondbig_index])
end = time.time()
print(end - begin)
