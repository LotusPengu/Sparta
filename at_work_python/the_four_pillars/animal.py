class Animal:
    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("One breath in, one breath out")

    def eat(self):
        print ("nom nom nom")


""" should not utilise the class within the same document as the definition,
creation and use of the class should be completed somewhere else - too messy! """

""" the definition of the class should be hidden away (abstraction) """
