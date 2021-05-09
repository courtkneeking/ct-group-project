class PDA:
    def __init__(self):
        self.grammar = dict(
            states = ['p', 'q', 'qa', 'qb', 'q$'],
            sigma = ['a', 'b', '$'],
            nonterminals = ['S'], 
            initial_state = 'p',
            final_states = ['q$'], 
            rules = {
                ('p','') : ('q','S'), 
                ('q','a') : ('qa',''),
                ('qa','a') : ('q',''),
                ('q','b') : ('qb', ''),
                ('qb','b') : ('q',''),
                ('q','$') : ('q$', ''),
                ('qa','S') : ('qa', 'aSb'),
                ('qb','S') : ('qb', '')
            }
        )
    def pushdown(self, input_string):
        try:
            state, stack, step = self.grammar['initial_state'], '', 0
            print('step'.center(5), 'state'.center(10), 'input'.center(25), 'stack'.center(25))
            print(str(step).center(5), state.center(10), input_string.rjust(25), 'e'.rjust(25))
            while input_string: 
                step+=1
                #if state is q read input_string, if state is qx read stack
                trans = self.grammar['rules'][(state, '' if state == 'p' else input_string[0] if state == 'q' else stack[0])]
                #decrement input_string if q
                input_string = input_string[1:] if state == 'q' else input_string 
                #decrement/transform stack if qx
                stack = trans[1] + (stack[1:] if state[1:] else stack)
                #update state 
                state = trans[0]
                print(str(step).center(5), state.center(10), input_string.rjust(25) if input_string else 'e'.rjust(25), stack.rjust(25) if stack else 'e'.rjust(25)) 
            if state in self.grammar['final_states']: print('Accepted')
            else: print('Nope')
        except:
            print("PDA failed to consume. Not a viable language.")



