import google.generativeai as genai
import streamlit as st

gemini_api_key = "GEMINI API KEY"      # Provide your Gemini API Key here
genai.configure(api_key = gemini_api_key)

def fetch_recipe(recipe_name):
    try:
        prompt = f"Recommend recipe to prepare {recipe_name}."
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        st.error(f"An error occurred while fetching recipe: {e}")
        return "Sorry , we couldn't fetch the recipe this time."

def fetch_recommendations(ingredient_name):
    try:
        prompt = f"Give recipes that can be made with {ingredient_name}."
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        st.error(f"An error occurred while fetching recommmendations: {e}")
        return "Sorry , we couldn't fetch the recommendations this time."

def fetch_ideas(meal_type):
    try:
        prompt = f"Give recipes that can be made in {meal_type}."
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        st.error(f"An error occurred while fetching ideas: {e}")
        return "Sorry , we couldn't fetch the ideas this time."

def fetch_restaurants(food,city,state):
    try:
        prompt = f"Give restaurant names in {city} city of {state} state where one can eat {food} food item."
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        st.error(f"An error occurred while fetching restaurants: {e}")
        return "Sorry , we couldn't fetch the restaurants this time."

def main():
    st.set_page_config(page_title="MealMate", page_icon="https://th.bing.com/th/id/R.997f4ee69a66e5c3634a9c206f604a9c?rik=3kPbQ0749kVu1Q&riu=http%3a%2f%2fwww.pngmart.com%2ffiles%2f4%2fCooking-PNG-Clipart.png&ehk=nUd%2fWkOcm5O0g%2bUxTDWOYFw3ELEdVMIZa9lYVXVRy34%3d&risl=&pid=ImgRaw&r=0") 
    st.title("MealMate - Recipe Recommender Bot")
    st.write("Welcome to MealMate! Let's see what is in dinner tonight.")

    user_name = st.text_input("What is your name?")
    if user_name:
        option = st.selectbox("Choose an option: " , ["Choose anyone","Get a recipe directly" , "Get recipe suggestions from ingredients" , "Know what to make today" , "Know restaurants to eat your favourite food"])

        if option == "Get a recipe directly":
            recipe_name = st.text_input("Which recipe do you want to know ? ")

            if st.button("Get Recipe"):
                recipe = fetch_recipe(recipe_name)
                st.write("Here is the recipe you want : ")
                st.write(recipe)

        elif option == "Get recipe suggestions from ingredients":
            ingredient_name = st.text_input("Give the name of main ingredient that you have : ")

            if st.button("Get Recommendations"):
                recommendations = fetch_recommendations(ingredient_name)
                st.write("Here are some recipes that you can make: ")
                st.write(recommendations)

        elif option == "Know what to make today":
            meal_type = st.selectbox("Which type of meal do you need to cook?", ["Breakfast" , "Brunch" , "Lunch" , "Evening Snack" , "Dinner"])

            if st.button("Get Ideas"):
                ideas = fetch_ideas(meal_type)
                st.write("Here are some ideas what you can make: ")
                st.write(ideas)

        elif option == "Know restaurants to eat your favourite food":
            food = st.text_input("What do you want to eat : ")
            city = st.text_input("In which city do you live: ")
            state = st.text_input("In which state do you live : ")

            if st.button("Get Restaurants"):
                restaurants = fetch_restaurants(food,city,state)
                st.write(f"Here are some dinings where you can eat {food}: ")
                st.write(restaurants)

    st.write("Thank you for using MealMate. Enjoy your food!")

if __name__ == "__main__":
    main()