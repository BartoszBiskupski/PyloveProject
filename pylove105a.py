import json
import os


class Czlowiek:
    bmi = 0

    def __init__(self, name, hight, weight):
        self.name = name
        self.hight = hight
        self.weight = weight

    def speak(self):
        print("mowie prawde")

    def count_bmi(self):
        self.bmi = (self.weight) / ((self.hight / 100) ** 2)
        return round(self.bmi, 2)

    def diff_to_norm(self):
        if self.bmi < 18.5:
            expected_weight = 18.5 * ((self.hight / 100) ** 2)
            diff = round(self.weight - expected_weight, 2)
            return diff
        elif self.bmi > 25:
            expected_weight = 25 * ((self.hight / 100) ** 2)
            diff = round(self.weight - expected_weight, 2)
            return diff
        else:
            print("you are fine")

    def save_data(self):
        with open('{}'.format(self.name), "w") as file:
            json.dump(
                {
                    "name": self.name,
                    "waga": self.weight,
                    "hight": self.hight,
                    "bmi": self.bmi

                },
                file
            )

    def to_burn(self):
        runing = 500
        bicycling = 600
        hobbing = 250
        chess = 150
        if self.diff_to_norm() > 0:
            running = round(self.diff_to_norm() / (6000/500),2)
            bicycling = round(self.diff_to_norm() / (6000 / 600),2)
            hobbing = round(self.diff_to_norm() / (6000 / 250),2)
            chessing = round(self.diff_to_norm() / (6000 / 150),2)
            how_many =  """"you need:
                %(run)s hours of running,
                %(bic)s hours of bicycling,
                %(hob)s hours of hobbing or
                %(ches)s hours of chessing
                to get to normal BMI""" %{'run': running, 'bic':bicycling, 'hob': hobbing, 'ches': chessing}
            return how_many
        else:
            print("you are fine")


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


# bruno = Polityk()
# bruno.speak()
# bruno.recive_bribe()
# bruno.speak()
# ziutek = Czlowiek("bruno", 180 , 200)
# print(ziutek.count_bmi())
zuza = Czlowiek("zuzzanna", 160, 150)
print(zuza.count_bmi())
print(zuza.diff_to_norm())
zuza.save_data()
print(zuza.to_burn())
