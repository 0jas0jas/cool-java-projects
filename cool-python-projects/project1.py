def main():
    n = int(input("Enter a number: "))

    flag = 0
    i = 1

    while i <= (n/2):
        if (n % i) == 0:
            j = n/i;
            if (i + 1 == j or  j + 1 == 1):
                flag = 1;

        i = i + 1

    if flag == 1: print("The given number is a heteromecic number")
    else: print("The given number is not a heteromecic number")

main()