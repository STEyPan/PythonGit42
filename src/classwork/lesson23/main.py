from person import Person
from book import Book
from stack import Stack

# human_1 = Person()
# human_2 = Person("Jonh")
#
# print(human_1.name)
# print(human_2.name)

# def main():
#     price = float(input("Введите цену: "))
#     book = Book(price=price)
#     print(book.get_data())
#
# main()

# Создать класс для структуры данных Stack
# Класс должен иметь методы - push, pop, top, size

stack_1 = Stack()
print(stack_1.size_stack())
print(stack_1.push_item(10))
print(stack_1.push_item(100))
print(stack_1.top_item())
print(stack_1.size_stack())
print(stack_1.pop_item())
print(stack_1.top_item())

def main():
    numbers = []
    number = 0

    while number != -1:
        number = int(input("Введите число (-1 выключает цикл): "))
        numbers.append(number)


    item = int(input("Введите число которое хотите добавить: "))

    stack_2 = Stack(numbers)
    print(stack_2.size_stack())
    print(stack_2.top_item())
    print(stack_2.push_item(item))
    print(stack_2.push_item(item))
    print(stack_2.top_item())
    print(stack_2.pop_item())
    print(stack_2.top_item())
    print(stack_2.size_stack())

main()

