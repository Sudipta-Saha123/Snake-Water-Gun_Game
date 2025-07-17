import random

def choice(comp, user):
    if(comp==user):
        return 0
    else:
        if(comp==0 and user==1):
            return -1
        elif(comp==1 and user==2):
            return -1
        elif(comp==2 and user==0):
            return -1
        
        return 1


com= random.randint(0,2)
you=int(input("enter your choice 0 for snake, 1 for water, 2 for Gun: "))

choices_name = ["Snake", "Water", "Gun"]
print("you: ", choices_name[you])
print("Computer choice: ", choices_name[com])

score = choice(com, you)
print("Score: ", score) 

if(score==0):
    print("it a draw")
elif(score== -1):
    print("you lose")
elif(score == 1):
    print("YOU WON")





