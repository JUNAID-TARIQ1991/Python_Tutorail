# importing class as object
from Python_OOPs.inherritence import stdent_class_inher
from Python_OOPs.inherritence.Rectangle_cube import Rectangle


import sys
# print(sys.path)

shape1 = Rectangle(23, 34)
# print(shape1.length)
# print(shape1.Area)


# importing module as object

junaid = stdent_class_inher.FinalExam(10, 3)
print(junaid.grade(junaid.finalscore))
