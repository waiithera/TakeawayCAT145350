#Create a Book class with attributes for title, author, and is_borrowed
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False   
        
#  Implement methods in Book to: Mark as borrowed
def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"'{self.title}' has been marked as borrowed.")
        else:
            print(f"'{self.title}' is already borrowed.")

# Mark as returned
def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"'{self.title}' has been marked as returned.")
        else:
            print(f"'{self.title}' is not currently borrowed.")



def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"'{self.title}' by {self.author} ({status})")

#Create a LibraryMember class with attributes name, member_id, and a list for borrowed_books.

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # List to store borrowed books\
# Implement methods in `LibraryMember` to: Borrow a book (checks if the book is available), Return a book and List borrowed books

def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()  # Mark the book as borrowed
            self.borrowed_books.append(book)  # Add the book to the member's borrowed list
            print(f"{self.name} has borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is already borrowed and not available.")

def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()  # Mark the book as returned
            self.borrowed_books.remove(book)  # Remove the book from the borrowed list
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} has not borrowed '{book.title}'.")

def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has not borrowed any books.")

def __str__(self):
        print (f"Library Member: {self.name} (ID: {self.member_id})")

# Write interactive code to allow a member to borrow and return books.
# Create some books
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# Create a library member
member = LibraryMember("Alice", "M001")

# Interactive code for borrowing and returning books
while True:
    print("\nLibrary Menu:")
    print("1. Borrow a book")
    print("2. Return a book")
    print("3. List borrowed books")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAvailable books:")
        available_books = [book1, book2, book3]
        for i, book in enumerate(available_books, start=1):
            status = "Available" if not book.is_borrowed else "Borrowed"
            print(f"{i}. {book.title} by {book.author} ({status})")
        
        try:
            book_choice = int(input("Enter the number of the book to borrow: ")) - 1
            if 0 <= book_choice < len(available_books):
                member.borrowed_books.append(available_books[book_choice])

            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":
        print("\nBorrowed books:")
        if member.borrowed_books:
            for i, book in enumerate(member.borrowed_books, start=1):
                print(f"{i}. {book.title} by {book.author}")
            
            try:
                book_choice = int(input("Enter the number of the book to return: ")) - 1
                if 0 <= book_choice < len(member.borrowed_books):
                    member.return_book(member.borrowed_books[book_choice])
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("You have not borrowed any books to return.")

    elif choice == "3":  # List borrowed books
        if member.borrowed_books:
            print(f"{member.name} has borrowed the following books:")
            for book in member.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{member.name} has not borrowed any books.")
            

    elif choice == "4":  # Exit the library system
       print("Exiting the library system.")
    break  # This exits the loop and terminates the program
