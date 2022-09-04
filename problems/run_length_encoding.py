def runLengthEncoding(string: str) -> str:
    x = ""
    letter = None
    counter = None

    for c in string:
        if c != letter:
            if letter is not None:
                while counter > 0:
                    if counter > 9:
                        x += f"9{letter}"
                    else:
                        x += f"{counter}{letter}"

                    counter -= 9

            letter = c
            counter = 1
        else:
            counter += 1
    else:
        while counter > 0:
            if counter > 9:
                x += f"9{letter}"
            else:
                x += f"{counter}{letter}"

            counter -= 9

    return x
