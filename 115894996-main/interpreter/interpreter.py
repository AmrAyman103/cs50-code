expretion = input("Expretion: ")
x, y, z = expretion.split()

new_x =float(x)
new_z =float(z)

if y == "+":
   result = new_x + new_z

if y == "-":
    result = new_x - new_z

if y == "*":
   result = new_x * new_z

if y == "/":
    result = new_x / new_z

print(round(result,1))
