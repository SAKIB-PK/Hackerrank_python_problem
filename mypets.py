namelist = [ "sakib", "rahim", "mim", "memi", "sumaiya", "suraiya"]
name = input("What is your Name? ")
if name in namelist:
    print("You're name is found our database.")
elif name not in namelist:
    print("you are not entered our database. " )
    
