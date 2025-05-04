from stats import *
import sys

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  file = sys.argv[1] 
  # print(get_book_text("books/frankenstein.txt"))
  count = count_words(file)
  letter_count = count_chars(file)
  # print(f"{letter_count}")

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {file}...")
  print("----------- Word Count ----------")
  print(f"Found {count} total words")
  print("--------- Character Count -------")

  sorted_list = sorted_chars(letter_count)
  for dict in sorted_list:
    if dict["char"].isalpha():
      print(f"{dict["char"]}: {dict["num"]}")


  # for k in letter_count:
    # print(f"{k}: {letter_count[k]}")
  

main()
