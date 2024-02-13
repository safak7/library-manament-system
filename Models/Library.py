class Library:

    def __init__(self,path="books.txt"):
        self.path=path
        try:
            self.file=open(self.path ,'+a')
        except:
            print("Cannot open the file")


    def __del__(self):
        try: 
            self.file.close()
        except:
            print("Cannot close the file")
    
    def add_book(self):
        try:
            title = input("Title : ")
            author = input("Author : ")
            release_year = input("Release Year : ")
            num_pages = input("Number of Pages : ")

            book = f"{title},{author},{release_year},{num_pages}\n"

            self.file.write(book)
            print(f"The book '{title}' has been successfully added to the file.")
        except :
            print("ERROR while adding book")

    def list_all_books(self):
        try:
            self.file.seek(0)  
            books = self.file.read().splitlines()
            if not books:
                print("No books in the library.")
            else:
                print("***List of all books***")
                for book in books:
                    title, author, release_year, num_pages = book.split(',')
                    print(f"Title: {title}, Author: {author}")
        except :
            print("ERROR while listing all books")

        
    
    def remove_book(self):
        try:
            book_to_remove = input("Enter the title a book to remove: ")

            self.file.seek(0)
            books = self.file.read().splitlines()
            self.file.seek(0)
            self.file.truncate()  

            is_removed = False
            for book in books:
                if book_to_remove not in book:
                    self.file.write(book + '\n')
                else:
                    is_removed = True

          

            if is_removed:
                print(f"The book '{book_to_remove}' has been successfully removed.")
            else:
                print(f"No book with the title '{book_to_remove}' found.")
        except:
            print("ERROR while removing book")


    
