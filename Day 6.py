T = int(input())
words = ''
even_word = ''
odd_word = ''
e = True
for n in range (0, T):
    if e:
        words += input()
        e = False
    else:
        words += ' ' + input()
test = words.split(' ')
for word in test:
    even_word = ''
    odd_word = ''
    even = True
    for l in word:
        if even:
            even_word += l
            even = False
        else:
            odd_word += l
            even = True
    print(even_word, odd_word)


