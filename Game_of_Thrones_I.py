def gameOfThrones(s):

    # Answers if it is possible for a string to be transformed in a palindrome

    odds_counter = 0
    for v in set(s):
        if s.count(v) % 2 != 0:
            odds_counter += 1

    if odds_counter == 1 or odds_counter == 0:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':

    s0 = 'aaabbbb'
    s1 = 'cdefghmnopqrstuvw'
    s2 = 'cdcdcdcdeeeef'
    print(gameOfThrones(s0))
