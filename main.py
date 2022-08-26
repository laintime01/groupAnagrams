# This is a grouping anagrams programs using python by hao
from collections import defaultdict


def group_words(words):
    default_dic = defaultdict(list)
    for word in words:
        sorted_word = "".join(sorted(word))
        default_dic[sorted_word].append(word)
    print(default_dic.values())
    return default_dic.values()


some_words = ["tab", "eat", "abt", "bat", "ate", "arc", "car", "tape", "pat"]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    group_words(some_words)
