def comma_code(items):

    item_len = len(items)

    if item_len == 0:
        return ''
    elif item_len == 1:
        return items[0]

    return ', '.join(items[:-1]) + ', and ' + items[-1]

if __name__ == '__main__':

    spam = ['apples','bananas','tofu','cats']
    spam1 = []
    spam2 = ['oranges']
    print(comma_code(spam))
    print(comma_code(spam1))
    print(comma_code(spam2))

