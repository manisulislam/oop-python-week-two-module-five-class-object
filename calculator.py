class Calculator:
    brand= "casio"
    def add(self, num1, num2):
        add_res=num1+num2
        return add_res
    def mul(self, num1, num2):
        mul_res= num1*num2
        return mul_res
    def deduct(self, num1, num2):
        deduct= num1-num2
        return deduct
    
my_calculator= Calculator()
add_result=my_calculator.add(5,2)
print(add_result)
mul_result= my_calculator.mul(6,4)
print(mul_result)
deduct_result= my_calculator.deduct(8,2)
print(deduct_result)