def CheckArmstrong(num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        return True
    else:
        return False


def CheckDivisibleby8(num):
    if num % 8 == 0:
        return True
    else:
        return False


def SmallestAmong3(a, b, c):
    if a < b and a < c:
        return a
    elif b < c:
        return b
    else:
        return c


def EvenOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


def isPalindrome(s):
    return s == s[::-1]


if __name__ == "__main__":
    while True:
        print("\nPress ")
        print("1 to Check Armstrong or not")
        print("2 to Check divisible by 8 or not ")
        print("3 to find smallest among three ")
        print("4 to to check even odd ")
        print("5 to to check palindrome or not ")
        print("6 to Exit")

        ch = int(input("Enter your Choice "))
        if ch == 1:
            num = int(input("Enter no.:"))
            print(CheckArmstrong(num))
        elif ch == 2:
            num = int(input("Enter no.:"))
            print(CheckDivisibleby8(num))
        elif ch == 3:
            a = int(input("Enter a:"))
            b = int(input("Enter b:"))
            c = int(input("Enter c:"))
            print(SmallestAmong3(a, b, c))
        elif ch == 4:
            num = int(input("Enter no.:"))
            print(EvenOdd(num))
        elif ch == 5:
            s = input("Enter String : ")
            print(isPalindrome(s))
        elif ch == 6:
            break
