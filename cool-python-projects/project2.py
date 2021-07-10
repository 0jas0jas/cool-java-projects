def main():
    s = str(input("Enter a string: "))
    sArr = list(s)
    
    i = 0
    Arr = []

    while i < (len(sArr) - 1):
        try:
            if sArr[i] != sArr[i - 1]:
                Arr.append(sArr[i])
                
        except IndexError:
                break

        i = i + 1
        

    s2 = "".join(Arr)
    print("The edited string without consecutive repetition of characters is: ")
    print(s2)


main()