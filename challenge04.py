student = {
    "name": "Felix",
    "math": 8,
    "english": 9,
    "python": 10
}

print(student["name"])

average = (student["math"] + student["english"] + student["python"]) / 3
print(f"Average: {average}")

if average >= 8:
    print("Excellent")
else:
    print("Keep Learning")
