
class india():
    def capital(self):
        print("New delhi is capital of india")
    def language(self):
        print("Hindi is national language of india")
    def type(self):
        print("hindu")

class USA():
    def capital (self):
       print("Washington, D.C. is the capital of USA.")
    def language(self):
        print("In USA all people speak english")
    def type(self):
        print("british")
    
ind_roll =india()
us_roll = USA()
for country in (ind_roll,us_roll):
    country.capital()
    country.language()
    country.type()

