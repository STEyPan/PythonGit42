def isEven(number):
    return number % 2 == 0

def isNumber(number):
    return (number > -1) and (number >= 10)

def evalFactorial(number):
    factorial = 1
    for n in range(2, number+1):
        factorial *= n
    return factorial

def evalSquare(number):
    return number*number

def makeDict(start, end):
    numbers = {}
    for num in range(start, end + 1):
        element = {}
        element["number"] = num
        element["isEven"] = isEven(num)
        element["isNumber"] = isNumber(num)
        element["Factorial"] = evalFactorial(num)
        element["Square"] = evalSquare(num)
        numbers[num] = element
    return numbers

def printDict(numbers):
    for key, value in numbers.items():
        print(f"\n{key}:\n\tnumber: {value["number"]}\n\teven: {value["isEven"]}"
              f"\n\tis number: {value["isNumber"]}\n\tfactorial: {value["Factorial"]}\n\t"
              f"square: {value["Square"]}\n")
def main():
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))
    numbers = makeDict(start, end)
    printDict(numbers)


main()