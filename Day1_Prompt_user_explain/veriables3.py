types=10
x=f"there are {types} of peoples"
print(x)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

'''In this Python code snippet, a joke_evaluation string is defined with a placeholder {} for a variable, 
and a boolean variable hilarious is set to False.

The joke_evaluation string contains a placeholder {} where some content will be inserted using the format() method. 
The format() method is a string method in Python that allows you to insert values into a string dynamically. In this case, 
the value of the hilarious variable will be inserted into the placeholder.

The print() statement is then used to output the joke_evaluation string, 
where the placeholder will be replaced by the value of the hilarious variable. Since hilarious is False, it will be displayed as part of the output.'''

skills= ['c', 'shell']
my_skills='These are my skills {} '
print(my_skills.format(skills))

name ='junaid'
age =32
skills = 'programmer'
print("my name is {}, I am {} year old, I have {} sklls".format(name, age, skills))

w='I love with my parents...'
s='I also love very much with my childerns'
print(w +s)
print ('*')
print ('*'*2)
print ('*'*3)
