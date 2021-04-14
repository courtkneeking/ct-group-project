from collections import deque

class PDA:
    def __init__(self):
        self.grammar = dict(
            states = ['Q', 'P', 'F'],
            sigma = ['a', 'b'],
            nonterminals = ['S'], 
            initial_state = 'Q',
            final_states = ['F'], 
            rules = dict(
                'Qee' : 'QeS',
            )
        )
    def pushdown(self, input_string):
        stack = ""
        input_top = ""
        current_state = initial_state 
        while current_state not in final_states: 
            try:
                next_state = rules[current_state+input_string[-1]+stack[-1]]
                if 
            except:
                print("string not accepted")
        print('string accepted')


