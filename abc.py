class Animal:
    def __init__(self):
        self.name = ""
        self.lifetime = 0
        self.food = ""
        self.grade = ""

    def getDetails(self):
        self.name = input("Enter the name of the animal: ")
        self.lifetime = int(input("Enter the lifetime of the animal (in years): "))
        self.food = input("Enter the food of the animal: ")

    def putDetails(self):
        print("Animal Details:")
        print("Name:", self.name)
        print("Lifetime:", self.lifetime, "years")
        print("Food:", self.food)
        print("Grade:", self.grade)

    def computeFitness(self):
        pass
class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.usedIn = "police department"
        self.noOfCrimesDetected = 0
        self.commandUnderstanding = 0
    def computeFitness(self):
        self.noOfCrimesDetected=int(intput("Enter crimes:"))
        if self.noOfCrimesDetected>25:
            self.grad='fit'
        elif 