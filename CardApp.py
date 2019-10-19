"""
Program Info Comment
Name: Talon Schmidt
CSC 119-004
Date: 10/17/2019
Program Name: CardApp.py
Description: a program that takes user input describing a playing card in the
following shorthand notation:
A          Ace
2 ... 10   Card values 
J          Jack 
Q          Queen 
K          King 
D          Diamonds 
H          Hearts 
S          Spades 
C          Clubs
Sources
"""
def main():

    # variables

    A = "Ace"
    J = "Jack"
    Q = "Queen"
    K = "King"
    D = "Diamonds"
    H = "Hearts"
    S = "Spades"
    C = "Clubs"

    # input

    prompt = input("Please enter your card notation(A=Ace,J=Jack,Q=Queen,K=King,D=Diamonds,H=Hearts,S=Spades,C=Clubs & 2-10) # first:")

    # process formulas
    first = prompt[0]
    pos = len(prompt) - 1
    last = prompt[pos]

    # output

    if first in "AJQK" :
        if first == "A" :
            first = A
        elif first == "J" :
            first = J
        elif first == "Q" :
            first = Q
        elif first == "K" :
            first = K
            
    elif first in "23456789" :
        if first == "2" :
            first = "2"
        elif first == "3" :
            first = "3"
        elif first == "4" :
            first = "4"
        elif first == "5" :
            first = "5"
        elif first == "6" :
            first = "6"
        elif first == "7" :
            first = "7"
        elif first == "8" :
            first = "8"
        elif first == "9" :
            first = "9"
            
    elif first in "1" :
        first = "10"
        
    if last in "DHSC" :
        if last == "D" :
            last = D
        elif last == "H" :
            last = H
        elif last == "S" :
            last = S
        elif last == "C" :
            last = C

    print(first, "of", last)

main()

"""
Test Case 1
Please enter your card notation(A=Ace,J=Jack,Q=Queen,K=King,D=Diamonds,H=Hearts,S=Spades,C=Clubs & 2-10) # first:9S
9 of Spades

Test Case 2
Please enter your card notation(A=Ace,J=Jack,Q=Queen,K=King,D=Diamonds,H=Hearts,S=Spades,C=Clubs & 2-10) # first:AS
Ace of Spades

Test Case 3
Please enter your card notation(A=Ace,J=Jack,Q=Queen,K=King,D=Diamonds,H=Hearts,S=Spades,C=Clubs & 2-10) # first:5H
5 of Hearts
"""
        
        
