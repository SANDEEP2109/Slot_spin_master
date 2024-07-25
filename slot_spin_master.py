import random

max_deposit = 500
max_lines = 3
max_bet = 100
min_bet = 1

row = 3
col = 3

symbol_count = {
    "A": 3,
    "B": 4,
    "C": 5,
    "D": 6
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_win(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def deposit():
    while True:
        amount = input("How much would you like to deposit? Max deposit $500: $")
        if amount.isdigit():
            amount = int(amount)
            if 0 < amount <= max_deposit:
                break
            else:
                print("Deposit amount must be greater than 0 and do not exceed max amount.")
        else:
            print("Please enter a number.")
    return amount

def print_slot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def number_of_lines():
    while True:
        lines = input(f"How many lines you want to bet (1-{max_lines}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= max_lines:
                break
            else:
                print("Please enter a valid number of lines as mentioned.")
        else:
            print("Please enter a number.")
    return lines

def bets():
    while True:
        amount = input("How much would you like to bet on each line?: $")
        if amount.isdigit():
            amount = int(amount)
            if min_bet <= amount <= max_bet:
                break
            else:
                print(f"Amount must be between ${min_bet} - ${max_bet}")
        else:
            print("Please enter a number.")
    return amount

def run(balance):
    lines = number_of_lines()
    while True:
        bet = bets()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You cannot bet more than your balance ${balance}.")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is {total_bet}.")

    slots = get_slot_spin(row, col, symbol_count)
    print_slot(slots)
    winnings, winning_lines = check_win(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        choice = input("Press enter to spin (press q to quit).")
        if choice.lower() == "q":
            break
        balance += run(balance)
    print(f"You left with ${balance}")

main()
