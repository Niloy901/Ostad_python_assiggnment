import json

def load_books_from_file():
    try:
        with open("books.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return "no books found"
    except json.JSONDecodeError:
        return "error occured"

def save_books_to_file(books):
    try:
        with open("books.json", "w") as f:
            json.dump(books, f, indent=4)  # Using indent=4 for pretty formatting
        print("Data successfully written to books.json")
        return "Success"
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Failed"

def find_book_by_title_or_isbn(books, search_term):
    return [book for book in books if search_term in book['title'] or search_term in book['isbn']]

def find_book_by_author(books, search_term):
    return [book for book in books if any(search_term in author for author in book['authors'])]