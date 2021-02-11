def distance(word1: str, word2: str) -> int:
    '''Differences between words'''
    diff_count = 0
    for ctr in range(len(word1)):
        #print(f"word1 {word1}, word2 {word2}")
        if word1[ctr] != word2[ctr]:
            diff_count += 1
    return diff_count

def diff_by_one_all(word, all_words, used_words):
    '''Find all words that differ by 1 letter'''
    one_diff_words = []
    for test_word in all_words:
        if test_word not in used_words:
            if distance(word, test_word) == 1:
                print(f"new word {test_word}")
                one_diff_words.append(test_word)
                used_words.append(test_word)
                print(one_diff_words)
    return one_diff_words

word = 'stone'
all_words = ['atone', 'store', 'hello']
used_words = []
new_set = diff_by_one_all(word, all_words, used_words)
print(new_set)
