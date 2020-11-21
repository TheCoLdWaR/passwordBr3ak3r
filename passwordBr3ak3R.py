import sys
from termcolor import colored, cprint
import random

cprint("Attention!","red",attrs=["bold","blink"],file=sys.stderr)
text=colored("Welcome to the TheCoLdWaR's pw generator...","green",attrs=["concealed","bold"])
print(text)

targetUser=input("Enter Target's Name or Target's Username :")

showoptions = colored("Choose One :\n 1-)Single Digit(00-10) \n 2-)two digits(10-99) \n 3-)three digits(100-1000) \n 4-)Without The Vowels(1-1000)"
                       "\n 5-)underScoreAndYearCombination \n 6-)KeywordCombination \n 7-)RandomNumbers","red",attrs=["concealed","bold"])

print(showoptions)

choose=int(input(""))

def zeroTen(t):
    f = open("00-10.txt","w")
    for x in range(0,10,1):
        f.write(t+str(x)+"\n")
    f.close()
    cprint("Password Generated !","blue",attrs=["blink","bold"],file=sys.stderr)

def tenOneHundred(t):
        f = open("10-100.txt","w")
        for x in range(10,100,1) :
            f.write(t+str(x)+"\n")
        f.close()
        cprint("Password Generated !","blue",attrs=["blink","bold"],file=sys.stderr)

def oneHundredThousend(t):
    f = open("100-1000.txt","w")
    for x in range(100,1000,1):
        f.write(t+str(x)+"\n")
    f.close()
    cprint("Password Generated !","blue",attrs=["blink","bold"],file=sys.stderr)

def WithoutVowels(t):
    result=""
    Vowels = ["A","a","E","e","i","u","o","ı"]
    for x in t:
        if x not in Vowels:
            result+=x
    #print(result)
    f = open("withoutVowels(1-1000).txt","w")
    for y in range(1,1000,1):
        f.write(result+str(y)+"\n")
    f.close()
    cprint("Password Generated !","blue",attrs=["blink","bold"],file=sys.stderr)

def underScoreAndYearCombination(t):
    whichyear=input("Which Year Do you want to use ? (Example : 2001)")
    str1=""
    str2=""
    f = open("underScoreAndYearCombination","w")
    for x in range(0,len(t),1):
        res_x=list(t)
        res_x[x]="_"
        #print(res_x)
        for y in res_x:
            str1 +=y
            str2 +=y
        str1 +=whichyear+"\n"
        str2 +="\n"+whichyear
    #print(str2)
    f.write(str1)
    f.write(str2)
    f.close()
    cprint("Password Generated !","blue",attrs=["blink","bold"],file=sys.stderr)

def KeywordCombination():
    f=open("KeywordCombination","w")
    f2=open("KeywordCombination2","w")
    keywordChanger=0
    new=""
    new2=""
    keywords=[]
    print("Enter 5 keywords")
    for x in range(0,5,1):
        item=input("")
        keywords.append(item)
    for z in range(0,5,1):
        for y in range(0,100,1):
            new=keywords[z]+"_"+str(y)
            new2=keywords[z]+"."+str(y)
            f.write(new+"\n")
            f2.write(new2+"\n")
            #print(new)

            #keywordChanger=keywordChanger + 1
    f.close()
    f2.close()
    print(keywords)
    cprint("Password Generated !","blue",attrs=["blink","bold"],file=sys.stderr)

def RandomNumbers(t):
    f=open("RandomNumbers","w")
    str1=""
    for x in range(0,len(t),1):
        res_x=list(t)
        res_x[x]=random.randint(0,9)
        for y in res_x:
            str1 +=str(y)
        str1 +="\n"
    f.write(str1)
    f.close()
    cprint("Password Generated !","blue",attrs=["blink","bold"],file=sys.stderr)


if choose==1:
    zeroTen(targetUser)
elif choose==2:
    tenOneHundred(targetUser)
elif choose==3:
    oneHundredThousend(targetUser)
elif choose==4:
    WithoutVowels(targetUser)
elif choose==5:
    underScoreAndYearCombination(targetUser)
elif choose==6:
    KeywordCombination()
elif choose==7:
    RandomNumbers(targetUser)
else:
    cprint("wR0nq Ch01s3 br0... \ntRy 4g41n","blue",attrs=["blink","bold"],file=sys.stderr)
