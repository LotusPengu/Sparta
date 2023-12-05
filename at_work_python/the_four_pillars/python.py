from snake import Snake


class Python(Snake):

    def __init__(self):
        super().__init__()
        self.venom = False

    def eat(self):
        print("yum yum yum")


""" this function is already in another class, when calling Python it will utilise
this .eat as it is the first it sees in the hierarchy """
