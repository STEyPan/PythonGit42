from book import Book

def book_input_data() -> object:
    new_book = Book()

    new_book.book_title = input("\nВведите название книги: ")
    new_book.book_autor = input("Введите имя автора: ")
    new_book.book_release = int(input("Введите год издания: "))
    new_book.book_publisher = input("Введите издание: ")
    new_book.book_genre = input("Введите жанр: ")
    new_book.book_price = input("Введите цену: ")
    print()

    return new_book


def book_menu() -> None:
    new_book = Book()
    choice = ""

    while choice != "0":

        print("\nКнига\n")
        print(f"1) Ввести данные\n"
              f"2) Показать данные\n"
              f"0) Выйти из программы\n")
        choice = input("Выберете пункт меню: ")

        if choice == "1":
            new_book = book_input_data()

        elif choice == "2":
            print(f"\n{new_book.get_data()}")

        elif choice == "0":
            print("До свидания!")

        else:
            print("Нет такой команды!")