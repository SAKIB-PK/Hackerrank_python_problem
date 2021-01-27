def spam():
    global eggs
    eggs = "Spam" #eggs variable value can be modify
eggs = "Global"
spam()
print(eggs) # print spam
