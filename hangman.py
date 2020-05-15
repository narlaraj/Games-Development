from random import randint
import linecache

processed = []
text = ""
guess = ""


# replace_char(3,'K')s
# --> abc K edf

def replace_char(pos, ch):
    global guess
    guess = guess[:pos] + ch + guess[pos + 1:]


def find_and_replace(ch):
    global text
    found = False
    for i in range(len(text)):
        if text[i] == ch:
            replace_char(i, ch)
            found = True
    return found


def init_word(pos):
    global text
    global guess

    text = linecache.getline('hangman.txt', pos)
    text = text[:-1]
    guess = '_' * len(text)


def guess_word():
    global text
    global guess
    cnt = 0
    while cnt < 7 and text != guess:
        print(f"Guess : {guess}")
        gs = input('Enter the guess character')
        rs = find_and_replace(gs)
        if rs == False:
            cnt += 1

    if text != guess:
        return False
    else:
        return True


def main():
    count = 1
    while True:
        rint = randint(0, 50 - 1)
        while rint in processed:
            rint = randint(0, 50 - 1)
        processed.append(rint)
        init_word(rint)
        res = guess_word()
        if res == True:
            print(f"Guess : {guess}")
            count += 1
        else:
            print("Sorry time up")
            print(f"The wor is : {text}")

        if count == 5:
            print('You won 5 times, Congratulations!!!')
            break
        cont = input("Want to play again(y/n)?")
        if (cont == 'n' or cont == 'N'):
            break


main()
