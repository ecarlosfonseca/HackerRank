def loveLetter(s):

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    mid = len(s)//2
    left = []
    right = []
    for i in s[:mid]:
        left.append(alphabet.index(i))
    for j in s[-1:-mid-1:-1]:
        right.append(alphabet.index(j))

    soma = 0
    for i in range(len(left)):
        soma += abs(left[i] - right[i])

    return soma

if __name__ == '__main__':
    s0 = 'abc'
    s1 = 'abcba'
    s2 = 'abcd'
    print(loveLetter(s2))