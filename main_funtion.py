import book
import menu
import utils
import json
import time

def json_convert(title, authors, isbn, publishing_year, price, quantity):
    book = {
        "title": title,
        "authors": authors,
        "isbn": isbn,
        "publishing_year": publishing_year,
        "price": price,
        "quantity": quantity
    }
    return book



def add_book(books):
    title = input("Enter book title: ")
    authors = input("Enter authors (comma separated): ").split(",")
    isbn = input("Enter ISBN: ")
    publishing_year = input("Enter publishing year: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    new_book = json_convert(title, authors, isbn, publishing_year, price, quantity)
    print(new_book)
    books.append(new_book)
    time.sleep(2)
    message = utils.save_books_to_file(books)
    print(message)

def view_all_books(books):
    for book in books:
        print(book['title'],book['authors'],book['isbn'],book['publishing_year'],book['price'],book['quantity'])
        time.sleep(2)

def search_for_book(books):
    search_term = input("Enter search term: ")
    results = utils.find_book_by_title_or_isbn(books, search_term)
    if results:
        for book in results:
            print(book)
            time.sleep(2)
    else:
        print("No books found.")
        time.sleep(2)

def lend_book(books):
    search_term = input("Enter book title or ISBN: ")
    results = utils.find_book_by_title_or_isbn(books, search_term)
    if results:
        book_to_lend = results[0]
        if book_to_lend['quantity'] > 0:
            book_to_lend['quantity'] -= 1
            print(f"You have lent {book_to_lend['title']}.")
            utils.save_books_to_file(books)
            time.sleep(2)
        else:
            print("Not enough books available to lend.")
            time.sleep(2)
    else:
        print("Book not found.")
        time.sleep(2)

def return_book(books):
    search_term = input("Enter book title or ISBN: ")
    results = utils.find_book_by_title_or_isbn(books, search_term)
    if results:
        book_to_return = results[0]
        book_to_return['quantity'] += 1
        print(f"You have returned {book_to_return['title']}.")
        utils.save_books_to_file(books)
        time.sleep(2)
    else:
        print("Book not found.")
        time.sleep(2)

def view_lent_books(books):
    lent_books = [book for book in books if book['quantity'] == book['quantity']]
    for book in lent_books:
        print(book)
        time.sleep(2)

def main():
    books = utils.load_books_from_file()
    while True:
        menu.display_menu()
        choice = menu.get_user_choice()
        if choice == 1:
            add_book(books)
        elif choice == 2:
            view_all_books(books)
        elif choice == 3:
            search_for_book(books)
        elif choice == 4:
            lend_book(books)
        elif choice == 5:
            return_book(books)
        elif choice == 6:
            view_lent_books(books)
        elif choice == 7:
            break

if __name__ == "__main__":
    main()