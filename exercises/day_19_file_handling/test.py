import re

def find_most_common_words(file_name, numbers_to_display):
    try:
        with open(f"D:\python-30day-challenge-collab\exercises\data/{file_name}", 'r', encoding='utf-8') as f:
            file = f.read()
            words = re.findall(r'\b\w+\b', file.lower())
            word_dictionary = {}
            word_list = []
            for word in words:
                if word in word_dictionary:
                    word_dictionary[word] += 1
                else:
                    word_dictionary[word] = 1
            most_common_words = sorted(word_dictionary.items(), key=lambda x: x[1], reverse=True)[:numbers_to_display]
            for key, value in most_common_words:
                word_list.append((key, value))
            return word_list

    except FileNotFoundError as e:
        print(f"An error occurred: {e}")
    except TypeError as e:
        print(f"An error occurred: {e}")







if __name__ == "__main__":
    print(find_most_common_words("donald_speech.txt", 10))