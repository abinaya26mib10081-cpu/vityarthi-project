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


def mark_number(card, marked, number):
    for i in range(5):
        for j in range(5):

            if card[i][j] == number:
                marked[i][j] = True
