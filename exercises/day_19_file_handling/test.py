
import re
def most_repeated_words():
    try:
        with open ("D:/python-30day-challenge-collab/exercises/data/romeo_and_juliet.txt", 'r', encoding='utf-8') as f:
            file_content = f.read()
        repeated_words = {}
        words = re.findall(r'\b\w+\b', file_content.lower())
        for word in words:
            if word in repeated_words:
                repeated_words[word] += 1
            else:
                repeated_words[word] = 1
        repeated_words_sorted = sorted(repeated_words.items(), key=lambda x:x[1], reverse=True)[:10]
        return repeated_words_sorted

    except FileNotFoundError as e:
        print(f"An error occurred with romeo_and_juliet.txt: {e}")



print(most_repeated_words())