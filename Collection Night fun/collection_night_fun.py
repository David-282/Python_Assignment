from unittest import result


students_list = [("Alice", 78),("Bob", 45),("Charlie", 90),("Diana", 62),("Kent", 30)]


def tuple_unpacking(list):
    for element in list:
        name, score = element
        print(name,score)

tuple_unpacking(students_list)


def print_passed_students(list):

    for element in list:
        name, score = element
        if score >= 50:
            print(name)


print_passed_students(students_list)


def pass_student_count(list):
    count = 0
    for element in list:
        name, score = element
        if score >= 50:
            count += 1
    return count

print(pass_student_count(students_list))


products = [("Laptop", 1200),("Mouse", 25),("Keyboard", 45),("Monitor", 300),("USB Cable", 10)]


def checking_price(price):
    return price[1] > 100

print(list(filter(checking_price, products)))
    


def sum_products(list):
    total = 0
    for element in list:
        name, price = element
        total += price
    return total

print(sum_products(products))


def unpacking_products(list):
    for element in list:
        name, price = element
        print(f"Product: {name}-Price: {price}")

unpacking_products(products)



points = [ (2, 3),(-1, 4),(5, -6),(0, 7),(-3, -2)]

def positive_points_filter (points):
    return points[0] >=0 and points[1] >=0

print(list(filter(positive_points_filter, points)))


def positive_point (points):
    result = []
    for element in points:
        point_a, point_b = element
        if point_a >=0 and point_b >=0:
            result.append(element)
    return result

print(positive_point(points))



employees = [("John", "IT", 50000),("Jane", "HR", 45000),("Mike", "IT", 60000),("Sara", "Finance", 70000)]


def staff_unpacking(list):
    it_department = []
    for element in list:
        name, department, salary = element
        if department == "IT":
            it_department.append(element)

    for staff in it_department:
        name , department, salary = staff
        if salary >55000:
            print(name)
            

staff_unpacking(employees)


staff_list = [staff for staff in employees if staff[1] == "IT" and staff[2] >55000]
for staff in staff_list:
    name, department, salary = staff
    print(name)
