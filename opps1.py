class Employee:
    # Special method in python, Magic methods or dunder methods.
    def __init__(self):
        print("Employee executing data/attributes.")
        self.id = 101
        self.name = "Irfan Muhammad"
        self.salary = 100000
        self.designation = "Software Engineer"
        self.location = "lahore"

        print("Employee data/attributes initialized.")

    def travel(self):
        print("Employee executing manually travel method.")
        self.destination = "London"
        print(f"Traveling to the {self.destination} office")
    
sam = Employee()
print(sam.id)
print(sam.name)
print(sam.salary)
print(sam.designation)

# Calling the method manually.
sam.travel() 