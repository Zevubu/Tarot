hat=int(input())

print(hat)

import random

cut=[]
bil=2
bui=0

while bui<=bil:
     x=random.randint(0,10)
     if x not in cut:
       bui=bui+1
       cut.append(x)
     
print(cut)        
      
thing1=cut[0] 
thing2=cut[1]
thing3=cut[2]

tus=hat+thing1
tut=hat+thing2
tun=hat+thing3

if tus>=26:
   tus=tus % 26
   
print(tus)

if tut>=26:
   tut=tut % 26
   
print (tut)
   
if tun>=26:
   tun=tun % 26
   
print(tun)
   