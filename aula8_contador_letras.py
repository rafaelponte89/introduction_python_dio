def letter_counter(words_list):
    counter = []
    for x in words_list:
        amount = len(x)
        counter.append(amount)
    return counter

if __name__ == '__main__':
    animal_list = ['cat','dog','fish']
    print(letter_counter(animal_list))