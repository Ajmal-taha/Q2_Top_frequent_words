FILE_PATH = "document.txt"

my_dict = {}

with open(FILE_PATH, 'r') as f:
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

for word, count in top_10:
    print(word, count)