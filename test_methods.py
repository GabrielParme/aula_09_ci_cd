import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_sum():
    # given two numbers
    num1 = 2
    num2 = 5

    # when we calculate the sum
    output = methods.sum(num1, num2)

    #then the sum shoult be 7
    assert output == 7

def test_subtract():
    #given two numbers
    num1 = 5
    num2 = 2

    #when we calculate the difference
    output = methods.subtract(num1, num2)

    #then the difference should be 3
    assert output == 3

def test_multiply():
    #given two numbers
    num1 = 5
    num2 = 2

    #when we calculate the product 
    output = methods.multiply(num1, num2)

    #then the product should be 10
    assert output == 10

def test_division():
    ##given two numbers
    num1 = 5
    num2 = 2

    #when we calculate the quotient 
    output = methods.division(num1, num2)

    #then the quotient should be 2.5
    assert output == 2.5
    
    