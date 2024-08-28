class library:
    def __init__(self):
        self.books ={}
        def add_book(self, title, author,isbn, genre,availability = True):
        if isbn in self.books:
            print(f"book with isbn {isbn} already exists")
             else:
        self.books[isbn] = {
             'Title': title,
                'Author': author,
                 'Genre': genre,
                'Availability': availability
            }
            print(f"Book'{title}'added successfully")
            def update_book_details(self, isbn, title=None, author=None, genre=None, availability=None):
if isbn in self.books:
    if title:
        self.books[isbn]['Title'] = title
    if author:
            self.books[isbn]['Author'] = author
            if genre:
   self.books[isbn]['Genre'] = genre
            if availability is not None:
        self.books[isbn]['Availability'] = availability
            print(f"Details for ISBN {isbn} updated successfully")
        else:
        print(f"No book found with isbn {isbn}")
        
 def search_by_isbn(self, isbn):
       
        if isbn in self.books:
            book = self.books[isbn]
 print(f"Book Found: {book}")
            return book
        else:
            print(f"No book found with isbn {isbn}.")
            return None

 def generat_genre_report(self)
 genre_report={}
 for book in self.books.values():
     if book ['availability']:
         genre =book['genre']
         if genre in genre_report:
             genre_report[genre].apend(book['title'])
             if genere_report:
                 for genre, titles in genre_report.items():
                     print (f"genre: {genre}")
                     for title in titles:
                         print (f" {titles})
                                else:
                                    print ("not found")
                                   
                                    

















































































       

    
        

   

    


