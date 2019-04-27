# Uses python2
n =int(raw_input())
a = [int(x) for x in raw_input().split()]

def max_pairwise_fast(num_list):
    product = 0
    index = 0 
    n = len(num_list)

    for i in range(1, n):
        if num_list[i] > num_list[index]:
            index = i

    temp = num_list[n - 1]
    num_list[n - 1] = num_list[index]
    num_list[index] = temp 
    
    index = 0
    for i in range(0, n - 1):
        if (num_list[i] > num_list[index]):
            index = i

    temp = num_list[n - 2]
    num_list[n - 2] = num_list[index]
    num_list[index] = temp

    return(num_list[n - 2] * num_list[n - 1])

print(max_pairwise_fast(a))
