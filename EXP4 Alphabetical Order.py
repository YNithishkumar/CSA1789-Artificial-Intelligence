def sort_sentence(sentence):
    words = sentence.split()
    words.sort()
    return " ".join(words)

sentence = input("Enter a sentence: ")
sorted_sentence = sort_sentence(sentence)
print("Sorted sentence:", sorted_sentence)
