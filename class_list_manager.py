names = ["Alanoud", "Jood", "Sadeem", "Rana", "Rand"]

# Each student adds her function below this line

# Written by: Alanoud Altammami
def count_names(names):
 return len(names)

# Written by: Sadeem Alotaibi
def search_name(names, name):
    for student in names:
        if student == name:
            return True
    return False

def main():
 print("Welcome to the Class List Manager!")
 print("Class list:", names)
 print("Number of names:", count_names(names))

# Other students will call their functions here
print("Search for Sadeem:", search_name(names, "Sadeem"))

main()
