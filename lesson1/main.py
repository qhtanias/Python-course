# text = "Hello this python course"

# print(text.lower())

# print(text.strip())

# print(text.upper())

# print(text.upper())

# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible to vote.") 
# elif age < 18:
#     print("You are not eligible to vote.")    
# else: 
#     print("Invalid age entered.")
  
#EX2
age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ").lower()
if age >= 18 and has_ticket == "yes":
    print("You can enter the concert.")
elif age < 18 and has_ticket == "yes":
    print("You are not allowed to enter the concert.")
else:
    print("You cannot enter the concert.")
if age >= 18 and has_ticket == "no":
    print("You cannot enter the concert without a ticket.")
else:
    print("You cannot enter the concert without a ticket.")
