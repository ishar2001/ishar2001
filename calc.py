#This is the operators definition section
print ("ISHA'S ADVANCED CALCULATOR")

def exponential (x,y):
    return x**y

def multiply (x,y):
    return x*y

def add (x,y):
    return x+y

def subtract (x,y):
    return x-y

def modulus (x,y):
    return x%y

def floor (x,y):
    return x//y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Division by 0 is not allowed"

#This is the operators definition section ends here

# Operation selection section
def operations():
    print ("Choose your preferred operation:")
    print ("a. Exponential")
    print ("b.Multiplication")
    print ("c.Subtraction")
    print ("d. Addition")
    print ("e.Division")
    print ("f.Modulus")
    print ("g.floor")

operations()

Options = input (" Choose one of the below (a/b/c/d/e/f/g)" )

# Operation selection section ends here


if Options in ["a","b","c","d","e","f","g"]:
    num1 = float(input ("Enter first value:"))
    num2 = float(input ("Enter second value:"))

    if Options == "a":
        print( "result:" , (exponential(num1,num2)))
    elif Options == "b":
            print("result:" , (multiply (num1,num2)))
    elif Options == "c":
            print("result:", (subtract(num1, num2)))
    elif Options == "d":
            print("result:", (add(num1, num2)))
    elif Options == "e":
            print("result:", (divide(num1, num2)))
    elif Options == "f":
        print("result:", (modulus (num1, num2)))
    elif Options == "g":
        print("result:", (floor (num1, num2)))
    else:
            print ("invalid input")


#end of code