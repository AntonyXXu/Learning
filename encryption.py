# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 14:54:01 2021

@author: Test
"""

myMessage = "My sister received a scholarship from the University of Alberta for 2016"
myPrivateKey = "CMPT175"

mySortedPK=sorted(myPrivateKey)
print(mySortedPK)

myListedPK=list(myPrivateKey)
print(myListedPK)

myOrder=[]
i=0
while i<len(myListedPK):
    j=mySortedPK.index(myListedPK[i])
    myOrder.append(j)
    mySortedPK[j]=' '
    i=i+1
print(mySortedPK)
print(myOrder)
#3 corresponds to 3rd element in sorted C
#4 corresponds to 4th element in sorted M, etc...

#encipher:
#snip the msg to lengths of the private key
i=0
snips=[]
while i<len(myMessage):
    snip = myMessage[i:i+len(myPrivateKey)]
    i=i+len(myPrivateKey)
    snips.append(snip)
print(snips)


MyEncodedMessage=[]
j=0
while j < len(myOrder):
    i=0
    while i < len(snip):
        snip=snips[i]
        MyEncodedMessage.append(snip[myOrder[j]])
        i=i+1
    MyEncodedMessage.append('#') #end of snip
    print("".join(MyEncodedMessage))
    j=j+1
    
cypher="".join(MyEncodedMessage)
print(cypher)
    