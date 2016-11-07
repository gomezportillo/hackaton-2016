a = {'{':1, '(':2, '[':3 }
b = {1:'}', 2:')', 3:']' }

def extract_tokens(word):
    letters = list(word)
    check_balance(letters)

def check_balance(letters):
    stack = []
    for letter in letters:
        if letter in a:
            stack.append(b[a[letter]])
        elif letter in list(b.values()):
            if len(stack) == 0:
                print("No balanceada")
                return -1
            elif letter == stack[-1]:
                stack.pop()
            else:
                print("No balanceada")
                return -1
    if len(stack) > 0:
        print("No balanceada")
        return -1
    else:
        print("Balanceada")
        return 0

text = open("22.in", 'r').read().split("\n")[:-1]
for i in text:
    # print(i)
    extract_tokens(i)
