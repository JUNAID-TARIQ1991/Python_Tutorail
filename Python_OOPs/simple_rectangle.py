class Rectangle:
    def __init__(self, length, width, height):
        """constructor: constructor is special method which is called 
        when an object is created(in memory). 
        Self: self is the reference to the current object. when we call Rectangle class python internally 
        create an object in the memory and set delf to refernce that object in memory
        Attributes: An object can have several attributes, that are basicaaly veriable that store
        data about the object, i,e, length, width, height
        Example: a human class: each object has attributes like, hair color, eye color, height, weight
        and method to an object: walk, run, read, get-name, get_state
        Remember: The method you create in a class must have one parameter called self """

        self.length = length
        self.width = width
        self.height = height

    def get_length(self):
        return self.length

    def get_SQRvolume(self):
        try:
            if self.length == self.width:
                print("The volume of square is:")
                return self.length*self.width*self.height
            else:
                print("Not a square object")
        except:
            print("Enter valid parameters for an object")

    def get_volume(self):

        return self.length*self.width*self.height

    def get_area(self):
        print("The area of the rectangle is follow:")
        return self.length*self.width


square = Rectangle(20, 40, 45)
square1 = Rectangle(30, 30, 40)
print(square.get_length())
print(square.get_area())
print(square.get_SQRvolume())


print(Rectangle.get_SQRvolume(self=square1))
