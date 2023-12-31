import random
while True:
    try:
        level=int( input("Level: "))
        if level>0:
            break

    except:
        pass
ramdom_number = random.randint(1,level)
while True:
    try:
        guess= int(input("Guess: "))
        if guess>0:
          if guess<ramdom_number:
            print("Too small!")

          elif guess>ramdom_number:
            print("Too large!")

          else:
            print("Just right!")
            break

    except:
        pass
