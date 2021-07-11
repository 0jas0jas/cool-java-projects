def main():
    s1 = str(input("Enter first string: "))
    s2 = str(input("Enter second string: "))
    s1 = s1.lower()
    s2 = s2.lower()

    lastChars1 = s1[-2: ]
    lastChars2 = s2[-2: ]
    
    if lastChars1 == lastChars2: print("The entered strings rhyme!")
    else: print("The entered strings do not rhyme!")

main()