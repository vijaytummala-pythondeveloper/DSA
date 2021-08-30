import random
def max_pairwise_product_fast(numbers_list):
    bignum = 0
    for i in numbers_list:
        if i > bignum:
            bignum = i
    secondbig = 0
    for i in numbers_list:
        if i != bignum and i > secondbig:
            secondbig = i

    return bignum * secondbig


def max_pairwise_product(numbers_list):
    res = 0
    for i in range(0, len(numbers_list)):
        for j in range(1, len(numbers_list)):
            if i != j:
                if (numbers_list[i] * numbers_list[j] > res):
                    res = numbers_list[i] * numbers_list[j]
    return res


result = 0
fast = 0
count = 0
while True:
    if __name__ == '__main__':
        n = (random.randint(2, 11))
        a = list(random.randint(0, 99999) for r in range(n))
        assert (len(a) == n)
        result = max_pairwise_product(a)

        fast=max_pairwise_product_fast(a)
        count = count+1
        if fast != result:
            print("not ok")
            break
        else:
            print(fast, result, "OK",count)
