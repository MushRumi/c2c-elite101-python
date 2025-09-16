
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

def greet_user(name):
    mood = input(f"Hello, {name}, how are you? ")
    return mood

def mood_user(mood):
    print(f"Oh, you are feeling {mood}? Nevertheless, remember that things can always get better!")

def main():
    user_name = get_user_name()
    user_mood = greet_user(user_name)
    mood_user(user_mood)

if __name__ == "__main__":
    main()
