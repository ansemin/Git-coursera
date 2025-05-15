class Employee:
    def __init__(self, first, last, pay): #first, last, pay these are the attributes of the class
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'

    def fullname(self): #this is the methods where you can create functions within class that you can call later
        # self is needed because method expects at least one instance 
        return '{} {}'.format(self.first, self.last)
    
#Class -> blue print of instances

employ_1=Employee('Corey', 'Schafer', 50000)
employ_2=Employee('Test','User',6000) # each of these are the instances of the class employee
# Instance variable contains Data that is unique to each instance
# print(employ_1)
# print(employ_2)
print(employ_1.fullname())
print(Employee.fullname(employ_1)) #these are the same thing because employ_1 in employ.fullname() is 
# pass on as instance to Employee.fullname(employ_1)

# print(employ_1.email)
# print(employ_2.email)
# print(employ_1.fullname()) #make sure to add the () to call the method
# print(employ_2.fullname())

# instead of creating variables for each employee we can create a class
# class variables are the variables that are shared among all instances of a class
# we can create innit method to initialize the variables
# the innit method is the first method that runs when we create an instance of a class



