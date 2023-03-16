dominant={'A':11,'K':4,'Q':3,'J':20,'T':10,'9':14,'8':0,'7':0}
notDominant={'A':11,'K':4,'Q':3,'J':2,'T':10,'9':0,'8':0,'7':0}
a=input("Enter number of hands and suit: ")
b=[y for y in a]
d=int(b[0])
sum=0
for i in range(4*d):
    hand=input()
    c=[x for x in hand]
    card=c[0]
    if c[1]== b[1]:
        sum=sum + dominant[card]
    else:
        sum=sum + notDominant[card]
print(sum)