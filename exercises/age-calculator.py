# Write an algorithm that asks for user's age and prints in screen if the person is a minor (less than 19 years of age) or is an adult.

ageInput = input("Hi! we need to know your age. Please instert your age with digits: ")
print("Your input is: " + ageInput)
age = int(ageInput)


if age > 0 and age < 19:
    print("You are minor.")
elif age >=19 and age <100:
    print("You are an adult.")
else:
    print("Invalid age.")