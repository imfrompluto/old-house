name = input("what is your name? ")
print("hello " + name + " you're currently stuck in a haunted house")



import time
import random
score = 0
life = 1
while life > 0:
    ghostdoor = random.randint(1,3)
    print("there are 3 doors in front of you")
    time.sleep(1)
    print()
    print("behind one of those there is a ghost hiding")
    time.sleep(1.5)
    print()
    print("you need to guess at which door there is no ghost")
    time.sleep(2)
    print()
    door = input("1, 2 or 3? ")
    print()
  
    if ghostdoor == int(door):
        print("you lose! your score was " + str(score))
        print()
        life = life - 1
        print("you have " + str(life) + " more life left")
        print()

    else:
        print("thats correct, keep going, the ghost was behind " + str(ghostdoor) + "!")
        print()
        if random.randint(1,10) == 4:
            life = 2
            print("you got an extra life, you currently have 2 lives")
        score = score +1
        print("score: " + str(score))
        print()

    # hw on whatsapp