def spam():
    global eggs
    eggs = " spam" # eggs are global variable
def bacon():
    eggs = "Local" # LOcal is a local variable
def hum():
    print(eggs)
eggs = "global"
spam()
print(eggs) # print spam
hum() # print global variable
