
"""
    Welcome to Elite 101 this program is a starter for your chatbot project.
    The starter prompts the user to enter their name and then greets them with a personalized message.

    Functions:
        get_user_name(): Prompts the user to enter their name and returns it.
        greet_user(name): Prints a greeting message using the provided name.
        main(): Main function that orchestrates the user input and greeting process.

    Execution:
        When the script is run directly (not imported as a module), it will execute the main() function.
"""



def get_user_name():
    return input("Please enter your name: ")

def get_user_age():
    return input("Please enter your age: ")

def greet_user(name, age):
    mood = input(f"Hello, {name}! You are {age} years old. How are you? ")
    return mood

def mood_user(mood):
    print(f"Oh, you are feeling {mood}? Nevertheless, remember that things can always get better!")
    print("Now, what is it that you need?")

def show_menu():
    print("\nMenu Options:")
    print("1. Option 1 (ph)")
    print("2. Option 2 (ph)")
    print("3. Option 3 (ph)")
    print("4. Exit")

def main():
    print("I'm Sandy's Chatbot!")
    user_name = get_user_name()
    user_age = get_user_age()
    user_mood = greet_user(user_name, user_age)
    mood_user(user_mood)

    show_menu()
    choice = input("Please choose an option (1-4): ")

    if choice == "1":
        print("You chose Option 1 (ph).")
    elif choice == "2":
        print("You chose Option 2 (ph).")
    elif choice == "3":
        print("You chose Option 3 (ph).")
    elif choice == "4":
        print("Be seeing ya.")
    else:
        print("Invalid choice. Please  try again.")

if __name__ == "__main__":
    main()
