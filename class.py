class Mobile:
    def __init__ (self):
        self.model = "Realme X"

    def show_model(self):
        print("Model:",self.model)
realme= Mobile() #creat object and name is Realme
realme.show_model() #Print object method show_model()
print(realme.model) #access variable without class
realme.model= "RealMe pro"
realme.show_model()
print(id(realme))

