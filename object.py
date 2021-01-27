class User:
    name = ""
    email = ""
    password = "" 
    login = False
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password



        
    def login(self):
        email = input("Enter your Email: ")
        password = input("Enter your Password: ")

        if email == self.email and password == self.password:
            login = True
            print("Login Successfully!")
        else:
            login = False
            print("Login Failed!")
    def islogged(self):
        if self.login:
            return True
        else:
            return False

    def profile(self):
        if self.islogged():
            print(f"Your name is {self.name} \nYour Password is {self.password}")
        else:
            print("You are not log in ....." )

user1 = User("Shakib Rahman ","golperrajjo@gmail.com","12345")
user1.login()
user1.profile()

wlcm = input()
