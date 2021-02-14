#!/bin/python3

# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    answer = list()
    last_answer = 0
    arr = list()
    for i in range(n):
        arr.append(list())
    for q in queries:
        idx = (q[1] ^ last_answer) % n
        if q[0] == 1:  # write
            arr[idx].append(q[2])
        else:  # query
            current = arr[idx][q[2] % len(arr[idx])]
            answer.append(current)
            last_answer = current
    return answer


if __name__ == '__main__':
    fptr = open('./hacker-rank-dynamic-array.txt', 'r')

    first_multiple_input = fptr.readline().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []
    for _ in range(q):
        queries.append(list(map(int, fptr.readline().rstrip().split())))

    result = dynamicArray(n, queries)

    print(result)

    fptr.close()
