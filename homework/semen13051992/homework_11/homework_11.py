class Book:
    page_material = 'бумага'
    presence_text = True


    def reserv(self):
        if self.flag:
            print('зарезервирована')


    def __init__(self, name_book, author, pages, flag=True):
        self.name_book = name_book
        self.author = author
        self.pages = pages
        self.flag = flag


class Schoolbooks(Book):
    object = 'Математика'
    clas = 9
    tasks = True


    def __init__(self, name_book, author, pages, flag):
        super().__init__(name_book, author, pages, flag)


boock_1 = Book('Идиот', 'Достоевский', 500, True)
boock_2 = Book('Идиот', 'Достоевский', 500, False)
boock_3 = Schoolbooks('Алгебра', 'Иванов', 200, True)
boock_4 = Schoolbooks('Алгебра', 'Иванов', 200, False)

print('Название:',boock_1.name_book + ',', 'Автор:', boock_1.author + ',',
      'страниц:', str(boock_1.pages) + ',', 'материал:', boock_1.page_material + ',',
      boock_1.reserv)
print('Название:',boock_2.name_book + ',', 'Автор:', boock_2.author + ',',
      'страниц:', str(boock_2.pages) + ',', 'материал:', boock_2.page_material,
      boock_2.reserv)
print('Название:', boock_3.name_book + ',', 'Автор:', boock_3.author + ',',
      'страниц:', str(boock_3.pages) + ',', 'предмет:', boock_3.object + ',',
      'класс:', str(boock_3.clas) + ',', boock_3.reserv)
print('Название:', boock_4.name_book + ',', 'Автор:', boock_4.author + ',',
      'страниц:', str(boock_4.pages) + ',', 'предмет:', boock_4.object + ',',
      'класс:', boock_4.clas, boock_4.reserv)
