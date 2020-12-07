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


import string
import sys
from typing import NoReturn, List, NamedTuple, Tuple, Dict, Union, Iterable
from prettytable import PrettyTable


class ParseError(Exception):
    """ Исключение, связанное с тем, что программа не смогла распарсить строку. """
    pass


class DFA:
    def __init__(self, name, rules, start_accept: Union[List[str], Tuple[str]], show_on_create: bool=False) -> NoReturn:
        self.name = name
        self.rules = rules
        self.START_STATE, self.ACCEPT_STATES = self.set_start_accept(*start_accept)
        self.CURRENT_STATE = None
        
        if show_on_create:
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


    def run_state_transition(self, input_symbol, show_on_process):
        if (self.CURRENT_STATE == 'REJECT') or (self.CURRENT_STATE == 'SUCCESS'):
            return self.CURRENT_STATE
        if show_on_process:
            print("ТЕКУЩЕЕ СОСТОЯНИЕ : {}\tАЛФАВИТ ВВОДА : {}\t СЛЕДУЮЩЕЕ СОСТОЯНИЕ : {}".format(self.CURRENT_STATE, input_symbol, self.rules[self.CURRENT_STATE][input_symbol]))
        self.CURRENT_STATE = self.rules[self.CURRENT_STATE][input_symbol]
        return self.CURRENT_STATE


    def check_if_accept(self):
        if self.CURRENT_STATE in self.ACCEPT_STATES:
            return True
        else:
            return False


    def run_machine(self, in_string, show_on_process: bool=True):
        self.CURRENT_STATE = self.START_STATE
        for ele in in_string:
            check_state = self.run_state_transition(ele, show_on_process)
            if (check_state == 'REJECT'):
                return False
            if (check_state == 'SUCCESS'):
                return True
        return self.check_if_accept()


class AnalyzingInfo(NamedTuple):
    """ Именнованный кортеж с аннотацией типов. """
    parsed_type: str    # 'addition operator', 'subtraction operator' и т.д.
    position: str       # '0-5', '6-12' и т.д.
    value: str          # 'abc25', '25', '0.25' и т.д.


class Analyzer:
    """ Непосредственный класс-анализатор строки подмножества ЯП Pascal. """
    _PARSED_TYPES = {
        '+': 'addition operator',
        '-': 'subtraction operator',
        ':=': 'assignment operator',
        '*': 'multiplication operator',
        '/': 'division operator',
        '%': 'modulus operator',
        '(': 'open parenthesis',
        ')': 'close parenthesis',
        'int': 'integer number',
        'float': 'float number',
        'var': 'variable'
    }
    
    
    def __init__(self, data: Union[List[DFA], Tuple[DFA]]) -> None:
        self.information = []
        try:
            self.data = [
                self.assignment_operator_analyzer,
                self.int_analyzer,
                self.float_analyzer,
                self.operator_analyzer,
                self.variable_analyzer,
                self.open_parenthesis_analyzer,
                self.close_parenthesis_analyzer] = data
        except KeyError as e:
            print(e)
            sys.exit('\nНе то количество анализаторов')

    
    def _check_on_DFA(self, str_part: str, dfa: DFA, show_on_process: bool=True) -> bool:
        if show_on_process:
            print('\n' + dfa.name, str_part)
        return dfa.run_machine(str_part, show_on_process)


    def _type_parser(self, type_parse_string: str) -> str:
        if type_parse_string in self._PARSED_TYPES:
            return self._PARSED_TYPES[type_parse_string]
        else:
            if self._check_on_DFA(type_parse_string, self.variable_analyzer, show_on_process=False):
                return self._PARSED_TYPES['var']
            if self._check_on_DFA(type_parse_string, self.int_analyzer, show_on_process=False):
                return self._PARSED_TYPES['int']
            if self._check_on_DFA(type_parse_string, self.float_analyzer, show_on_process=False):
                return self._PARSED_TYPES['float']
            if self._check_on_DFA(type_parse_string, self.assignment_operator_analyzer, show_on_process=False):
                return self._PARSED_TYPES[':=']
            return 'Not recognized'


    def _normalize_right_part(self, right_string_part: str, interval: Tuple[int]) -> Iterable:
        """ Преобразует правую часть введенной строки. """
        shift = interval[0]
        left_pos = 0
        info = []

        if right_string_part.count('(') != right_string_part.count(')'):
            return ['Not recognized', '{}-{}'.format(*interval), right_string_part]
        if not any([True if x in right_string_part else False for x in '()*+-/%']):
            return [self._type_parser(right_string_part), '{}-{}'.format(*interval), right_string_part]
        
        for pos in range(1, len(right_string_part)):
            for dfa in self.data:
                if self._check_on_DFA(right_string_part[left_pos:pos], dfa, False):
                    info.append(
                        [
                            self._type_parser(right_string_part[left_pos:pos]),
                            '{}-{}'.format(left_pos+shift, pos+shift) if left_pos != pos else '{}'.format(pos+shift),
                            right_string_part[left_pos:pos]
                        ])
                    left_pos = pos
        return info

    def _normalize_data_from_string(self, input_string: str) -> Iterable:
        """ Преобразует введенную строку в кортеж из parsed_types, positions, values строк. """
        values = input_string.partition(':=')

        parsed_types = (self._type_parser(value.strip()) for value in values)
        if len(values[1]) == 1:
            raise ParseError('\nВ строке нет оператора присваивания.')
        
        positions = []
        left_pos = 0
        for value in values:
            positions.append(f'{left_pos}-{left_pos + len(value) - 1}')
            left_pos += len(value)
        
        right_part = self._normalize_right_part(values[2], positions[2][0])
        for cur_data, ri_part in zip([parsed_types, positions, values], right_part):
            cur_data[0] += ri_part[0]
            cur_data[1] += ri_part[1]
            cur_data[2] += ri_part[2]
            return cur_data


    def final_validation(self) -> bool:
        """ Валидация итоговых данных.
        Возвращает True, если соблюдена структура, иначе False. """
        if len(self.information) < 3:
            return False
        if self.information[0].parsed_type != 'variable' and self.information[1].parsed_type != 'assignment operator':
            return False
        for info in self.information:
            if info.parsed_type == 'Not recognized':
                return False
        return True


    def analyzing(self, input_string: str) -> Tuple[List[AnalyzingInfo], bool]:
        """ 
        ядро всего кода. Здесь анализируется введенная строка и заполняется
        список с информацией по каждой распаршенной части этой строки.
        """
        normalized_data = self._normalize_data_from_string(input_string)

        for parsed_type, position, string in normalized_data:
            for dfa in self.data:
                if self._check_on_DFA(string, dfa):
                    self.information.append(AnalyzingInfo(
                        parsed_type= parsed_type,
                        position=position,
                        value=string))
        return self.information, self.final_validation()


    def pretty_table_print(self, final_valid_res: bool) -> PrettyTable:
        table = PrettyTable(["Тип лексемы", "Позиция в строке", "Значение"])
        for info in self.information:
            table.add_row(info)
        print('\n\n')
        print(table, '\n\n+--- Итог: ---+')
        print('Строка прошла проверку!' if final_valid_res else 'Строка НЕ прошла проверку!')



def all_dfa() -> List[DFA]:
    return [
        DFA(*assignment_operator_rules()),
        DFA(*integer_rules()),
        DFA(*float_rules()),
        DFA(*operator_rules()),
        DFA(*variable_rules()),
        DFA(*open_parenthesis_rules()),
        DFA(*close_parenthesis_rules())
        ]


def assignment_operator_rules() -> Tuple[str, dict, list]:
    """ Возвращает правила для формирования ДКА для валидации оператора присваивания. """
    return ('Проверка оператора присваивания: ', {
        'q0': {
            **dict_of_letters(),
            **dict_of_letters(upper_case=True),
            **dict_of_digits(),
            **dict_of_special_symbols(),
            **{' ': 'q0', ':': 'q1'}
        },
        'q1':{
            **dict_of_letters(),
            **dict_of_letters(upper_case=True),
            **dict_of_digits(),
            **dict_of_special_symbols(),
            **{' ': 'REJECT', "=": 'q1'}
        }}, ['q0', 'q1'])


def variable_rules() -> Tuple[str, dict, list]:
    """ Возвращает правила для формирования ДКА для валидации названия переменной. """
    return ('Проверка переменной: ' , {
        'q0': {
            **dict_of_letters(state='q1'),
            **dict_of_letters(state='q1', upper_case=True),
            **dict_of_digits(),
            **dict_of_special_symbols(),
            **{' ': 'q0'}},
        'q1': {
            **dict_of_letters(state='q1'),
            **dict_of_letters(state='q1', upper_case=True),
            **dict_of_digits(state='q1'),
            **dict_of_special_symbols(),
            **{' ': 'REJECT', '_': 'q1'} }}, ['q0', 'q1'])


def operator_rules() -> Tuple[str, dict, list]:
    """ Возвращает правила для формирования ДКА для валидации оператора. """
    return ('Проверка операторов: ', {
        'q0': {
            **dict_of_letters(),
            **dict_of_letters(upper_case=True),
            **dict_of_digits(),
            **dict_of_special_symbols(),
            **{' ': 'q0', '*': 'q0', '+': 'q0', '-': 'REJECT', '/': 'q0', '%': 'q0'}
        }}, ['q0', 'q0'])


def integer_rules() -> Tuple[str, dict, list]:
    """ Возвращает правила для формирования ДКА для валидации числа (int). """
    return ('Проверка числа (int): ', {
        'q0': {
            **dict_of_letters(),
            **dict_of_letters(upper_case=True),
            **dict_of_digits(state='q1'),
            **dict_of_special_symbols(),
            **{' ': 'q0'}
        },
        'q1': {
            **dict_of_letters(),
            **dict_of_letters(upper_case=True),
            **dict_of_digits(state='q1'),
            **dict_of_special_symbols(),
            **{' ': 'q1'}
        }}, ['q0', 'q1'])


def float_rules() -> Tuple[str, dict, list]:
    """ Возвращает правила для формирования ДКА для валидации числа (float). """
    return ('Проверка числа (float): ', {
        'q0': {
            **dict_of_letters(),
            **dict_of_letters(upper_case=True),
            **dict_of_digits(state='q1'),
            **dict_of_special_symbols(),
            **{' ': 'q0'}
        },
        'q1': {
            **dict_of_letters(),
            **dict_of_letters(upper_case=True),
            **dict_of_digits(state='q1'),
            **dict_of_special_symbols(),
            **{'.': 'q2', ' ': 'REJECT'}
        },
        'q2':{
            **dict_of_letters(),
            **dict_of_letters(upper_case=True),
            **dict_of_digits(state='q2'),
            **dict_of_special_symbols(),
            **{' ': 'REJECT'}
        }}, ['q0', 'q2'])


def open_parenthesis_rules() -> Tuple[str, dict, list]:
    """ Возвращает правила для формирования ДКА для валидации открывающейся строки. """
    return ('Проверка числа (int): ', {
        'q0': {
            **dict_of_letters(),
            **dict_of_letters(upper_case=True),
            **dict_of_digits(),
            **dict_of_special_symbols(),
            **{' ': 'q0', '(': 'q1'}
        },
        'q1': {
            **dict_of_letters(),
            **dict_of_letters(upper_case=True),
            **dict_of_digits(),
            **dict_of_special_symbols(),
            **{' ': 'q1'}
        }}, ['q0', 'q1'])


def close_parenthesis_rules() -> Tuple[str, dict, list]:
    """ Возвращает правила для формирования ДКА для валидации закрывающихся скобок строки. """
    return ('Проверка числа (int): ', {
        'q0': {
            **dict_of_letters(),
            **dict_of_letters(upper_case=True),
            **dict_of_digits(),
            **dict_of_special_symbols(),
            **{' ': 'q0', ')': 'q1'}
        },
        'q1': {
            **dict_of_letters(),
            **dict_of_letters(upper_case=True),
            **dict_of_digits(),
            **dict_of_special_symbols(),
            **{' ': 'q1'}
        }}, ['q0', 'q1'])


def dict_of_letters(state: str='REJECT', upper_case: bool=False) -> Dict[str, str]:
    """ Возвращает словарь с ключем-значением 'состояние-переход' по буквенным символам. """
    letters = string.ascii_uppercase if upper_case else string.ascii_lowercase
    return {x: state for x in letters}


def dict_of_digits(state: str='REJECT') -> Dict[str, str]:
    """ Возвращает словарь с ключем-значением 'состояние-переход' по циферным символам. """
    return {x: state for x in string.digits}


def dict_of_special_symbols(state: str='REJECT') -> Dict[str, Dict[str, str]]:
    """ Возвращает словарь с ключем-значением 'состояние-переход' по специальным символам. """
    return {x: state for x in string.punctuation}


def main() -> None:
    check = True
    print("\nЛексический анализатор")
    while(check):
        choice = int(input("\nМеню:\n1. Запустить анализатор с введенной строкой\n2. Выйти из программы\nВыбор [1/2]: "))
        if (choice == 1):
            string = input('\nВведите строку для проверки: ')
            analyzer = Analyzer(all_dfa())
            __, valid_result = analyzer.analyzing(string)
            analyzer.pretty_table_print(valid_result)
        elif (choice == 2):
            sys.exit()
        else:
            check = False


if __name__ == "__main__":
    main()