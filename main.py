from stats import count_words

def main():
  file = "books/frankenstein.txt"
  # print(get_book_text("books/frankenstein.txt"))
  count = count_words(file)
  print(f"{count} words found in the document")
  
def get_book_text(book):
  with open(book) as file:
    book_contents = file.read()

  return book_contents


main()
