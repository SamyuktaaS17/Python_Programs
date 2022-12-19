#ATM Machine CodeChef
T=int(input())
for x in range(T):
    inp=input()
    userInput=inp.split(" ")
    #splitting the number of people and total units of cash
    N=int(userInput[0])
    K=int(userInput[1])
    A=[]
    B=[]
    people=input()
    A=people.split(" ")
    for y in range(N):
        p=int(A[y])
        #checking whether given amount is available for transaction
        if p<=K:
            B.append("1")
            K=K-p
        else:
            B.append("0")
 
    s=""        
    C=s.join(B)
    print(C)
     
        