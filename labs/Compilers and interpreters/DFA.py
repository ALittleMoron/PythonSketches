# Код взят отсюда: https://github.com/VijayaGB98/automata-theory-py/tree/master/finite-state-machine/deterministic-finite-automata


class DFA:
    def __init__(self):
        self.Q = self.populate_states()
        self.SIGMA = self.populate_alphabet()
        self.DELTA = self.populate_transition_function()
        self.START_STATE, self.ACCEPT_STATES = self.set_start_accept()
        self.CURRENT_STATE = None

    def set_start_accept(self):
        while(True):
            start = input("Введите стартовое состояние: ")
            accept = input("Введите состояние допуска: ").split()
            if (start in self.Q) and (set(accept).issubset(set(self.Q))):
                return start, accept
            else:
                print("Пожалуйста, введите стартовое состояние и состояние допуска, которые есть в Q : {}.\nСостояние допуска должно быть допустимым подмножеством Q\n".format(self.Q))

    def populate_states(self):
        Q_input = input("Введите список состояний через пробел: ").split()
        print("СОСТОЯНИЯ : {}".format(Q_input))
        return Q_input
    
    def populate_alphabet(self):
        SIGMA_input = input("Введите алфавит ввода через пробел: ").split()
        print("АЛФАВИТ : {}".format(SIGMA_input))
        return SIGMA_input

    def populate_transition_function(self):
        transition_dict = {el : {el_2 : 'REJECT' for el_2 in self.SIGMA} for el in self.Q}

        for key, dict_value in transition_dict.items():
            print("Введите переходы для состояния {}. При необходимости используйте 'REJECT'.".format(key))

            for input_alphabet, transition_state in dict_value.items():
                transition_dict[key][input_alphabet] = input("ТЕКУЩЕЕ СОСТОЯНИЕ : {}\tАЛФАВИТ ВВОДА : {}\tСЛЕДУЮЩЕЕ СОСТОЯНИЕ : ".format(key, input_alphabet))
        
        print("\nПЕРЕХОДНАЯ ФУНКЦИЯ Q X SIGMA -> Q")
        print("ТЕКУЩЕЕ СОСТОЯНИЕ\tАЛФАВИТ ВВОДА\tСЛЕДУЮЩЕЕ СОСТОЯНИЕ")
        for key, dict_value in transition_dict.items():
            for input_alphabet, transition_state in dict_value.items():
                print("{}\t\t{}\t\t{}".format(key, input_alphabet, transition_state))

        return transition_dict

    def run_state_transition(self, input_symbol):
        if (self.CURRENT_STATE == 'REJECT'):
            return False
        print("ТЕКУЩЕЕ СОСТОЯНИЕ : {}\tАЛФАВИТ ВВОДА : {}\t СЛЕДУЮЩЕЕ СОСТОЯНИЕ : {}".format(self.CURRENT_STATE, input_symbol, self.DELTA[self.CURRENT_STATE][input_symbol]))
        self.CURRENT_STATE = self.DELTA[self.CURRENT_STATE][input_symbol]
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

if __name__ == "__main__":
    check = True
    print("\nДетерминированный конечный автомат (ДКА).")
    machine = DFA()
    while(check):
        choice = int(input("\nМеню:\n1. Заменить ДКА\n2. Запустить ДКА с введенной строкой\nВыбор [1/2]: "))
        if (choice == 1):
            machine = DFA()
        elif (choice == 2):
            input_string = list(input("Введите строку для обработки: "))
            print("ПРИНЯТО" if machine.run_machine(input_string) else "ОТКЛОНЕНО")
        else:
            check = False