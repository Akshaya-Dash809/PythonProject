# Function to reverse the order of words
def reverse_word_order(st):
    words=string.split()
    reverse_words=' '.join(reversed(words))
    return reverse_words

# Function to reverse each word in the string
def reverse_each_word(st):
    words=string.split()
    reversed_each_word= ' '.join([word[::-1] for word in words])
    return reversed_each_word

string="Akshaya Kumar"
print(reverse_word_order(string))
print(reverse_each_word(string))




# Explanation:
# reverse_word_order function:
# Splits the string into words using split().
# Reverses the list of words with reversed().
# Joins the reversed list of words with ' '.join().
# reverse_each_word function:
#
# Splits the string into words.
# Reverses each word using Python’s slicing method [::-1].
# Joins the reversed words back into a string.