def repeated_string(n, s):

    # Returns number of 'a' characters in a string n length string formed by repetition of s (whole and partially)

    rep = s.count('a')
    rest = n % len(s)

    if rest == 0:
        result = rep * (n/len(s))
    else:
        result = rep * (n//len(s)) + s[:rest-1].count('a')

    return int(result)

if __name__ == '__main__':
    n = 685118368975
    s = 'ojowrdcpavatfacuunxycyrmpbkvaxyrsgquwehhurnicgicmrpmgegftjszgvsgqavcrvdtsxlkxjpqtlnkjuyraknwxmnthfpt'
    print(repeated_string(n, s))