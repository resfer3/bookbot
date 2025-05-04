# count how many words are in the text
def count_words(book):
  book_str = ""
  with open(book) as file:
    book_contents = file.read()
    book_str = book_contents.split()
    
  return len(book_str)

# count characters of book
def count_chars(book):
  chars_dict = {}
  with open(book) as file:
    book_contents = file.read()
    for letter in book_contents:
        turn_to_lower = letter.lower()
        if turn_to_lower in chars_dict:
            chars_dict[turn_to_lower] += 1
        else: 
            chars_dict[turn_to_lower] = 1
        
        # print(turn_to_lower)

    return chars_dict

# return a sorted list of dictionaries
def sorted_chars(dict):
    list_chars = []
    for k in dict:
        tmp_dict = {}
        tmp_dict["char"] = k
        tmp_dict["num"] = dict[k]
        list_chars.append(tmp_dict)
    return sorted(list_chars,reverse=True, key=lambda i:i["num"])


# get full book text
def get_book_text(book):
  with open(book) as file:
    book_contents = file.read()

  return book_contents

   
