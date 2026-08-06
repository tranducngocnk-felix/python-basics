person = {
    "name": "Felix",
    "age": 36,
    "country": "Vietnam",
}
print(person)
print(person["name"])
person["job"] = "Data Engineer"
print(person)
person["age"] = 37
print(person)
for key, value in person.items():
    print(f"{key}: {value}")
# ===== Exercise 2 =====
laptop = {
    "Brand": "Macbook",
    "CPU": "M1",
    "Ram": "16GB",
    "SSD": "256GB",
}
print(laptop)
print(laptop["Ram"])
laptop["Price"] = 15000000
laptop["Ram"] = "32GB"
for key, value in laptop.items():
    print(f"{key}: {value}")
