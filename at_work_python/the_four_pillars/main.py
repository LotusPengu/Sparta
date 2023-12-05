from animal import Animal
from reptile import Reptile
from snake import Snake
from python import Python

cat = Animal()
cat.eat()

lizard = Reptile()
lizard.eat()        # This works because python will work itself up the class hierarchy until a match is found
lizard.use_venom()

samantha_the_snake = Snake()
print(samantha_the_snake)
print(samantha_the_snake.cold_blooded)
# print(samantha_the_snake.venom)

perry_the_python = Python()

samantha_the_snake.eat()
perry_the_python.eat()

