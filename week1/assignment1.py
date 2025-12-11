print("hello world")

# problem 1:

# if __name__ == "__main__":
#     unserName: str = input("enter the user name:")
#     age: int = int(input("enter the age:"))
#     print(f"Hello {unserName}, you are {age} years old!")


#problem2:




# def differ(a: int, b: int) -> int:
#     return abs(a - b)

# if __name__ == "__main__":
#     input1: int = int(input("Enter the first number: "))
#     input2: int = int(input("Enter the second number: "))
#     total = input1 + input2
#     diff = differ(input1, input2)
#     mul = input1 * input2
#     quo = input1 / input2
#     print(f"sum: {total}, difference: {diff}, multiplication: {mul}, quotient: {quo}")



#problem 3:

# if __name__ == "__main__":
#     input1: int = int(input("enter the interger number: "))
#     input2: float = float(input("enter the floating number: "))
#     convert_input1: float = float(input1)
#     avg: float = ((convert_input1 + input2)/2)
#     print(f"Average:{avg}")

# pronlem 4:

# if __name__ == "__main__":
#     input1: str = input("enter the string containg a number: ")
#     convert_int: int = int(input1)
#     convert_float: float = float(input1)
#     print(f"integer: {convert_int}, float: {convert_float}, string: {input1}")


#problem 5:

# x:float = 10+3*2**2
# print(x)

#problem 6:


# def swaps(input1:int,input2:int) -> tuple[int, int]:
#     input1,input2 = input2,input1
#     return input1,input2


# if __name__ == "__main__":
#     input1: int = int(input("enter the input 1: "))
#     input2: int = int(input("enter the input 2: "))
#     swap:tuple[int, int] = swaps(input1,input2)
#     print(f"Before: {input1},{input2} After:{swap[0]},{swap[1]}")


# problem 7




# if __name__ == "__main__":
#     temp:str = input("enter the temperature in celsius: ")
#     temp_float = float(temp)
#     fahrenheitTemp:float = (temp_float*(9/5) + 32)
#     print(f"temperature in fahrenheit {fahrenheitTemp}")
                

# problem 8:

# def areas(r:int) -> float:
#     pie:float = 3.14
#     rs:float = float(r)
#     area:float = pie * (rs*rs)
#     return area
# if __name__ == "__main__":
#     radius:int = int(input("enter the radius as a integer: "))
#     area:float = areas(radius)
#     print(f"area of the circel {area}")


# problem 9:

# if __name__ == "__main__":
#     p:float = float(input("enter the principal: "))
#     r:float = float(input("enter the rate"))
#     t:float = float(input("enter the time"))
#     si:float = (p*r*t)/2 
#     print(f"simple interest {si}")


# problem 10:

# if __name__ == "__main__":
#     input1: float = float(input("enter the decimal number: "))
#     int_input:int = int(input1)
#     frac_part: float = input1 - (float(int_input))
#     print(f"interger part {int_input} fractional part {frac_part:.2f}")