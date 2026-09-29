def display_card(card, marked):

    print("\n     1    2    3    4    5")

    for i in range(5):

        for j in range(5):

            if marked[i][j]:
                print(" X ", end=" ")

            else:
                print("%2d " % card[i][j], end=" ")

        print()
