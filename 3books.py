class Book:
    def __init__(self,title):
        self.title=title
def create_book_list():
        return[Book("python 101"),Book("AI Basics"),Book("Data science")]
book=create_book_list()
for b in book:
  print("Books title:",b.title)
