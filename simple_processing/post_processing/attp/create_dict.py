import pickle
import numpy as np

from utils import no_accent_vietnamese, load_yaml, abs_path


if __name__ == '__main__':
    testing_center_list_path = 'testing_center_list.yaml'
    testing_center_list = load_yaml(abs_path(testing_center_list_path)).get('testing_center')

    dict_word = {}
    for idx, testing_center in enumerate(testing_center_list):
        testing_center = no_accent_vietnamese(testing_center).lower()
        testing_center = "".join(c for c in testing_center if c == ' ' or c.isalnum())
        words = testing_center.split(' ')
        for word in words:
            if word not in dict_word:
                dict_word[word] = [idx]
            else:
                dict_word[word].append(idx)

        for i in range(len(words) - 1):
            word = words[i] + words[i + 1]
            if word not in dict_word:
                dict_word[word] = [idx]
            else:
                dict_word[word].append(idx)

    for word in dict_word.keys():
        dict_word[word] = np.unique(dict_word[word])

    testing_center_words_file = open("testing_center_words.pkl", "wb")
    pickle.dump(dict_word, testing_center_words_file)
    testing_center_words_file.close()

    testing_center_words_file = open("testing_center_words.pkl", "rb")
    testing_center_words = pickle.load(testing_center_words_file)
