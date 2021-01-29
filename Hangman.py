# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 16:29:36 2021

@author: Test
"""

class Hangman_init:
    def __init__(self,size):
        self.dashes = ["_"]*size
    
    def Complete(self):
        if "_" in self.dashes:
            return False
        else:
            return True
        
    def Update(self,word,guess):
        found = False        
        for i in range(len(word)):
            if guess == word[i]:
                self.dashes[i]=word[i]
                found = True
        return found
        
    def show(self):
        line=""
        i=0
        while i<len(self.dashes):
            line=line + self.dashes[i]+" "
            i+=1
        print(line)

class Picture:
    def __init__(self,step=0):
        self.step=0
    
    def increment(self):
        self.step+=1
        
    def get(self):
        return self.step
    
    def show(self):
        l1=l2=l3=l4=l5=l6=""
        if self.step>0:
            l2=l3=l4=l5=l6=" |"
        if self.step>1:
            l1=" ____"
        if self.step>2:
            l6="/|\\"
        if self.step>3:
            l2=" |/ |"
        if self.step>4:
            l3=" |  o"
            l4=" | /|\\"
            l5=" | / \\"
        print(l1,l2,l3,l4,l5,l6, sep="\n")

#game initializer
Word=input("input word:")
print(Word)
wrongGuesses=[]
gameOver=False
Word=Word.rstrip()
Hangman=Hangman_init(len(Word))
Pic=Picture()

while not gameOver:
    Pic.show()
    Hangman.show()
    out=""
    for i in range(len(wrongGuesses)):
        out+=wrongGuesses[i]+"  "
    print(out)
    Guess=input("Guess a letter: ")
    myChar=Guess[0]
    if Hangman.Update(Word,myChar)==False:
        Pic.increment()
        wrongGuesses.append(myChar) 
    gameOver = Hangman.Complete() or Pic.get()==5

if Hangman.Complete():
    print("Congratulations")
    print("The word was ", Word)
else:
    Pic.show()
    Hangman.show()
    out=""
    for i in range(len(wrongGuesses)):
        out+=wrongGuesses[i]+" "
    print(out + " R.I.P.")
    print("The word was " + Word)
    

    