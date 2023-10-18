import random


def get_integer_input(prompt):
    """
    Requests input from the user and only accepts an integer. Keeps prompting until valid input is provided.

    :param prompt: str
    :return: int
    """
    while True:
        try:
            # Try converting the input to an integer
            return int(input(prompt))
        except ValueError:
            # If conversion fails, prompt again
            print("Das ist keine gültige Zahl. Bitte versuchen Sie es erneut.")


def guessing_game():
    """
    Runs the guessing game where the user has to guess a randomly generated number
    within a range they specify.
    """
    print("Willkommen zum Ratespiel!")

    # Get user-defined range with error handling for non-integer inputs
    lower_bound = get_integer_input("Bitte geben Sie die untere Grenze des Bereichs ein: ")
    upper_bound = get_integer_input("Bitte geben Sie die obere Grenze des Bereichs ein: ")

    # Generate a random number within the user-defined range
    random_number = random.randint(lower_bound, upper_bound)

    # Let the user define the number of attempts
    # attempts = get_integer_input("Wie viele Versuche möchten Sie haben? ")

    attempts = 3

    print(f"Sie haben {attempts} Versuche, um die Zahl zu erraten.")

    for attempt in range(1, attempts + 1):
        guess = get_integer_input("Bitte geben Sie Ihre Vermutung ein: ")

        if guess == random_number:
            print("Herzlichen Glückwunsch! Sie haben die Zahl richtig erraten.")
            break  # Exit the loop as the user has guessed correctly
        else:
            remaining_attempts = attempts - attempt  # Calculate remaining attempts
            if remaining_attempts > 0:
                print(f"Das ist nicht korrekt. {remaining_attempts} Versuch(e) verbleiben.")

    else:  # This part is executed only if the number wasn't guessed
        print(f"Leider haben Sie alle Versuche verbraucht. Die richtige Zahl war {random_number}.")


# Main execution
if __name__ == "__main__":
    # Entry point
    guessing_game()
