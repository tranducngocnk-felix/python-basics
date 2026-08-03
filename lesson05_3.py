age = int(input("Nhập tuổi: "))
has_ticket = input("Bạn có vé không? (y/n): ")
if age >= 18 and has_ticket == 'y':
    print("Vào rạp thôi.")
else:
    print("Ở ngoài đi.")
    