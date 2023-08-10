def main():
    # we create a class with class and instance attribute, we include no object method here in thos class
    class Dog:
        # class attribute
        type = "mamel"

    # instance attributes
        def __init__(self, name):
            self.name = name

# Object Initialization
    tommy = Dog("Tommy")
    puppy = Dog("Puppy")

    # accessing class attribute
    print(f"Rogger is a {Dog.type}")
    # accessing instance attributes
    print(f"My name is {tommy.name}")

    print(puppy.type)
    print(tommy.type)


main()
