def words(word):
    word1 = word[-3:]
    if word1 != "ing":
        print("adding 'ing' = ", word+"ing")
    else:
        print("adding 'ly' = ", word+"ly")


a = input("enter the word:")
words(a)
