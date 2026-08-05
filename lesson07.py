for i in range(5):
    print(i)    
# ====== Example 2 =====
for number in range(1, 6):
    print(number)
# ======= Example 3 =====
for i in range(3):
    print("Hello, Felix")
# ======= Example 4 =====
for i in range(5, 11):
    print(i)
# ======= Example 5 =====
for i in range(0, 10, 2):
    print(i)
# ======= Example 6 =====
for i in range(10, 0, -1):
    print(i)
# ======= Example 7 =====
count = 1
while count <= 5:
    print(count)
    count += 1
# ======= Example 8 =====
while True:
    text = input(" Nhập exit để thoát: ")
    if text == "exit":
        break
    print("Bạn nhập:", text)
# ====== Example 9 =====
for i in range(6):
    if i == 3:
        continue
    print(i)
# ======= Example 10 =====
total = 0
for i in range(1, 101):
    total += i
print(total)
# ======= Example 11======
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
