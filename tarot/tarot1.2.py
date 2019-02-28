zero=('The Fool')
a=('I The Magician')
b=('II High Priestess')
c=('III The Empress')
d=('IIII The Emperor')
e=('V The High Priest')
f=('VI The Lovers')
g=('VII The Chariot')
h=('VIII Justice')
i=('VIIII The Hermit')
j=('X The Wheel of Fortune')
k=('XI Strength')
l=('XII The Hanged Man')
m=('XIII The Nameless Card')
o=('XIIII temperance')
p=('XV The Devil')
q=('XVI The Tower')
r=('XVII The Star')
s=('XVIII The Moon')
t=('XVIIII The Sun')
u=('XX Judgement')
v=('XXI The World')
aa=('Ace of Pentacles')
bb=('II of Pentacles' )
cc=('III of Pentacles')
dd=('IIII of Pentacles')
ee=('V of Pentacles')
ff=('VI of Pentacles')
gg=('VII Pentacles')
hh=('VIII of Pentacles')
ii=('VIIII of Pentacles')
jj=('X of Pentacles')
kk=('Page of Pentacles')
ll=('Queen of Pentacles')
mm=('King of Pentacles')
nn=('Knight of Pentacles')
aaa=('Ace of Wands')
bbb=('II of Wands')
ccc=('III of Wands')
ddd=('IIII of Wands')
eee=('V of Wands')
fff=('VI of Wands')
ggg=('VII of Wands')
hhh=('VIII of Wands')
iii=('VIIII of Wands')
jjj=('X of Wands')
kkk=('Page of Wands')
lll=('Queen of Wands')
mmm=('King of Wands')
nnn=('Knight of Wands')
aaaa=('Ace of Swords')
bbbb=('II of Swords')
cccc=('III of Swords')
dddd=('IIII of Swords')
eeee=('V of Swords')
ffff=('VI of Swords')
gggg=('VII of Swords')
hhhh=('VIII of Swords')
iiii=('VIIII of Swords')
jjjj=('X of Swords')
kkkk=('Page of Swords')
llll=('Queen of Swords')
mmmm=('King of Swords')
nnnn=('Knight of Swords')
aaaaa=('Ace of Cups')
bbbbb=('II of Cups')
ccccc=('III of Cups')
ddddd=('IIII of Cups')
eeeee=('V of Cups')
fffff=('VI of Cups')
ggggg=('VII of Cups')
hhhhh=('VIII of Cups')
iiiii=('VIIII of Cups')
jjjjj=('X of Cups')
kkkkk=('Page of Cups')
lllll=('Queen of Cups')
mmmmm=('King of Cups')
nnnnn=('Knight of Cups')

tarot0=[zero,a,l,d,p,g,s,u,cc,ff,ii,ll,aaa,ddd,ggg,kkk,nnn,aaaa,dddd,gggg,jjjj,mmmm,bbbbb,fffff,iiiii,lllll]

tarot10=[j,k,c,o,f,r,i,aa,dd,gg,jj,mm,bbb,eee,hhh,lll,bbbb,eeee,hhhh,kkkk,nnnn,ccccc,ggggg,jjjjj,mmmmm]

tarot21=[v,b,m,e,q,t,bb,ee,hh,kk,nn,ccc,fff,iii,mmm,cccc,ffff,iiii,llll,aaaaa,ddddd,eeeee,hhhhh,kkkkk,nnnnn]

import random

def ran(y,z):
   for i in range(3):
      x=random.randint(y,z)
      return(x)

sect1=ran(1,3)
sect2=ran(1,3)
sect3=ran(1,3)

catch=sect1,sect2,sect3

print(catch)

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


 
card1=deck1[8]

print (card1)
