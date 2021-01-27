def spam():
    eggs =  "Spam Local" #spam Local print 2nd time
    print(eggs)
def bacon ():
    eggs = "bacon Local"
    print(eggs) #bacon Local print 1st time
    spam()
    print(eggs) # Bacon Local print 3rd time
eggs ="global"
bacon()
print(eggs) # global print 4th time
