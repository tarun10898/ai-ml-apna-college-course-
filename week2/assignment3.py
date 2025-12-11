# problem1:

# def palindrome(str1: str) -> bool:
#    str1 = str1.lower()
#    return str1 == str1[::-1]
# if __name__ == "__main__":
#     str1: str = input("enter a string to check the palindrome or not: ")
#     value: bool = palindrome(str1)
#     print(f"the given value is palindrome {value}")
   
#problem2:

# def average_of_numbers(arr:list[int]) -> int:
#     count: int= len(arr)
#     sum:int = 0
#     for i in arr:
#         sum += i
#     return sum//count    
     

# if __name__ == "__main__":
#     n:int = int(input("enter the number of elemets to be entered in the list: "))
#     arr:list[int] = list(map(int, input("enter the nu8mbers: ").strip().split()))[:n]
#     average: int =  average_of_numbers(arr)
#     print(f"the average of the numnbers {average}")

#problem3:

# list1: list[int] = [1,2,7]
# list2: list[int] = [2,4,5]
# result: list[int] = sorted(set(list1 +list2))
# print(result)

#problem4:

# def even_odd_numbers(arr: tuple[int, ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
#     even: tuple[int, ...] = tuple(i for i in arr if i % 2 == 0)
#     odd: tuple[int, ...] = tuple(i for i in arr if i % 2 != 0)
#     return even, odd

# if __name__ == "__main__":
#     n: int = int(input("Enter the number of elements: "))
#     arr_input = input("Enter the numbers separated by space: ").strip().split()
#     arr: tuple[int, ...] = tuple(map(int, arr_input[:n]))
#     even, odd = even_odd_numbers(arr)
#     print(f"Evens: {even}")
#     print(f"Odds: {odd}")


#problem5:



# if __name__ == "__main__":
#     dicit:dict[int,str] = {}
#     while True:
#         string:str = input(
#             "press the key according to the operation: \n"
#             "A - add the students\n"
#             "B - Update the marks\n"
#             "C - Search for all the students\n"
#             "D - Display alll the students and there marks\n"
#             "E - Exit\n"
#         ) 
#         if string.lower() == 'a':
#             name:str = input("enter the student names: ")
#             marks:int = int(input("Enter the marks: "))
#             dicit[name] = marks
#             print(f"Added {name} with marks {marks}")

#         elif string.lower() == 'b':
#             name:str = input("enter the name of the student: ")
#             if name in dicit:
#                 marks:int = int(input("enter the marks to change"))
#                 dicit[name] = marks
#                 print(f"updated {name}'s marks to {marks}")
#             else:
#                 print("Student is not found")
#         elif string.lower() == 'c':
#             name = input("Enter student name to search: ")
#             if name in dicit:
#                 print(f"{name} has {dicit[name]} marks")
#             else:
#                 print("Student not found!")
#         elif string.lower() == 'd':
#             print("All students and marks:")
#             for student, marks in dicit.items():
#                 print(f"{student}: {marks}")

#         elif string.lower() == 'e':
#             print("Exiting program...")
#             break

#         else:
#             print("Invalid option. Try again.")                


#problem6:

# if __name__ == "__main__":
#     dicit: dict[str,int] = {}
#     words: list[str] = ["apple", "banana", "kiwi", "cherry", "mango"]
#     for word in words:
#         if word not in dicit:
#             dicit[word] = len(word)
#     print(dicit)        

#problem 7:


# if __name__ == "__main__":
#     text: str = input("Enter a string: ")
#     space_count: int = text.count(" ")
#     print(f"The number of spaces in the string '{text}' is {space_count}")

#problem 8:

# def check_common_elements(list1: list[int], list2: list[int]) -> None:
#     set1 = set(list1)
#     set2 = set(list2)
#     found = False
#     for i in set1:  
#         if i in set2:
#             print(f"Common element found: {i}")
#             found = True
#             break
#     if not found:
#         print("No common elements")

# if __name__ == "__main__":
#     list1 = [1, 2, 7, 2, 3]
#     list2 = [4, 5, 6, 7, 2]
#     check_common_elements(list1, list2)

#problem 9:


# def once(arr: list[int])->set[int]:
#     list2:list[int]= []
#     count = 0
#     for i in arr:
#         count += 1
#         if i in arr[count: ]:
#             list2.append(i)
#     return set(list2)       


# if __name__ == "__main__":
#     arr:list[int] = list(map(int,input("enter the elements of the list: ").strip( ).split()))
#     apper:set[int] = once(arr)
#     print(f"the elemtns only apper only ones {apper}")


#problem 10:

# def get_unique(arr:list[int]) -> tuple[list[int],int]:
#     uniques:list[int] = [i for i in arr if arr.count(i) == 1]
#     return uniques,len(uniques)

# if __name__ == "__main__":
#     arr:list[int] = list(map(int,input("enter the elements in the list").strip().split()))
#     unique,counts = get_unique(arr)
#     print(f"list of eleemnts which are unique {unique} and count of the elements{counts}")