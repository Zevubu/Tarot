#origenal test to turn letters into number equivalent 



word=input()
counter=0
max_index=len(word)-1

while counter<= max_index:
      b=word [counter]
      if b=="a":
         a=1
      elif b=="b":
         a=2
      print (a)
      counter=counter+1


#refined and changed to actualy work with tarot program
words = input()
counter = 0
max_index = len(words) - 1

while counter <= max_index:
    word = words[counter]
    if word=="a":
       a=1
    elif word=="b":
       a=2
    print(a)
    counter = counter + 1
    
    