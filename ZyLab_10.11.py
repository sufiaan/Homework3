"""
Sufiaan Shaikh - 1859029

CIS-2348-18349

ZyLab - 10.11
"""
class FoodItem:

    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))

if __name__ == "__main__":
    food1 = FoodItem()

    name1 = input()
    fat1= float(input())
    carbs1 = float(input())
    protein1 = float(input())

    another_food = FoodItem(name1, fat1, carbs1, protein1)
    num_servings = float(input())

    food1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, food1.get_calories(num_servings)))
    print()

    another_food.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, another_food.get_calories(num_servings)))

