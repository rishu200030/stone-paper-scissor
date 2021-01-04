import random

print("welcome to stone paper scissor")
print("we will have total 3 rounds for the game")
print("and if it's a tie then one extra round")
print("----------------------------------------------------")
compwin = 0
playwin=0
def ourchoice(a):
    if a == 1:
        print("you choose stone")
    if a == 2:
        print("you choose paper")
    if a == 3:
        print("you choose scissor")

def compchoice(a) :
    if a == 1:
        print("computer choose stone")
    if a == 2:
        print("computer choose paper")
    if a == 3:
        print("computer choose scissor")
COUNT = 0

while COUNT<3 :

    n = int(input(print("press '1' for stone,'2' for paper,'3' for scissor")))
    if n not in range(1,4):
        print("please make a valid choice")
        break
    else :
        flag = n
        ourchoice(n)

        computer =random.randint(1,3)
        compchoice(computer)

        if n == computer :

            print (" its a tie ")


        if (n== 1 and computer== 2) or (n== 2 and computer==3) or (n== 3 and computer==1) :
            print ("computer wins")
            compwin = compwin +1
            COUNT += 1

        if (n== 1 and computer== 3) or (n== 2 and computer==1)or (n== 3 and computer==2):

            print ("You wins")
            playwin =playwin +1
            COUNT += 1
        print("----------------------------------------------------")
print("----------------------------------------------------")

if compwin > playwin and COUNT == 3:
    print ("          COMPUTER IS THE WINNER")
    print("----------------------------------------------------")
    print("----------------------------------------------------")

if compwin < playwin and COUNT == 3:
    print ("             YOU ARE THE WINNER")
    print("----------------------------------------------------")
    print("----------------------------------------------------")






