class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

class Female(Human):
    def __init__(self, name, age, female_staff):
        super().__init__(name, age, "F")
        self.female_stuff = female_staff
        
    def voice(self):
        print("Чо ко во я вумен")

class Male(Human):
    def __init__(self, name, age, male_staff):
        super().__init__(name, age, "M")
        self.male_stuff = male_staff

    def voice(self):
        print("Чо ко во я мэле")

m = Male("Nikita", 19, ["Fortnite"])
mar = Female("Marg", 19, ["Skirt"])

print(m.__dict__, mar.__dict__, sep="\n")