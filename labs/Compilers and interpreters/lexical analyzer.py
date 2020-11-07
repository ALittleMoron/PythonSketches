"""
Продолжение лабораторной работы с ДКА, только на этот раз введенная строка
будет проверяться по нескольким ДКА (на каждый тип и операцию
свой автомат со своим набором правил). Сам ДКА будет изменен для того,
чтобы постоянно при запуске программы не вписывать вручную функции перехода
для автомата (когда он 1 - это одно, а когда их 5 - совершенно другое).
Проверяться будет подмножество языка Pascal в виде арифметических выражений
и операции присваивания, поэтому также будет учтен приоритет по операциям:
приравнивание - минимальный приоритет, а умножение и деление - максимальный,
а также скобки, но уже в особом порядке.

"""


from collections import namedtuple
from typing import NoReturn, List, NamedTuple, Tuple


class DFA:
    def __init__(self, name, rules, start_accept):
        self.name = name
        self.rules = rules
        self.START_STATE, self.ACCEPT_STATES = self.set_start_accept(*start_accept)
        self.CURRENT_STATE = None
        self.populate_transition_function()


    def set_start_accept(self, start_state: str, accept_state: str):
        if not (start_state in self.rules and accept_state in self.rules):
            state = list(self.rules.keys())[0]
            start_state, accept_state = state, state
            print(f"\nCтартовое состояние и/или состояние допуска были введены неправильно. Они будут изменены на {state} и {state}\n")
        return start_state, accept_state


    def populate_transition_function(self):
        print(f'\n{self.name}:')
        print("\nПЕРЕХОДНАЯ ФУНКЦИЯ Q X SIGMA -> Q")
        print("ТЕКУЩЕЕ СОСТОЯНИЕ\tАЛФАВИТ ВВОДА\tСЛЕДУЮЩЕЕ СОСТОЯНИЕ")
        for key, dict_value in self.rules.items():
            for input_alphabet, transition_state in dict_value.items():
                print("{}\t\t{}\t\t{}".format(key, input_alphabet, transition_state))


    def run_state_transition(self, input_symbol):
        if (self.CURRENT_STATE == 'REJECT'):
            return False
        print("ТЕКУЩЕЕ СОСТОЯНИЕ : {}\tАЛФАВИТ ВВОДА : {}\t СЛЕДУЮЩЕЕ СОСТОЯНИЕ : {}".format(self.CURRENT_STATE, input_symbol, self.rules[self.CURRENT_STATE][input_symbol]))
        self.CURRENT_STATE = self.rules[self.CURRENT_STATE][input_symbol]
        return self.CURRENT_STATE


    def check_if_accept(self):
        if self.CURRENT_STATE in self.ACCEPT_STATES:
            return True
        else:
            return False


    def run_machine(self, in_string):
        self.CURRENT_STATE = self.START_STATE
        for ele in in_string:
            check_state = self.run_state_transition(ele)
            if (check_state == 'REJECT'):
                return False
        return self.check_if_accept()


class AnalyzingInfo(NamedTuple):
    parsed_type: str    # 'addition operator', 'subtraction operator' и т.д.
    position: str       # '0-5', '6-12' и т.д.
    value: str          # 'abc25', '25', '0.25' и т.д.



class Analyzer:
    _PARSED_TYPES = {
        '+': 'addition operator',
        '-': 'subtraction operator',
        ':=': 'assignment operator',
        '*': 'multiplication operator',
        '/': 'division operator',
        '(': 'open parenthesis',
        ')': 'close parenthesis',
        'int': 'integer number',
        'float': 'float number'
    }
    
    
    def __init__(self, data) -> NoReturn:
        pass

    
    def check_on_DFA(self, str_part: str) -> bool:
        pass


    def analyzing(self, input_string: str) -> bool:
        pass


def main():
    pass


if __name__ == "__main__":
    rules = {
    'q0': {
        '0': 'q1',
        '1': 'q0'
    },
    'q1': {
        '0': 'q2',
        '1': 'q0'
    },
    'q2': {
        '0': 'q2',
        '1': 'q0'
    }
}
    a = DFA('ПАРСЕР ПЕРЕМЕННЫХ', rules, ['q0', 'q4'])
    print(a.run_machine('01101'))