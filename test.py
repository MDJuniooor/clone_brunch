def is_prime(n):
    return all([(n % j) for j in range(2, int(n**0.5)+1)]) and n > 1

def solution(a, b):
    primelist = [is_prime(x) for x in range(100100)]
    solutionlist = [False for x in range(100001)]
    cnt=0
    for i in range(1,100001):
        if not primelist[i]:
            cnt = cnt+1
        else:
            cnt = 0
        if cnt >= 10:
            solutionlist[i] = True
    solution =0
    for i in range(a,b+1):
        if solutionlist[i]:
            solution = solution+1
    print(solution)
    # for i in range(a,b+1):
    #     check = True
    #     for j in range(i-10,i+11):
    #         if primelist[j]:
    #             check=False
    #             break
    #     if check:
    #         solutionlist.append(j)
    # print(len(set(solutionlist)))
    # return len(set(solutionlist))


solution(a=97001,
         b=97691)
