"""
error print because zero did'nt divide
def spam(DivideZero):
    return 22/ DivideZero
    
print(spam(2))
print(spam(4))
print(spam(0))
print(spam(1))
"""
"""
#Best Option to hundle Zero Division
def spam(DivideZero):
    try:
        return 22/ DivideZero
    except ZeroDivisionError:
        print("Invalid Value" )
    
print(spam(2))
print(spam(4))
print(spam(0))
print(spam(1))
"""

def spam(DivideZero):
    return 22/ DivideZero
try:    
    print(spam(2))
    print(spam(4))
    print(spam(0))
    print(spam(1))      # 1 did'nt divide because when 0 excute then except part is print so python don't back to print 1
except ZeroDivisionError:
    print("0 Did'nt Divide")
