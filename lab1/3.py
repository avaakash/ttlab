salary = int(input("Enter salary: "))

if salary <= 10000:
    print("Clerk")
elif salary in range(10001, 20001):
    print('Operator')
elif salary in range(20001, 35001):
    print('Assistant')
elif salary in range(35001, 50001):
    print('Manager')
else:
    print('Invalid Post')