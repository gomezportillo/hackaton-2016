from math import sqrt

def split_text(text):
    text_without_spaces = text.replace(" ", "")
    # print(text_without_spaces)
    return text_without_spaces

def set_text(text):
    new_text = set(text)
    return new_text

def count_occurences_and_obtain_ascii(text, setted_text):
    occurences = {}
    for word in setted_text:
        occurences[word] = (text.count(word), ord(word))
    return occurences

def obtain_prime_chars(occurences):
    primes = {}
    for key, value in occurences.items():
        if obtain_prime(value[0]):
            primes[key] = value
    return primes

def obtain_prime(number):
    if number % 2 == 0:
        return False
    for num in range(3, int(number/2)):
        if number % num == 0:
            return False
    return True

def calc_prices(primes):
    prices = {}
    for key, value in primes.items():
        prices[key] = (value[0], obtain_price(value[1], value[0]))
    return prices

def obtain_price(code, occurence):
    return round( (code/1000) * float(occurence), 3)

def print_results(prices):
    total = 0.0
    for key, value in prices.items():
        total += value[1]
        print("{} {} {}€".format(key, value[0], value[1]))
    print("Coste total: {}€".format(total))


file = open("02.in", 'r')
text = split_text(file.read())
setted_text = set_text(text)
occurences = count_occurences_and_obtain_ascii(text, setted_text)
primes = obtain_prime_chars(occurences)
prices = calc_prices(primes)
print_results(prices)
