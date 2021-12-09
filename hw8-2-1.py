# Yongdong Xi
def count_odds(lst1):
    total = 0
    for x in lst1:
        if x % 2 == 1:
            total += 1
        else:
            total += 0
    return total
    

lst = [1, 3, 5, 7, 9]
print(count_odds(lst))
