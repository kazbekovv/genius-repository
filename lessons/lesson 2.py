class Books:

    prise=350

    def __init__(self, title, author):
        self.title=title
        self.author=author

    def __str__(self):
        return f'{self.title} \nавтор: {self.author}\n'

book1=Books("преступление и наказание",'достоевский')
print(book1)

book2=Books("этоМИР",'beka')
print(book2)

# дочерний класс
class Manga(Books):

    prise = 600
    def __init__(self, title, author,image='default.jpg'):
        Books.__init__(self,title,author)
        super().__init__(title,author)
        self.image=image

    def reverse(self):
        print('читай с права на лево')

    def __str__(self):
        return f'\nName: {self.title}\nAuthor: {self.author}, \n'



manga=Manga('берсерк','миура')
print(manga)
manga.reverse()