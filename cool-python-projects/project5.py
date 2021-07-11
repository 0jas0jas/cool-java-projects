def  main():
    while True:
        print("Note: Roman Numbers are from 0 to 3999")
        n = int(input("Enter a number: "))

        if n <= 3999 or n >= 0:
            break
    
    s = ""

    if n == 0:
        s = "N"

    while n >= 1000:
        s = s+ "M";
        n = n - 1000;
    
    while n >= 900:
        s = s + "CM"
        n = n - 900
    
    while n >= 500:
        s = s + "D"
        n = n - 500
    
    while n >= 400:
        s = s + "CD"
        n = n - 400

    while n >= 100:
        s = s + "C"
        n = n - 100

    while n >= 90:
        s = s + "XC"
        n = n - 90

    while n >= 50:
        s = s + "L"
        n = n - 50

    while n >= 40:
        s = s + "XL"
        n = n - 50

    while n >= 10:
        s = s + "X"
        n = n - 10

    while n >= 9:
        s = s + "IX"
        n = n - 9

    while n >= 5:
        s = s + "V"
        n = n - 5
    
    while n >= 4:
        s = s + "IV"
        n = n - 4

    while n >= 1:
        s = s + "I"
        n = n - 1



    print(s)

main()