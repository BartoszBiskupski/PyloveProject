import json
class Czlowiek:
    bmi = 0
    def __init__(self, name, hight, weight):
        self.name = name
        self.hight = hight
        self.weight = weight


    def speak(self):
        print("mowie prawde")

    def count_bmi(self):
        self.bmi = (self.weight) / ((self.hight/100) **2)
        return round(self.bmi, 2)

    def diff_to_norm(self):

        if self.bmi <18.5:
            expected_weight = 18.5 * (self.hight/100) ** 2
            diff = expected_weight - self.weight
            print("musisz przytyc " + str(diff))
    def save_data(self):
        with open(''.json.format(self.name), w) as file:
            json.dump(
                {
                "waga": self.weight,


                },
                file
            )
    def to_burn(self):
        pass

    def to_eat(self):
        pass

    def what_to_do(self):
        pass

class Polityk(Czlowiek):
    bribed = False
    def speak(self):
        if self.bribed:
            super().speak()
        else:
            print("klamie bo moge")
    def recive_bribe(self):
        self.bribed = True

#bruno = Polityk()
#bruno.speak()
#bruno.recive_bribe()
#bruno.speak()
ziutek = Czlowiek("bruno", 180 , 200)
ziutek.speak()
print(ziutek.count_bmi())
zuza = Czlowiek("zuzzanna", 150, 20)
print(zuza.diff_to_norm())
zuza.save_data()