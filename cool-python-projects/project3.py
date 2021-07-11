def main():
    message = str(input("Enter a string: "))
    crooked_message = []
    chars = list(message)
    switch = 1

    for char in chars:
        if switch == 0:
            crooked_message.append(char.lower())
            switch = 1
        elif switch == 1:
            crooked_message.append(char.upper())
            switch = 0


    output = ''.join(crooked_message)

    print("Your cRoOkEd message is '" + output + "', you're welcome.")

main()