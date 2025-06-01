class Book:
    __title = str()
    __autor = str()
    __release = 1970
    __publisher = str()
    __genre = str()
    __price = 0.0

    def __init__(self,
                 title : str = "Название",
                 autor : str = "Автор",
                 release : int = 1970,
                 publisher : str = "Издание",
                 genre : str = "Жанр",
                 price : float = 0.0):

        self.__title = title
        self.__autor = autor
        self.__release = release
        self.__publisher = publisher
        self.__genre = genre
        self.__price = price

    def __del__(self):
        pass

    def input_data(self,
                   title: str = None,
                   autor: str = None,
                   release: int = None,
                   publisher: str = None,
                   genre: str = None,
                   price: float = None
                   ):

        self.__title = title if title != None else self.__title
        self.__autor = autor if autor != None else self.__autor
        self.__release = release if release != None else self.__release
        self.__publisher = publisher if publisher != None else self.__publisher
        self.__genre = genre if genre != None else self.__genre
        self.__price = price if price != None else self.__price


    def get_data(self):
        return (f"Название книги: {self.__title}\n"
                f"Автор: {self.__autor}\n"
                f"Год издания: {self.__release}\n"
                f"Издание: {self.__publisher}\n"
                f"Жанр: {self.__genre}\n"
                f"Цена: {self.__price} р")

    @property
    def book_title(self):
        return self.__title

    @book_title.setter
    def book_title(self, new_title: str = None):
        if new_title != None:
            self.__title = new_title

    @property
    def book_autor(self):
        return self.__autor

    @book_autor.setter
    def book_autor(self, new_autor: str = None):
        if new_autor != None:
            self.__autor = new_autor

    @property
    def book_release(self):
        return self.__release

    @book_release.setter
    def book_release(self, new_release: int = None):
        if new_release != None:
            self.__release = new_release

    @property
    def book_publisher(self):
        return self.__publisher

    @book_publisher.setter
    def book_publisher(self, new_publisher: str = None):
        if new_publisher != None:
            self.__publisher = new_publisher

    @property
    def book_genre(self):
        return self.__genre

    @book_genre.setter
    def book_genre(self, new_genre: str = None):
        if new_genre != None:
            self.__genre = new_genre

    @property
    def book_price(self):
        return self.__price

    @book_price.setter
    def book_price(self, new_price: int = None):
        if new_price != None:
            self.__price = new_price

