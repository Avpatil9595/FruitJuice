import sys


class FruitJuice:
    def __init__(self, no_of_fruits, cupboard_fruit_list, fruit_calories_list, friends_calorie_intake):
        self.alphabet_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k',
                              12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u',
                              22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}

        self.no_of_fruits = no_of_fruits
        self.cupboard_fruits = cupboard_fruit_list
        self.fruits_calories = fruit_calories_list
        self.friends_calorie_consumption = friends_calorie_intake

        self.fruit_list = self.__generate_fruit_list()
        self.mapping = self.__map_fruits_with_calories()

    def __generate_fruit_list(self):
        count = 1
        f_list = list()
        while count <= self.no_of_fruits:
            f_list.append(self.alphabet_dict[count])
            count += 1
        return f_list

    def __map_fruits_with_calories(self):
        if not len(self.fruit_list) == len(self.fruits_calories):
            raise Exception('Calories are not provided for every fruits')
        return ({self.fruit_list[i]: self.fruits_calories[i] for i in range(len(fruit_list) - 1)},
                {self.fruits_calories[i]: self.fruit_list[i] for i in range(len(fruit_list) - 1)})

    def get_fruits_calories_in_cupboard(self):
        return sorted([self.mapping[0][f] for f in self.cupboard_fruits], reverse=True)

    def get_me_a_juice(self):
        sorted_fruits = self.get_fruits_calories_in_cupboard()
        juice_tried = 0
        while juice_tried < len(sorted_fruits):
            intake = self.friends_calorie_consumption
            juice_served = list()
            for sf in sorted_fruits[juice_tried:]:
                if sf <= intake:
                    juice_served.append(sf)
                    intake -= sf
            if sum(juice_served) == self.friends_calorie_consumption:
                return [self.mapping[1][js] for js in juice_served]
            juice_tried += 1

        return 'SORRY, YOU JUST HAVE WATER'


if __name__ == '__main__':
    number_of_friends = int(input("Please Enter Number of Friends invited"))
    if not isinstance(number_of_friends, int) or number_of_friends > 100:
        print("Please enter valid number")
        sys.exit()

    while number_of_friends > 0:
        fruit_calories = str(input("Please Enter Calories of Fruits"))
        fruit_list = fruit_calories.split(' ')
        if len(fruit_list) < 2:
            print("Please valid fruits with calories")
            sys.exit()

        fruits = int(fruit_list[0])
        fruit_calories = [int(f) for f in fruit_list[1:]]

        cupboard_fruits = str(input("Please Enter Fruits in cupboard"))
        cupboard_list = list(cupboard_fruits)

        friends_calorie_consumption = int(input("Please Enter Calorie intake of friend"))

        fj = FruitJuice(no_of_fruits=fruits, cupboard_fruit_list=cupboard_list, fruit_calories_list=fruit_calories,
                        friends_calorie_intake=friends_calorie_consumption)
        print(fj.get_me_a_juice())
        number_of_friends -= 1
    sys.exit('Thanks for coming!')
