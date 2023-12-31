def main ():
     message = input()
     print (convert(message))

def convert(message):
    message1 = message.replace(":)", "🙂")
    message2 =message1.replace(":(", "🙁")
    return message2

main( )
