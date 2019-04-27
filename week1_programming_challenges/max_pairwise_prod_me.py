# Uses python2
from random import randint
#n =int(raw_input())
a = [int(x) for x in raw_input().split()]
#print(len(a))
#a = []
#for i in range(2 * 10 ** 5):
#    a.append(i)
N, M = a[0], a[1]

def max_pairwise_fast(num_list):
    product = 0
    index1 = 0 
    n = len(num_list)

    for i in range(1, n):
        if num_list[i] > num_list[index1]:
            index1 = i

    if index1 == 0:
        index2 = 1
    else:
        index2 = 0 

    for i in range(0, n):
        if (i != index1) and (num_list[i] > num_list[index2]):
            index2 = i

    product = num_list[index1] * num_list[index2]

    return(product)

#print(max_pairwise_fast(a))

def max_pairwise_naive(num_list):
    product = 0
    n = len(num_list)

    for i in range(n):
        for j in range(n):
            if i != j:
                if product < num_list[i] * num_list[j]:
                    product = num_list[i] * num_list[j]
    return(product)

while True:
    n = randint(2, N)
    A = [None] * n
    for i in range(n):
        A[i] = randint(0, M)
    print(A)
    result_one = max_pairwise_naive(A)
    result_two = max_pairwise_fast(A)
    if result_one == result_two:
        print("OK")
    else:
        print("Wrong answer: ", result_one, result_two)
        break
