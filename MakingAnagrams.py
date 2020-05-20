def makingAnagrams(s1, s2):

    # Calculates the min nb of deletes in both string parameters to have the same characters and same number for each

    common = set(s1 + s2)
    counter = 0
    for val in common:
        counter += abs(s1.count(val) - s2.count(val))

    return counter


def makingAnagrams2(s1, s2):

    common = set(s1) & set(s2)
    counter = 0

    for val in common:
        counter += min(s1.count(val), s2.count(val))

    return len(s1) + len(s2) - 2 * counter


if __name__ == '__main__':
    s0 = 'absdjkvuahdakejfnfauhdsaavasdlkj'
    s00 = 'djfladfhiawasdkjvalskufhafablsdkashlahdfa'
    print(makingAnagrams(s0, s00))
    print(makingAnagrams2(s0, s00))
