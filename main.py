from stats import *

def main():
  file = "books/frankenstein.txt"
  # print(get_book_text("books/frankenstein.txt"))
  count = count_words(file)
  print(f"{count} words found in the document")
  letter_count = count_chars(file)
  print(f"{letter_count}")
  

main()
