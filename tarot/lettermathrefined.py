#Ask a question
quest=input()
max_index=len(quest)-1
counter=0

cat=[]  

print (quest)

while counter<=max_index:
    bat=quest[counter]
    if bat=='a'or'A' or '1' or '!':
        art=1
    elif bat=='b'or'B' or '2':
        art=2
    elif bat=='c'or'C' or '3':
        art=3
    elif bat=='d':
        art=4
    elif bat=='e':
        art=5
    elif bat=='f':
        art=6
    elif bat=='g':
        art=7
    elif bat=='h':
        art=8
    elif bat=='i':
        art=9
    elif bat=='j':
        art=10
    elif bat=='k':
         art=11
    elif bat=='l':
        art=12
    elif bat=='m':
        art=13
    elif bat=='n':
        art=14
    elif bat=='o':
        art=15
    elif bat=='p':
        art=16
    elif bat=='q':
        art=17
    elif bat=='r':
        art=18
    elif bat=='s':
        art=19
    elif bat=='t':
        art=20
    elif bat=='u':
        art=21
    elif bat=='v':
        art=22
    elif bat=='w':
        art=23
    elif bat=='x':
        art=24
    elif bat=='y':
        art=25
    elif bat=='z':
        art=26
    elif bat=='A':
        art=1
    elif bat=='B':
        art=2
    elif bat=='C':
        art=3
    elif bat=='D':
        art=4
    elif bat=='E':
        art=5
    elif bat=='F':
        art=6
    elif bat=='G':
        art=7
    elif bat=='H':
        art=8
    elif bat=='I':
        art=9
    elif bat=='J':
        art=10
    elif bat=='K':
        art=11
    elif bat=='L':
        art=12
    elif bat=='M':
        art=13
    elif bat=='N':
        art=14
    elif bat=='O':
        art=15
    elif bat=='P':
        art=16
    elif bat=='Q':
        art=17
    elif bat=='R':
        art=18
    elif bat=='S':
        art=19
    elif bat=='T':
        art=20
    elif bat=='U':
        art=21
    elif bat=='V':
        art=22
    elif bat=='W':
        art=23
    elif bat=='X':
        art=24
    elif bat=='Y':
        art=25
    elif bat=='Z':
        art=26
    elif bat=='1':
        art=1
    elif bat=='2':
        art=2
    elif bat=='3' :
        art=3
    elif bat=='4':
        art=4
    elif bat=='5':
        art=5
    elif bat=='6':
        art=6
    elif bat=='7':
        art=7
    elif bat=='8':
        art=8
    elif bat=='9':
        art=9
    elif bat=='10':
        art=10 
    elif bat=='?':
        art=23 
    elif bat=='\'':
        art=1  
    else:
        art=0
    cat.append(art)
    counter=counter+1

print (cat)