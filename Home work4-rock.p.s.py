## Mohsen Pourdehghan

print('{r: rock | p: paper | s: scissors}\n')

p1_1st= input("hi 'Player 1', Set your first choice: ")
p1_2nd= input("Set your second choice: ")
p1_3rd= input("Set your third choice: ")
p1_score= 0

p2_1st= input("hi 'Player 2', your turn, Set your first choice: ")
p2_2nd= input("Set your second choice: ")
p2_3rd= input("Set your third choice: ")
p2_score=0 

# First round compare

if p1_1st == p2_1st :
    p1_score+= 0
    p2_score+= 0

elif p1_1st == "r" and p2_1st == "p":
    p2_score+= 1

elif p1_1st == "p" and p2_1st == "r":
    p1_score+= 1

elif p1_1st == "s" and p2_1st == "r":
    p2_score+= 1

elif p1_1st == "r" and p2_1st == "scissors":
    p1_score+= 1

elif p1_1st == "p" and p2_1st == "s":
    p2_score+= 1

elif p1_1st == "s" and p2_1st == "p":
    p1_score+= 1

# Second round compare

if p1_2nd == p2_2nd :
    p1_score+= 0
    p2_score+= 0

elif p1_2nd == "r" and p2_2nd == "p":
    p2_score+= 1

elif p1_2nd == "p" and p2_2nd == "r":
    p1_score+= 1

elif p1_2nd == "s" and p2_2nd == "r":
    p2_score+= 1

elif p1_2nd == "r" and p2_2nd == "s":
    p1_score+= 1

elif p1_2nd == "p" and p2_2nd == "s":
    p2_score+= 1

elif p1_2nd == "s" and p2_2nd == "p":
    p1_score+= 1

# Third round compare

if p1_3rd == p2_3rd :
    p1_score+= 0
    p2_score+= 0

elif p1_3rd == "r" and p2_3rd == "p":
    p2_score+= 1

elif p1_3rd == "p" and p2_3rd == "r":
    p1_score+= 1

elif p1_3rd == "s" and p2_3rd == "r":
    p2_score+= 1

elif p1_3rd == "r" and p2_3rd == "s":
    p1_score+= 1

elif p1_3rd == "p" and p2_3rd == "s":
    p2_score+= 1

elif p1_3rd == "s" and p2_3rd == "p":
    p1_score+= 1

print(f'\nscore of player 1: {p1_score}\nscore of player 2: {p2_score}')

# Final

if p1_score > p2_score :
    print('Player 1 is the winner!')

elif p1_score == p2_score :
    print('Draw!')
    
elif p1_score < p2_score :
    print('Player 2 is the winner!')
