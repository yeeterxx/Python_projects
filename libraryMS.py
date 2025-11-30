import json
import os

class Books:
    def __init__(self,title,author):
        self.title= title
        self.author= author 
        self.available=True
    
    def to_dict(self):
        return {"title": self.title, "author":self.author}

    def borrow(self):
        if self.available==True:
            self.available=False
            print("book borrowed !!")
        else:
            print("book not available to borrow!!")

    def return_book(self):
        if self.available==False:
            self.available=True
            print("book returned sucessfully!!")
        else:
            print("book already available!!")

FILENAME="books.json"

def load_books():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as f:
            data=json.load(f)
            return [ Books(d["title"],d["author"]) for d in data]
    else:
        return [
    Books("harry potter","jk rowling"),
    Books("one piece","eichiro oda"),
    Books("History of time", "stephen hawking")
]
    
def save_books():
    with open(FILENAME, 'w') as f:
        json.dump([b.to_dict() for b in books], f, indent=4)

books= load_books()


def view_all():
    for index,book in enumerate(books):
        status= "available " if book.available else "unavailable"
        print(f'{index}. {book.title}:{book.author} - {status} ')


while True:

        print("\n-- Library Management --")
        print("1. Add a book")
        print("2. View all books")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Quit")
        
        try:
            choice=int(input("enter a choice :"))
        except:
            print("value error!!")
            continue

        if choice==1:
            title= input("Enter title of book: ")
            author= input("Enter author of book: ")
            books.append(Books(title,author))
            

        elif choice==2:
            view_all()

        elif choice==3:
            view_all()
            try:
             pick= int(input("pick book to borrow:"))
             books[pick].borrow()
            except ValueError:
                print("invalid request!!")
                continue

        elif choice==4:
            view_all()
            try:
                pick=int(input("enter the book to return"))
                books[pick].return_book()
            except ValueError:
                print("invalid request")
                continue

        elif choice==5:
            break



    
    
    




        