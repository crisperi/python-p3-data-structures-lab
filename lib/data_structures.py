spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods): 
    names =[]
    for food in spicy_foods:
        names.append( (food["name"]))
        
    return names



def get_spiciest_foods(spicy_foods):
    spicy_food_list =[]
    for food in spicy_foods:
        if food["heat_level"] >5:
            spicy_food_list.append(food)
    return spicy_food_list


def print_spicy_foods(spicy_foods):
   
    for food in spicy_foods:
        name = food["name"]
        heat_level = int (food["heat_level"])
        emoji_heat = "🌶" * heat_level
        cuisine = food["cuisine"]
      
        print(f"{name} ({cuisine}) | Heat Level: {emoji_heat}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods :
        if food["cuisine"] == cuisine:
            print(food)
            return food
    


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print_spicy_foods([food])



def get_average_heat_level(spicy_foods):
    spicy_no =[]
    for food in spicy_foods:
        heat_no =int (food["heat_level"])
        spicy_no.append(heat_no)
        
    print (spicy_no)
    sum_heat = sum(spicy_no)
    print(sum_heat/len(spicy_no))
    return sum_heat/len(spicy_no)

get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
