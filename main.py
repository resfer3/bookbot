# BookBot

def count_words(txt):
  counter = 0
  words_split = txt.split()
  for word in words_split:
    counter+=1
  return counter

def count_non_duplicate_chars(txt):
  char_dict = {}
  storage = ""
  for char in txt:
    if char.isalpha():
      storage = char.lower()
    else:
      continue
    if storage in char_dict:
      char_dict[storage] += 1
    else:
      char_dict[storage] = 1
  return char_dict


def main():
  with open("books/frankenstein.txt") as f:  
    file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document")
    print()

    char_dict = count_non_duplicate_chars(file_contents)
    for key in char_dict:
      print(f"The '{key}' character was found {char_dict[key]} times")
    print("--- End report ---")


main()
