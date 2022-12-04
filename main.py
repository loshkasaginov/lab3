import re


alph="abccba cbab cbabcab cabcba bcabac bcabacbabc bacbcabcab acbabacb bcabcacbac bcacbab acbbbacccbac"


def main():
    alph_splited=alph.split()

    for word in alph_splited:
        match = re.sub(r'ac','.',word)
        if match:
            if 'a' not in match:
                print(word)


if __name__ == '__main__':
    main()
