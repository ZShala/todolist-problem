def solution():
    N=int(input("Enter the length of array:"))
    A=list(map(int, input("Enter the numbers to test:").split()))

    count=0
    for i in range(N):
        if A[i] >= 1000:
            count +=1

    print(count)

T=int(input("Enter the number of test cases:"))
while(T>0):
    T=T-1
    solution()
