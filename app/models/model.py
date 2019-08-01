import requests
import random
# def pickArea():
#     cuisine_url= 'https://www.themealdb.com/api/json/v1/1/list.php?a=list'
    
    
# area = 'American'
# # meal = 
# recipe_url= ''

# response = requests.get(area_url).json()
cuisine_url= 'https://www.themealdb.com/api/json/v1/1/list.php?a=list'
area = requests.get(cuisine_url).json()['meals'][5]['strArea']
meals_url= 'https://www.themealdb.com/api/json/v1/1/filter.php?a=' + area
meal = requests.get(meals_url).json()['meals'][0]['strMeal']
recipe_url='https://www.themealdb.com/api/json/v1/1/search.php?s=' + meal
recipe = requests.get(recipe_url).json()['meals'][0]['strIngredient7']
cuisineList = requests.get(cuisine_url).json()['meals']
# mealList = requests.get(meals_url).json()['meals']

# def cuisines():
#     for x in cuisineList:
#         print(x['strArea'])
#     return "done"
# cuisines()


def meals(cuisine_area):
    meals_url= 'https://www.themealdb.com/api/json/v1/1/filter.php?a=' + cuisine_area
    return requests.get(meals_url).json()['meals']

def recipes(meal_food):
    recipe_url='https://www.themealdb.com/api/json/v1/1/search.php?s=' + meal_food
    return requests.get(recipe_url).json()['meals']
    
# print(meals('Egyptian'))
# print(mealList)

    #requests.get(meals_url).json()['meals']
    
def code(cuisine):
    temp = {"American":"us","British":"gb","Canadian":"ca","Chinese":"cn","Dutch":"nl","Egyptian":"eg","French":"fr","Greek":"gr","Indian":"in","Irish":"ie","Italian":"it","Jamaican":"jm","Japanese":"jp","Kenyan":"ke","Malaysian":"my","Mexican":"mx","Moroccan":"ma","Russian":"ru","Spanish":"es","Thai":"th","Tunisian":"tn","Unknown":"aq","Vietnamese":"vn"}
    if cuisine not in temp:
        cuisine = random.choice(list(temp.keys()))
        # session['cuisine'] = cuisine
    return {'cuisine':cuisine, 'code':temp[cuisine]}
# print(requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s=Garides%20Saganaki').json()['meals'])