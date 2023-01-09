import random

# Constants for the maximum and minimum number of lines and bet
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# Constants for the number of rows and columns in the slot machine
ROWS = 3
COLS = 3

# Dictionary mapping symbols to their counts on the slot machine
SYMBOL_COUNT = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# Dictionary mapping symbols to their values in terms of winnings
SYMBOL_VALUE = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


# Calculates the winnings for a given spin of the slot machine
def check_winnings(columns, lines, bet, values):
    # Initialize variables to track total winnings and winning lines
    winnings = 0
    winnings_lines = []

    # Loop through each line in the slot machine
    for line in range(lines):
        # Get the symbol for the first column of the current line
        symbol = columns[0][line]

        # Loop through each column in the current line
        for column in columns:
            # Get the symbol for the current column
            symbol_to_check = column[line]

            # If the symbol for the current column is different from the first column,
            # move on to the next line
            if symbol != symbol_to_check:
                break

        # If the loop completes without breaking, that means all symbols in the current line are the same
        # so we add the winnings for that line to the total winnings
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    # Return the total winnings and the winning lines
    return winnings, winnings_lines


# Generates a random spin of the slot machine
def get_slot_machine_spin(rows, cols, symbols):
    # Create a list of all the symbols in the slot machine,
    # with each symbol repeated the number of times it appears in the "symbols" dictionary
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        # Add the current symbol to the list the number of times it appears
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # Initialize an empty list to store the columns of symbols for the spin
    columns = []

    # Loop through the number of columns in the slot machine
    for _ in range(cols):
        # Initialize an empty list to store the symbols for the current column
        column = []

        # Create a copy of the list of all symbols
        current_symbols = all_symbols[:]

        # Loop through the number of rows in the slot machine
        for _ in range(rows):
            # Randomly choose a symbol from the list of remaining symbols
            value = random.choice(all_symbols)

            # Remove the chosen symbol from the list of remaining symbols
            current_symbols.remove(value)

            # Add the chosen symbol to the current column
            column.append(value)

        # Add the current column to the list of columns
        columns.append(column)

    # Return the list of columns
    return columns


# Prints the symbols in each column of the slot machine
def print_slot_machine(columns):
    # Loop through each row in the slot machine
    for row in range(len(columns[0])):
        # Loop through each column in the slot machine
        for i, column in enumerate(columns):
            # Print the symbol for the current row and column, followed by a vertical bar (|) if it's not the last column
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            # Print the symbol for the current row and column without a vertical bar if it's the last column
            else:
                print(column[row], end="")

        # Print a newline after printing all the symbols for the current row
        print()


# Prompts the user for their deposit amount and returns it
def get_deposit_amount():
    # Loop until the user enters a valid deposit amount
    while True:
        # Prompt the user for their deposit amount
        amount = input("What would you like to deposit? $")

        # Check if the input is a number
        if amount.isdigit():
            # Convert the input to an integer and store it in the "amount" variable
            amount = int(amount)

            # If the amount is greater than 0, exit the loop
            if amount > 0:
                break
            # If the amount is not greater than 0, print an error message and loop again
            else:
                print("Amount must be greater than 0.")
        # If the input is not a number, print an error message and loop again
        else:
            print("Please enter a number.")

    # Return the deposit amount
    return amount


# Prompts the user for the bet amount and returns it
def get_bet_amount(balance):
    # Loop until the user enters a valid bet amount
    while True:
        # Prompt the user for the bet amount
        amount = input("Would you like to bet on each line? $")

        # Check if the input is a number
        if amount.isdigit():
            # Convert the input to an integer and store it in the "amount" variable
            amount = int(amount)

            # If the amount is within the allowed range (MIN_BET to MAX_BET), exit the loop
            if MIN_BET <= amount <= MAX_BET:
                break
            # If the amount is not within the allowed range, print an error message and loop again
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        # If the input is not a number, print an error message and loop again
        else:
            print("Please enter a number.")

    # Return the bet amount
    return amount


# Prompts the user for the number of lines to bet on and returns it
def get_number_of_lines():
    # Loop until the user enters a valid number of lines
    while True:
        # Prompt the user for the number of lines to bet on
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")

        # Check if the input is a number
        if lines.isdigit():
            # Convert the input to an integer and store it in the "lines" variable
            lines = int(lines)

            # If the number of lines is within the allowed range (1 to MAX_LINES), exit the loop
            if 1 <= lines <= MAX_LINES:
                break
            # If the number of lines is not within the allowed range, print an error message and loop again
            else:
                print("Enter a valid number of lines.")
        # If the input is not a number, print an error message and loop again
        else:
            print("Please enter a number.")

    # Return the number of lines
    return lines


# Simulates a spin of the slot machine and returns the resulting balance
def spin(balance):
    # Get the number of lines to bet on from the user
    lines = get_number_of_lines()

    # Loop until the user enters a valid bet amount
    while True:
        # Get the bet amount from the user
        bet = get_bet_amount(balance)

        # Calculate the total bet amount (bet * lines)
        total_bet = bet * lines

        # If the total bet amount is greater than the balance, print an error message and loop again
        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}.")
        # If the total bet amount is not greater than the balance, exit the loop
        else:
            break

    # Print the bet and total bet amounts
    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    # Generate a random spin of the slot machine
    slots = get_slot_machine_spin(ROWS, COLS, SYMBOL_COUNT)

    # Print the symbols in each column of the slot machine
    print_slot_machine(slots)

    # Calculate the winnings for the spin
    winnings, winnings_lines = check_winnings(slots, lines, bet, SYMBOL_VALUE)

    # Print the winnings and winning lines
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winnings_lines)

    # Calculate the new balance (balance + winnings - total_bet)
    new_balance = balance + winnings - total_bet

    # Return the new balance
    return new_balance


# The main function for the slot machine game
def main():
    # Prompt the user to start the game
    start = input(
        "Would you like to start the slot machine game? (y/n) ").lower()

    # If the user wants to start the game, execute the game loop
    if start == "y":
        # Get the deposit amount from the user
        balance = get_deposit_amount()

        # Game loop
        while True:
            # If the balance is 0, print a message and exit the game loop
            if balance == 0:
                print("You have no more money to play with.")
                break
            # Print the current balance
            print(f"Your balance is: ${balance}")

            # Prompt the user to spin or quit the game
            spin_again = input("Would you like to (s)pin or (q)uit? ").lower()

            # If the user wants to spin, spin the slot machine and add the result to the balance
            if spin_again == "s":
                balance += spin(balance)
            # If the user wants to quit, exit the game loop
            elif spin_again == "q":
                break
            # If the user inputs an invalid response, print an error message
            else:
                print("Invalid input. Please enter 's' to spin or 'q' to quit.")

        # Print the final balance after the game loop has exited
        print(f"Your final balance is: ${balance}")
    # If the user does not want to start the game, print a goodbye message
    else:
        print("Goodbye!")


 # Start the slot machine game
main()
