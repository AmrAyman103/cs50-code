answer = input(" What is the Answer to the Great Question in Life, the Universie, and Everything?")

if answer.strip() == "42":
    print ("Yes")
elif answer.lower().strip() =="forty-two":
    print ("Yes")
elif answer.lower().strip() =="forty two":
    print ("Yes")
else:
      print("NO")

