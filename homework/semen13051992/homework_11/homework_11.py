class Book:
    page_material = 'бумага'
    presence_text = True

    def __init__(self, name_book, author, pages, isdn, reserv=False):
        self.name_book = name_book
        self.author = author
        self.pages = pages
        self.isdn = isdn
        self.reserv = reserv

    def str_book(self):
        text = (
            f"Название: {self.name_book}, Автор: {self.author} "
            f",страниц: {self.pages}, материал: {self.page_material}"
        )
        if self.reserv:
            return text + ", зарезервирована"
        return text


class Schoolbooks(Book):

    def __init__(self, name_book, author, pages, isdn, reserv, predmet, clas, tasks):
        super().__init__(name_book, author, pages, isdn, reserv)
        self.predmet = predmet
        self.clas = clas
        self.tasks = tasks

    def str_schoolbook(self):
        text = (
            f"Название: {self.name_book}, Автор: {self.author}, "
            f"страниц: {self.pages}, предмет: {self.predmet},"
            f"класс: {self.clas}")
        if self.reserv:
            return text + ", зарезервирована"
        return text


boock_1 = Book('Идиот', 'Достоевский', 500, "958-5-64-630925-2", True)
boock_2 = Book('Война и мир', 'Толстой', 700, "105-0-01-420481-7")
boock_3 = Book('Белая Гвардия', 'Булгаков', 300, "071-1-91-416831-1", True)
boock_4 = Book('Тихий Дон', 'Шолохов', 380, "376-2-96-285943-5")
boock_5 = Book('Мастер и Маргарита', 'Булгаков', 470, "417-7-83-135467-8", True)

print(boock_1.str_book())
print(boock_2.str_book())
print(boock_3.str_book())
print(boock_4.str_book())
print(boock_5.str_book())

Schoolbooks_1 = Schoolbooks('Алгебра', 'Иванов', 500, "958-5-64-630925-2",
                            True, "Математика", 8, True)
Schoolbooks_2 = Schoolbooks('Химия', 'Шыманович', 400, "345-5-68-927595-2",
                            False, "Химия", 9, True)
Schoolbooks_3 = Schoolbooks('Биология', 'Барысау', 390, "458-8-08-275956-2",
                            True, "Биология", 5, True)
Schoolbooks_4 = Schoolbooks('Физика', 'Исачанкова', 300, "584-5-66-595935-2",
                            False, "Физика", 6, True)
Schoolbooks_5 = Schoolbooks('География', 'Попов', 290, "434-1-88-459509-2",
                            True, "География", 9, True)

print(Schoolbooks_1.str_schoolbook())
print(Schoolbooks_2.str_schoolbook())
print(Schoolbooks_3.str_schoolbook())
print(Schoolbooks_4.str_schoolbook())
print(Schoolbooks_5.str_schoolbook())
