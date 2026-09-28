import random

def create_card():

    numbers = list(range(1, 26))
    random.shuffle(numbers)
    card = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(numbers[i * 5 + j])
        card.append(row)
    return card

def display_card(card, marked):

    print("\n     B    I    N    G    O")

    for i in range(5):
        for j in range(5):
            if marked[i][j]:
                print(" X ", end=" ")
            else:
                print("%2d " % card[i][j], end=" ")
        print()

def mark_number(card, marked, number):
    for i in range(5):
        for j in range(5):
            if card[i][j] == number:
                marked[i][j] = True

def get_lines(marked):
    lines = []
    for i in range(5):
        complete = True
        for j in range(5):
            if marked[i][j] == False:
                complete = False
        if complete:
            lines.append("Horizontal " + str(i + 1))

    for j in range(5):
        complete = True
        for i in range(5):
            if marked[i][j] == False:
                complete = False
        if complete:
            lines.append("Vertical " + str(j + 1))

    complete = True
    for i in range(5):
        if marked[i][i] == False:
            complete = False
    if complete:
        lines.append("Diagonal 1")

    complete = True
    for i in range(5):
        if marked[i][4 - i] == False:
            complete = False
    if complete:
        lines.append("Diagonal 2")

    return lines

player_card = create_card()
computer_card = create_card()

player_marked = []
computer_marked = []

for i in range(5):
    player_row = []
    computer_row = []
    for j in range(5):
        player_row.append(False)
        computer_row.append(False)
    player_marked.append(player_row)
    computer_marked.append(computer_row)
called_numbers = []
player_completed_lines = []
computer_completed_lines = []
bingo_letters = ["B", "I", "N", "G", "O"]

print("======================================")
print("              BINGO")
print("======================================")

print("\nYOUR CARD")
display_card(player_card, player_marked)
print("\nCOMPUTER CARD")
display_card(computer_card, computer_marked)

while True:

    print("\n--------------------------------------")
    print("             YOUR TURN")
    print("--------------------------------------")

    print("BINGO:", end=" ")
    for i in range(5):
        if i < len(player_completed_lines):
            print("X", end=" ")

        else:
            print(bingo_letters[i], end=" ")
    print()
    number = int(input("Choose a number (1-25): "))

    if number < 1 or number > 25:
        print("Enter a number between 1 and 25.")
        continue

    if number in called_numbers:
        print("This number was already called.")
        continue

    called_numbers.append(number)
    print("\nYou selected:", number)

    mark_number(player_card, player_marked, number)
    mark_number(computer_card, computer_marked, number)

    current_lines = get_lines(player_marked)
    for line in current_lines:
        if line not in player_completed_lines:
            player_completed_lines.append(line)
            print("\nYou completed:", line)
            print("BINGO letter crossed:",
                  bingo_letters[len(player_completed_lines) - 1])

            break

    print("\nYOUR CARD")
    display_card(player_card, player_marked)

    print("\nYour BINGO:")
    for i in range(5):
        if i < len(player_completed_lines):
            print("X", end=" ")
        else:
            print(bingo_letters[i], end=" ")

    print()

    if len(player_completed_lines) >= 5:

        print("\n======================================")
        print("          B I N G O")
        print("          YOU WIN!")
        print("======================================")

        break

    print("\n--------------------------------------")
    print("          COMPUTER TURN")
    print("--------------------------------------")


    available_numbers = []
    for number in range(1, 26):
        if number not in called_numbers:
            available_numbers.append(number)

    computer_number = random.choice(available_numbers)
    called_numbers.append(computer_number)

    print("Computer selected:", computer_number)

    mark_number(computer_card,
                computer_marked,
                computer_number)

    mark_number(player_card,
                player_marked,
                computer_number)

    current_lines = get_lines(computer_marked)
    for line in current_lines:
        if line not in computer_completed_lines:
            computer_completed_lines.append(line)
            print("\nComputer completed:", line)
            print("Computer crossed:",
                  bingo_letters[len(computer_completed_lines) - 1])

            break

    print("\nCOMPUTER CARD")
    display_card(computer_card, computer_marked)

    print("\nComputer BINGO:")
    for i in range(5):
        if i < len(computer_completed_lines):
            print("X", end=" ")
        else:
            print(bingo_letters[i], end=" ")

    print()

    if len(computer_completed_lines) >= 5:

        print("\n======================================")
        print("       B I N G O")
        print("       COMPUTER WINS!")
        print("======================================")

        break
