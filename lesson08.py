student = {
    "name": "Felix",
    "age": 36,
    "city": "Ha Noi"
}
student = {
    "name": "Felix",
    "age": 36,
    "city": "Ha Noi"
}

print(student["name"])
print(student["age"])
student["job"] = "Data Engineer"

print(student)
student["age"] = 37

print(student)
del student["city"]

print(student)
student = {
    "name": "Felix",
    "age": 36,
    "job": "Data Engineer"
}

for key, value in student.items():
    print(key, value)
# ===== Exemple 1 =====
employee = {
    "id": 1001,
    "name": "Alice",
    "salary": 2500
}

for key, value in employee.items():
    print(key, value)
# ===== Exemple 2 =====
book = {
    "title": "Python",
    "price": 20,
    "author": "John"
}

book["price"] = 25

print(book)
