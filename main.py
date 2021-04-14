import pda 

def main():
    input_strings = []
    for i in range(1, 11):
        input_strings.append('a'*i+'b'*i+'$')
    test_one = input_strings[5]
    x = PDA()
    x.pushdown(test_one)

main()


