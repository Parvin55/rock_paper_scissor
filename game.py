import random
rock=0
paper=1
scissor=2
user=int(input("Enter your choice: "))
if(user>=3 or user<0):
    print("WRONG INPUT")
else:
    comp = random.randint(0, 2)
    print("computer choice: ", comp)
    if(user==comp):
        print("DRAW")
    elif(user==0 and comp==2):
        print("YOU WIN")
    elif(user==2 and comp==0):
        print("YOU LOOSE")
    elif(user>comp):
        print('YOU WINS')
    elif(comp>user):
        print("YOU LOOSE")
