def count_words(book):
  book_str = ""
  with open(book) as file:
    book_contents = file.read()
    book_str = book_contents.split()
    
  return len(book_str)

def count_chars(book):
  chars_dict = {}
  with open(book) as file:
    book_contents = file.read()
    
