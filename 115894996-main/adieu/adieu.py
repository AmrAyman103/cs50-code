import inflect
p = inflect.engine()
name=[]
while True:
    try:
        message = input("name: ")
        name.append(message)
    except EOFError:
         print()
         break

output =p.join(name)
print("Adieu, adieu, to "+ output)
