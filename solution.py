from dotenv import load_dotenv()
import os

load_dotenv()

file_path = os.getenv("FILE_PATH")

def top_freq(file_path):
    my_dict = {}

    with open(file_path, 'r') as f:
        word = f.readline()
        while(word):
            word = word.strip()
            if word in my_dict:
                my_dict[word] += 1
            else:
                my_dict[word] = 1

            word = f.readline()

    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

    top_10 = list(sorted_dict.items())[:10]
    return top_10

if __name__ == "__main__":
    top_10 = top_freq(file_path)
    for word, count in top_10:
        print(word, count)