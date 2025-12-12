# class Student:
#     subject = "python"
#     college = "ABC"
#     year = "4th year"

# stu1 = Student()
# stu2 = Student()

# print(stu1.subject,stu1.college,stu1.year)


# class Student:
#     def __init__(self,name):
#         self.name = name

# stu1 = Student("Tarun")
# print(stu1.name)


# class Student:
#     def __init__(self,name,cgpa):
#         self.name = name
#         self.cgpa = cgpa

#     def get_cgpa(self):
#         return self.cgpa+1


# stu1 = Student("tarun", 8.0)

# print(f"{stu1.get_cgpa()}")


# class Students:
#     collage_name = "ABC collage"

#     def __init__(self,name,gpa):
#         self.name = name
#         self.gpa = gpa

# stu1 = Students("tarun" , 9.2)

# print(stu1.collage_name)


class Product:
    count = 0
    def __init__(self,name,price=10000):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"price of {self.name} is rs.{self.product}")


    @classmethod
    def get_count(cls):
        print(f"total products in the store= {cls.count}")   


    @staticmethod
    def cla_price(price,discount):
        print(f"discount price = {price-(price*(discount/100))}")    

p1 = Product("Phone",30_000)
p1.cla_price(p1.price,10)
