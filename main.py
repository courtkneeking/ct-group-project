import pda 

def main():
    input_strings = []
    for i in range(1, 11):
        input_strings.append('a'*i+'b'*i+'$')
    x = pda.PDA()
    for t in input_strings:
        x.pushdown(t)

main()


