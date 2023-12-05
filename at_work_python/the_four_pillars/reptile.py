from animal import Animal


class Reptile(Animal):          # Animal is the parent class, reptile is the derived class

    def __init__(self):
        super().__init__()      # super() refers to the super class when in a subclass
        self.cold_blooded = True

    def use_venom(self):
        print("bitey bitey")