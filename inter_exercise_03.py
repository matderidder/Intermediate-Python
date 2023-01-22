def countChar(sent):
    chars = dict()
    sent = sent.lower()
    for char in sent:
        if char not in chars:
            if char != ' ':
                count = sent.count(char)
                chars.update({char: count})
    print(chars)


st = input("Please enter as string: ")
countChar(st)
