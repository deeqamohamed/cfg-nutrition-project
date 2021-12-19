from Call_API import CallAPI
from Recipe_class import Recipe
import pandas as pd

def main():
    query = input("What ingredient would you like to enter? \n") #input one ingredient only

    print("\nHere is a list of health options: \n")

    health_list = ["alcohol-cocktail", "alcohol-free", "celery-free", "crustacean-free", "dairy-free", "DASH",
                   "egg-free", "fish-free" "fodmap-free", "gluten-free", "immuno-supportive", "keto-friendly",
                   "kidney-friendly", "kosher", "low-fat-abs", "low-potassium", "low-sugar", "lupine-free",
                   "Mediterranean", "mollusk-free", "mustard-free", "no-oil-added", "paleo", "peanut-free",
                   "pescatarian", "pork-free", "red-meat-free", "sesame-free", "shellfish-free", "soy-free",
                   "sugar-conscious", "sulfite-free", "tree-nut-free", "vegan", "vegetarian", "wheat-free"]

    for i in range(len(health_list)):
        print(f'{i + 1}. {health_list[i]}')

    while True:
        try:
            health_input = int(input("\nPlease type in the number that corresponds to your health choice?\n"))
        except:
            print("\nYou should only put in numbers, please try again:\n ")
        else:
            if health_input-1 < 35:
                break

    health = health_list[health_input-1]

    print("\nHere is a list of diet options: \n")
    diet_list = ["balanced", "high-fiber", "high-protein", "low-carb", "low-fat", "low-sodium"]

    for i in range(len(diet_list)):
        print(f'{i+1}. {diet_list[i]}')

    while True:
        try:
            diet_input = int(input("\nPlease type in the number that corresponds to your diet choice?\n"))
        except:
            print("\nYou should only put in numbers, please try again:\n ")
        else:
            if diet_input-1 < 6:
                break

    diet = diet_list[diet_input-1]

    excluded = input("\nWhat are you allergic to?\n")

    api = CallAPI(query, health, diet, excluded)
    api.call_api()
    api.get_recipe_info()

    recipe_dict = dict()
    for i in range(1, 21):
        recipe_dict[f'Recipe {i}'] = Recipe(api.recipe_info[i-1]["recipe_name"], api.recipe_info[i-1]["image"], api.recipe_info[i-1]["recipe_ingredients"], api.recipe_info[i-1]["calories"], api.recipe_info[i-1]["total_nutrients"], api.recipe_info[i-1]["allergies"])

    for k, v in recipe_dict.items():
        print(k + ":")
        print(v)
        print("\n")

    api.ask_user()

    while True:
        review_flag = input("\nDo you want to review another recipe? Y or N\n")
        if review_flag.upper() == "Y":
            api.ask_user()
        else:
            break

def csv_read(filename):
    df = pd.read_csv(filename)


if __name__== '__main__':
    main()



