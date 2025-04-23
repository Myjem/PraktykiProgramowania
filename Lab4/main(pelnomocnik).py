class Dane:
    def pokaz(self):
            print("Tajne dane")

class Proxy:
    def __init__(self, haslo):
        self.haslo = haslo
        self.dane = Dane()

    def pokaz(self):
        if self.haslo == "test":
            self.dane.pokaz()
        else:
            print("nuh uh")

#dane = Dane()
#dane.pokaz()

subject1 = Proxy("test")
subject1.pokaz()

subject2 = Proxy("test2")
subject2.pokaz()