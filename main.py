import sys
from stats import count_words, count_char_instances, sort_dict


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_texts = get_book_text(sys.argv[1])
        book_num_words = count_words(book_texts)
        book_chars_instances = count_char_instances(book_texts)
        sorted_chars_instances = sort_dict(book_chars_instances)

        print(book_texts)
        print(f"{book_num_words} words found in the document")
        print(book_chars_instances)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {book_num_words} total words")
        print("--------- Character Count -------")

        for char_dict in sorted_chars_instances:
            if char_dict["char"].isalpha():
                print(f"{char_dict["char"]}: {char_dict["num"]}")

        print("============= END ===============")


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


main()
