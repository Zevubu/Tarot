#The current up to date version as it stands.
#3 card draw. Ask a question turns question into list of numbers.
#Runs algerithum to choose card between 1 and 26, 3 times, out of 3 randomly choosen lists
#This is one of my first programs. I built almost all peices in it from scratch, trile and eror.
#using sololearn and google as a guide when I got stuck.
#The current up to date version as it stands. Including some notes on process and function.


#Ask a question
quest=input()
max_index=len(quest)-1
counter=0

cat=[]  

print (quest)
#turns question into list of numbers

while counter<=max_index:
    bat=quest[counter]
    if bat=='a':
        art=1
    elif bat=='b':
        art=2
    elif bat=='c' :
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

# Takes list of numbers and deletes interigers. 
# IE what where when why so on. leaveing only the more varied portion of code    
tom=len(cat)
count=0
til=0
kit=cat[0]

while tom>=til:
    if (tom>=5 and cat[0]==23 and cat[1]==8 and cat[2]==5 and cat[3]==14 and cat[4]==0):
        while count<=4:
            cat.remove(cat[0])
            count=count+1  
    elif tom>=6 and cat[0]==23 and cat[1]==8 and cat[2]==5 and cat[3]==18 and cat[4]==5 and cat[5]==0:
        while count<=5:
            cat.remove(cat[0])
            count=count+1    
    elif tom>=6 and cat[0]==23 and cat[1]==8 and cat[2]==9 and cat[3]==12 and cat[4]==5 and cat[5]==0:
        while count<=5:
            cat.remove(cat[0])
            count=count+1   
    elif tom>=4 and cat[0]==23 and cat[1]==8 and cat[2]==25 and cat[3]==0:
        while count<=3:
            cat.remove(cat[0])
            count=count+1    
    elif tom>=5 and cat[0]==23 and cat[1]==8 and cat[2]==1 and cat[3]==20 and cat[4]==0:
        while count<=4:
            cat.remove(cat[0])
            count=count+1                 
    elif tom>=6 and cat[0]==23 and cat[1]==15 and cat[2]==21 and cat[3]==12 and cat[4]==4 and cat[5]==0:
        while count<=5:
            cat.remove(cat[0])
            count=count+1
    elif tom>=5 and cat[0]==23 and cat[1]==9 and cat[2]==12 and cat[3]==12 and cat[4]==0:
        while count<=4:
            cat.remove(cat[0])
            count=count+1
    elif tom>=7 and cat[0]==19 and cat[1]==8 and cat[2]==15 and cat[3]==21 and cat[4]==12 and cat[5]==4 and cat[6]==0:
        while count<=6:
            cat.remove(cat[0])
            count=count+1
    elif tom>=3 and cat[0]==9 and cat[1]==6 and cat[2]==0:
        while count<=2:
            cat.remove(cat[0])
            count=count+1 
    elif tom>=3 and cat[0]==9 and cat[1]==19 and cat[2]==0:
        while count<=2:
            cat.remove(cat[0])
            count=count+1   
    elif tom>=4 and cat[0]==3 and cat[1]==1 and cat[2]==14 and cat[3]==0:
        while count<=3:
            cat.remove(cat[0])
            count=count+1 
    elif tom>=6 and cat[0]==3 and cat[1]==15 and cat[2]==21 and cat[3]==12 and cat[4]==4 and cat[5]==0:
        while count<=5:
            cat.remove(cat[0])
            count=count+1    
    elif tom>=3 and cat[0]==4 and cat[1]==15 and cat[2]==0:
        while count<=2:
            cat.remove(cat[0])
            count=count+1       
    elif tom>=2 and cat[0]==9 and cat[1]==0:
        while count<=1:
            cat.remove(cat[0])   
            count=count+1
    elif tom>=4 and cat[0]==1 and cat[1]==18 and cat[2]==5 and cat[3]==0:
        while count<=3:
            cat.remove(cat[0])
            count=count+1   
    elif tom>=5 and cat[0]==23 and cat[1]==1 and cat[2]==14 and cat[3]==20 and cat[4]==0:
        while count<=4:
            cat.remove(cat[0]) 
            count=count+1  
    elif tom>=5 and cat[0]==23 and cat[1]==9 and cat[2]==19 and cat[3]==8 and cat[4]==0:
        while count<=4:
            cat.remove(cat[0]) 
            count=count+1   
    elif tom>=4 and cat[0]==23 and cat[1]==8 and cat[2]==15 and cat[3]==0:
        while count<=3:
            cat.remove(cat[0]) 
            count=count+1
    elif tom>=4 and cat[0]==8 and cat[1]==15 and cat[2]==23 and cat[3]==0:
        while count<=3:
            cat.remove(cat[0]) 
            count=count+1  
    elif tom>=6 and cat[0]==23 and cat[1]==8 and cat[2]==9 and cat[3]==3 and cat[4]==8 and cat[5]==0:
        while count<=5:
            cat.remove(cat[0])
            count=count+1
    elif tom>=6 and cat[0]==3 and cat[1]==1 and cat[2]==14 and cat[3]==1 and cat[4]==20 and cat[5]==0:
        while count<=5:
            cat.remove(cat[0])
            count=count+1  
    elif tom>=5 and cat[0]==3 and cat[1]==1 and cat[2]==14 and cat[3]==20 and cat[4]==0:
        while count<=4:
            cat.remove(cat[0])
            count=count+1  
    elif tom>=3 and cat[0]==1 and cat[1]==13 and cat[2]==0:
        while count<=2:
            cat.remove(cat[0])   
            count=count+1    
    til=til+1
    count=0                                                     
#done:when where while why what would will if is can should could do are want wish who how which can't cant am

#to add:

   
#Takes Remaining numbers on cat and add them into one number ie hat.  

catindex=len(cat)-1
count=0
hat=(0) 

while count<=catindex:
    hat=hat+cat[count]
    count=count+1

 

#it produces 3 distinct random numbers. 
#This is one of the few section I looked up I copied and tweeked it to fit my needs.
import random

cut=[]
bil=2
bui=0

while bui<=bil:
    x=random.randint(0,23)
    if x not in cut:
        bui=bui+1
        cut.append(x)

#adds random nuber ons to hat creating three new distinct numbers.      
thing1=cut[0] 
thing2=cut[1]
thing3=cut[2]

tus=hat+thing1
tut=hat+thing2
tun=hat+thing3

# Divides the 3 numb by 26 leaving the remainder. which by nature will be 0-25.
if tus>=26:
    tus=tus % 26
   
#print(tus)

if tut>=26:
    tut=tut % 26
   
#print (tut)
   
if tun>=26:
    tun=tun % 26
   
#print(tun)

#It took me longer then I care to admit to figure out...
#that the quickest way to reduce my my number to less then 26...
#was just to divide them by 26 and go with the remainder.
#25==26 26==0

#cat== digets catindex== numberofdigets hat==total of all digets added thing1,2&3 == random diget between 2&11 tus,tut,tun==hat+thing %26

#print(cat)
#print(catindex)
#print(hat)
#print(cut)   
#print(thing1)
#print(tus)
#print(thing2)
#print(tut)
#print(thing3)
#print(tun)

import random

tarot=('The Fool','I The Magician','II High Priestess','III The Empress','IIII The Emperor','V The High Priest','VI The Lovers','VII The Chariot','VIII Justice','VIIII The Hermit','X The Wheel of Fortune','XI Strength','XII The Hanged Man','XIII The Nameless Card','XIIII temperance','XV The Devil','XVI The Tower','XVII The Star','XVIII The Moon','XVIIII The Sun','XX Judgement','XXI The World','Ace of Pentacles','II of Pentacles','III of Pentacles','IIII of Pentacles','V of Pentacles','VI of Pentacles','VII Pentacles','VIII of Pentacles','VIIII of Pentacles','X of Pentacles','Page of Pentacles','Queen of Pentacles','King of Pentacles','Knight of Pentacles','Ace of Wands','II of Wands','III of Wands','IIII of Wands','V of Wands','VI of Wands','VII of Wands','VIII of Wands','VIIII of Wands','X of Wands','Page of Wands','Queen of Wands','King of Wands','Knight of Wands','Ace of Swords','II of Swords','III of Swords','IIII of Swords','V of Swords','VI of Swords','VII of Swords','VIII of Swords','VIIII of Swords','X of Swords','Page of Swords','Queen of Swords','King of Swords','Knight of Swords','Ace of Cups','II of Cups','III of Cups','IIII of Cups','V of Cups','VI of Cups','VII of Cups','VIII of Cups','VIIII of Cups','X of Cups','Page of Cups','Queen of Cups','King of Cups','Knight of Cups')
tcou=len(tarot)

(tcou)

cut=[]
bui=0
tarot0=[]
tarot10=[]
tarot21=[]
a=tarot0

#Shuffles the 78 card into 3 list of 26.
while bui<=25:
    x=random.randint(0,77)
    if x not in cut:   
        cut.append(x)
        a.append(tarot[x]) 
        if bui>=25 and a==tarot0:
            #print("tarot0 check")
            bui=0
            a=tarot10
        elif bui>=25 and a==tarot10:
            #print("tarot10 check")
            bui=0
            a=tarot21 
        elif bui>=25 and a==tarot21:
            #print("tarot21 check")
            bui=26
        else:
            bui=bui+1   
      
               

t0=len(tarot0)
t10=len(tarot10)
t21=len(tarot21) 
#cl=len(cut)
#print(cut)
#print(cl)

#print (tarot0)
#print (t0)
#print (tarot10)
#print (t10)
#print (tarot21)
#print (t21)

#Determins which deck will be pulled from. 
import random

def ran(y,z):
    for i in range(3):
        x=random.randint(y,z)
        return(x)

sect1=ran(1,3)
sect2=ran(1,3)
sect3=ran(1,3)

catch=sect1,sect2,sect3

#print(catch)

if sect1==1:
    deck1=tarot0
elif sect1==2:
    deck1=tarot10
elif sect1==3:
    deck1=tarot21
   
if sect2==1:
    deck2=tarot0
elif sect2==2:
    deck2=tarot10
elif sect2==3:
    deck2=tarot21
   
if sect3==1:
    deck3=tarot0
elif sect3==2:
    deck3=tarot10
elif sect3==3:
    deck3=tarot21

# finaly what cards will be shown, and in what order
card1=deck1[tus]

print (card1)

card2=deck2[tut]
        
print (card2)

card3=deck3[tun]
        
print (card3)

#still to be added: 
# Reverse cards, 
# larger or small draw ie number of cards shown, 
# save draws for reexamining, 
# card definitions
# english to hebrew translation with kabolic reading. 
# Pictures and genoral front end.


 

#print (t0)
#print (t10)
#print (t21)

