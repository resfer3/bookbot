# BookBot

def count_words(txt):
  counter = 0
  words_split = txt.split()
  for word in words_split:
    counter+=1
  return counter

def count_non_duplicate_chars(txt):
  # get rid of duplicates
  # TODO
  for char in txt:
  txt_set = set(txt)
  txt_set = str(txt_set).lower()
  new_dict = {}
  for char in txt_set:
    new_dict[char] = 0
  return new_dict

def main():
  with open("books/frankenstein.txt") as f:  
    file_contents = f.read()
    #print(count_words(file_contents))
    print(count_non_duplicate_chars(file_contents))


main()
