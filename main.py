import sys
from stats import get_num_words
from stats import get_num_chars
from stats import sort_char

def get_book_text(filepath):
        with open(filepath) as f:
            file_contents = f.read()
            return file_contents
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        try: 
            text = get_book_text(sys.argv[1])
        except FileNotFoundError as f:
             print(f)
             sys.exit(74)
        count = get_num_chars(text)
        ordered_count = sort_char(count)
        print("====")
        print(f"Found {get_num_words(text)} total words")
        print("====")
        # print(f"Counts of every character: {count}")
        print("Counts of every character in descending order")
        for dictionary in ordered_count:
            if dictionary["char"].isalpha():
                print(f"{dictionary["char"]}: {dictionary["num"]}")
        print("===")
main()
    