# name = str(input("Enter your name and address: "))
# print("Length of name & address: ",len(name))
# print(name.upper())
# print(name.capitalize())
# print(name.count("a"))
# print(name.find("ram"))
# print(name.endswith("lal"))

# name = input("Enter a name//: ")
# age = input("Enter a age: ")
# marks1 = int(input("Enter a marks 1: "))
# marks2 = int(input("Enter a marks 2: "))

# print("\nName = ", name, "\nAge = ", age, "\nResult = ", marks1+marks2)
# name = "Bhuwan Pulami Magar"
# print(f"Hello!, {name}")

lists = ["Ram", "Shyam", "Cat", 5, 7, 30.2, "Hello"]
print(lists)

lists.append("Yaman Gautam")
print("After Append list: ", lists)

lists.insert(4,"Apple")
print("After inserting: ", lists)

lists.pop(3)
print("After pop item: ", lists)

l1 = [5, 2, 7, 0, 10, 50, 23, 67]
l1.sort()
print("After sorted number: ", l1)

l1.reverse()
print("After reversed numbers: ", l1)

l1.remove(50)
print("After removed value in lists: ", l1)
