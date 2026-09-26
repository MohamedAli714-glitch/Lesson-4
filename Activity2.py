Amount=int(input("Enter the withdrawal amount: "))

note1= Amount // 100

note2= (Amount % 100) // 50

note3= ((Amount % 100) % 50) // 20

note4= ((Amount % 100) % 50) % 20 // 10

print("The number of 100 notes is:", note1)
print("The number of 50 notes is:", note2) 
print("The number of 20 notes is:", note3)
print("The number of 10 notes is:", note4)