from collections import Counter


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    ok = True
    word_dict = Counter()
    magazine_dict = Counter()
    for word in magazine:
        magazine_dict[word] += 1
    for word in note:
        word_dict[word] += 1
    for k, v in word_dict.items():
        if magazine_dict[k] < v:
            ok = False
            break
    if ok:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    checkMagazine(['This', 'is', 'a', 'test'], ['test'])
