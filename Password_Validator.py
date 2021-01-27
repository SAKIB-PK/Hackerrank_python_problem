while True:
    name = input ("Please type your name :")
    if name != "joe":
        continue
    password = input ("Welcome Joe, Please enter your password: " )
    if password == "swordfish":
        break
print ("Access Granted!")
