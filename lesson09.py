def say_hello():
    print("Hello")
def greet(name):
    print(f"Hello {name}!")

greet("Felix")
greet("Alice")
greet("Bob")
def add(a, b):
    print(a + b)

add(5, 8)
add(100, 250)
def profile(name, age, city):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
profile("Felix", 36, "Ha Noi")
def add(a, b):
    print(a + b)

result = add(5, 8)

print(result)
def add(a, b):
    return a + b

result = add(5, 8)

print(result)
def square(number):
    return number * number

result = square(6)

print(result)
def square(number):
    return number * number

print(square(10) + 5)
def get_name():
    return "Felix"

print(get_name())
def is_adult(age):
    return age >= 18

print(is_adult(36))
def numbers():
    return [1,2,3,4]

print(numbers())
def person():
    return {
        "name":"Felix",
        "age":36
    }

print(person())
def calculate_average(math, english, python):
    return (math + english + python) / 3

average = calculate_average(8, 9, 10)

print(f"Average: {average:.2f}")


