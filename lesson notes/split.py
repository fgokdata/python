sentence = input("Write me a sentence:")
words = sentence.split()
longest = 0
i = 0
while i < len(words):
    if len(words[i]) > longest:
        longest = len(words[i])
    i += 1
    
print("The lenght of the longest word is:", longest)
        