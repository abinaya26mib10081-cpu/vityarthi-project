def get_lines(marked):

    lines = []

    # Horizontal lines
    for i in range(5):

        complete = True

        for j in range(5):

            if not marked[i][j]:
                complete = False

        if complete:
            lines.append("Horizontal " + str(i + 1))

    # Vertical lines
    for j in range(5):

        complete = True

        for i in range(5):

            if not marked[i][j]:
                complete = False

        if complete:
            lines.append("Vertical " + str(j + 1))

    # First diagonal
    complete = True

    for i in range(5):

        if not marked[i][i]:
            complete = False

    if complete:
        lines.append("Diagonal 1")

    # Second diagonal
    complete = True

    for i in range(5):

        if not marked[i][4 - i]:
            complete = False

    if complete:
        lines.append("Diagonal 2")

    return lines
