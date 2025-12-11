#problem 1:

# def tax(salary:int):
#     if salary <30000 :
#         return (salary*(0.05))
#     elif 30000<=salary<=70000:
#         return (salary*0.15)
#     elif salary>70000:
#         return (salary*0.25)
   


# if __name__ == "__main__":
#     salary:int = int(input("enter the salary: "))
#     tax_amount:int = tax(salary)
#     print(f"total salary {salary}, final taxed amount {tax_amount}")


#problem 2:

# def list_integers(list1:list[int]) -> list[int]:
#     list2 = []
#     for i in list1:
#         if i%2 == 0:
#             list2.append(i) 
#     return list2

# if __name__ == "__main__":
#     a:int = int(input("enter the integer1: "))
#     b:int = int(input("enter the integer2: "))
#     list1:list[int] = list(range(a,b+1))
#     final_list:list[int] = list_integers(list1)
#     print(final_list)        

# problem 3:

# def digits(n: int) -> list[int]:
#     list1: list[int] = []
#     while n:
#         num = n % 10
#         list1.append(num)
#         n //= 10  
#     return list1[::-1] 

# if __name__ == "__main__":
#     n: int = int(input("Enter the number: "))
#     split: list[int] = digits(n)
#     print(f"entered number {n}, digits in the number: {', '.join(str(d) for d in split)}")

#problem 4:


# def total_count(n:int) -> int:
#     count = 0
#     while n:
#         if n%10:
#             count += 1
#         n= n//10
#     return count        

# if __name__ == "__main__":
#     n:int = int(input("enter the number: "))
#     count = total_count(n)
#     print(f"count of the given number {n} is {count}")


# problem5:



# def total_count(n:int) -> int:
#     sum = 0
#     while n:
#         num = n%10
#         sum += num
#         n= n//10
#     return sum        

# if __name__ == "__main__":
#     n:int = int(input("enter the number: "))
#     sum = total_count(n)
#     print(f"count of the given number {n} is {sum}")


#problem 6:




# if __name__ == "__main__":
#     for i in range(1,101):
#         if (i%3 ==0 and i%5 == 0):
#             print(i)


#problem 7:

# if __name__ =="__main__":
#     quit:bool = True
#     while quit:
#         input1 = input("enter the number or want to exit enter 'Quit'")
#         if (input1.lower() == "quit"):
#             print("bye bye monisha ")
#             quit = False
#         elif (input1.lower() != "quit" ):
#             n:int = int(input1)
#             if n>0:
#                 print(f"{n} is a positive number")
#             elif n<0:
#                 print(f"{n} is a negative number") 
#             else:
#                 print("number is neither positive nor negative")      
        
#problem 8 

# def calculator(a: float, b: float, operation: str) -> float:
#     if operation == '+':
#         return a + b
#     elif operation == '-':
#         return a - b
#     elif operation == '*':
#         return a * b
#     elif operation == '/':
#         if b != 0:
#             return a / b
#         else:
#             raise ValueError("Cannot divide by zero")
#     else:
#         raise ValueError("Invalid operation")


# if __name__ == "__main__":
#     a:float = float(input("enter the number a: "))
#     b:float = float(input("enter the number b: "))
#     operation:str = input("enter the operation '+' , '-' , '*' , '/' ")
#     value = calculator(a,b,operation)
#     print(f"value for the given data {a} {operation} {b} = {value}")


#problem 9:

# def is_prime(n: int) -> bool:
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# if __name__ == "__main__":
#     n:int = int(input("enter the number: "))
#     value = is_prime(n)
#     print(f"{n} is prime: {value}")


#problem 10

# def guessing_game(secret: int):
#     while True:
#         guess = int(input("Guess the number: "))
#         if guess > secret:
#             print("Too high")
#         elif guess < secret:
#             print("Too low")
#         else:
#             print("Correct!")
#             break
# if __name__ == "__main__":
#     guessing_game(45)