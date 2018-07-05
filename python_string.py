#create a length of string
def str_len(str1):
    count = 0
    for char in str1:
        count += 1
    return count
print(str_len('sample'))


#python takes a list of words and returns a smallest word in the list
def find_smallest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-2][0]

print(find_smallest_word(['sam', 'sample', 'code']))