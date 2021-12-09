# Yongdong Xi
def three_letter_words(wordlst):
    total = 0
    for x in wordlst:
        if int(len(x)) == 3:
            total += 1
        else:
            total += 0
    return total


print(three_letter_words(["cat", "bat", "apple"]))