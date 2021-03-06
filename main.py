import pda 

def main():
    print("Input custom string?")
    run = pda.PDA()
    answer = input("Type 'Y' or 'N': ").upper()
    if answer == 'Y':
        while answer == 'Y':
            print("This program accepts a string input for a pushdown automata")
            string = input("String input (don't forget the '$'): ").lower()
            run.pushdown(string)
            print('\n New string input?')
            answer = input("Type 'Y' or 'N': ").upper()
    else:
        print("Here are some example strings:")
        input_strings = []
        for i in range(1, 11):
            input_strings.append('a'*i+'b'*i+'$')
        for t in input_strings:
            run.pushdown(t)

main()
print("\nDone!")


