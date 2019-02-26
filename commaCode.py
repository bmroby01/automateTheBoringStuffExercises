spam = ['apples', 'bananas', 'tofu', 'cats']
ham = ['apples', 'bananas', 'tofu', 'cats', 'dogs', 'pens', 'fruit', 'phones']

def makeString(a):
    s = ''
    for i in range(len(a)):
        if i > 0:
            if i == len(a) - 1:
                s = s + ' snd '
            else:
                s = s + ', '
        s = s + a[i];
    print(s)

makeString(ham)
