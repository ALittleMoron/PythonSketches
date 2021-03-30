import sys

from termcolor import colored, cprint

import Caesars_method_with_keyword as caesar_kw
import Caesars_method_on_affine_permutation as caesar_af
import Permutation_method as pm


class Menu:
    def __init__(self):
        self.config = {
            'kw_keyword': 'keyword',
            'kw_shift': 5,
            'af_initial_shift': 5,
            'af_further_shift': 3,
            'pm_first_keyword': 'abstract',
            'pm_second_keyword': 'word',
        }
        self.instances = {
            'kw_keyword': str,
            'kw_shift': int,
            'af_initial_shift': int,
            'af_further_shift': int,
            'pm_first_keyword': str,
            'pm_second_keyword': str, 
        }

    def config_change(self):
        cprint(
            '\n\nВведите через пробел ключ и значение, которые хотите изменить.\n', 'cyan')
        cprint(f'Конфигурация: \n{self.config}\n', "yellow")

        try:
            key, value = input(colored('ключ-значение: ', 'cyan')).split(' ')
        except ValueError:
            cprint(
                '\nНеправильный ввод или вы решили выйти. Ничего не меняю, возвращаю вас в главное меню.\n\n', 'red')
            return
        try:
            value = self.instances[key](value)
        except ValueError:
            cprint('\nНеправильный тип данных для значения конфига.\n\n', 'red')
            return
        except KeyError:
            pass

        if key not in self.config:
            cprint(
                '\nНеверный ключ для конфига, либо вы пытались добавить ещё одно поле в нерасширяемый конфиг.\n\n', 'red')
        else:
            cprint(
                f'Значение "{value}" для поля "{key}" успешно установлено!\n\n', 'green')
            self.config[key] = value

    def keyword_caesar_form(self):
        print(colored(
            f"\nИспользовать сдвиг ({self.config['kw_shift']}) и ключевое слово ({self.config['kw_keyword']}) из конфига? [y/n]", 'cyan'), end='')
        if input('\n> ') in ['нет', 'n', 'N', 'Нет', 'No', 'no']:
            cprint(f'\nВведите через пробел свой сдвиг и ключевое слово.', 'cyan')
            try:
                shift, keyword = input('> ').split()
                shift = int(shift)
            except ValueError:
                cprint(
                    '\nНеправильный ввод или вы решили выйти. Ничего не меняю.', 'red')
            else:
                self.config['kw_shift'] = shift
                self.config['kw_keyword'] = keyword

        print(colored(
            '\nЧто вы хотите сделать: зашифровать [e] или расшифровать [d]? Введите букву в зависимости от выбора.', 'cyan'), end='')
        choice = input('\n> ')
        if choice == 'd':
            print(colored(
                '\nВведите фразу или предложение, которое хотите расшифровать.', 'cyan'), end='')
            phrase = input('\n> ')
            print(
                colored(f"Оригинальная фраза/предложение: {phrase}", "yellow"), end='')
            print(colored(
                f"Расшифрованная фраза/предложение: {caesar_kw.decrypting(phrase, self.config['kw_shift'], self.config['kw_keyword'])}", 'yellow'), end='')
        elif choice == 'e':
            print(colored(
                '\nВведите фразу или предложение, которое хотите зашифровать.', 'cyan'), end='')
            phrase = input('\n> ')
            print(
                colored(f"\nОригинальная фраза/предложение: {phrase}", "yellow"), end='')
            print(colored(
                f"\nЗашифрованная фраза/предложение: {caesar_kw.encrypting(phrase, self.config['kw_shift'], self.config['kw_keyword'])}\n\n", 'yellow'))

    def affine_caesar_form(self):
        print(colored(
            f"\nИспользовать начальный сдвиг ({self.config['af_initial_shift']}) и дальнейший сдвиг ({self.config['af_further_shift']}) из конфига? [y/n]", 'cyan'), end='')
        if input('\n> ') in ['нет', 'n', 'N', 'Нет', 'No', 'no']:
            cprint(f'\nВведите через пробел свой начальный и дальнейший сдвиг.', 'cyan')
            try:
                initial_shift, further_shift = input('> ').split()
                initial_shift, further_shift = int(
                    initial_shift), int(further_shift)
            except ValueError:
                cprint(
                    '\nНеправильный ввод или вы решили выйти. Ничего не меняю.', 'red')
            else:
                self.config['af_initial_shift'] = initial_shift
                self.config['af_further_shift'] = further_shift

        print(colored(
            '\nЧто вы хотите сделать: зашифровать [e] или расшифровать [d]? Введите букву в зависимости от выбора.', 'cyan'), end='')
        choice = input('\n> ')
        if choice == 'd':
            print(colored(
                '\nВведите фразу или предложение, которое хотите расшифровать.', 'cyan'), end='')
            phrase = input('\n> ')
            print(
                colored(f"Оригинальная фраза/предложение: {phrase}", "yellow"), end='')
            print(colored(
                f"Расшифрованная фраза/предложение: {caesar_af.decrypting(phrase, self.config['af_initial_shift'],self.config['af_further_shift'])}", 'yellow'), end='')
        elif choice == 'e':
            print(colored(
                '\nВведите фразу или предложение, которое хотите зашифровать.', 'cyan'), end='')
            phrase = input('\n> ')
            print(
                colored(f"\nОригинальная фраза/предложение: {phrase}", "yellow"), end='')
            print(colored(
                f"\nЗашифрованная фраза/предложение: {caesar_af.encrypting(phrase, self.config['af_initial_shift'],self.config['af_further_shift'])}\n\n", 'yellow'))

    def two_square_form(self):
        pass

    def permutation_form(self):
        print(colored(
            f"\nИспользовать первое ключевое слово ({self.config['pm_first_keyword']}) и второе ключевое слово ({self.config['pm_second_keyword']}) из конфига? [y/n]", 'cyan'), end='')
        if input('\n> ') in ['нет', 'n', 'N', 'Нет', 'No', 'no']:
            cprint(f'\nВведите через пробел 2 ключевых слова.', 'cyan')
            try:
                pm_first_keyword, pm_second_keyword = input('> ').split()
            except ValueError:
                cprint(
                    '\nНеправильный ввод или вы решили выйти. Ничего не меняю.', 'red')
            else:
                self.config['pm_first_keyword'] = pm_first_keyword
                self.config['pm_second_keyword'] = pm_second_keyword

        print(colored(
            '\nЧто вы хотите сделать: зашифровать [e] или расшифровать [d]? Введите букву в зависимости от выбора.', 'cyan'), end='')
        choice = input('\n> ')
        if choice == 'd':
            print(colored(
                '\nВведите фразу или предложение, которое хотите расшифровать.', 'cyan'), end='')
            phrase = input('\n> ')
            permutation = pm.PermutationCipher(self.config['pm_first_keyword'], self.config['pm_second_keyword'], phrase)
            print(
                colored(f"Оригинальная фраза/предложение: {phrase}", "yellow"), end='')
            print(colored(
                f"Расшифрованная фраза/предложение: {permutation.decrypting()}", 'yellow'), end='')
        elif choice == 'e':
            print(colored(
                '\nВведите фразу или предложение, которое хотите зашифровать.', 'cyan'), end='')
            phrase = input('\n> ')
            permutation = pm.PermutationCipher(self.config['pm_first_keyword'], self.config['pm_second_keyword'], phrase)
            print(
                colored(f"\nОригинальная фраза/предложение: {phrase}", "yellow"), end='')
            print(colored(
                f"\nЗашифрованная фраза/предложение: {permutation.encrypting()}\n\n", 'yellow'))

    def main(self):
        menu_choices = {
            '1': self.keyword_caesar_form,
            '2': self.affine_caesar_form,
            '3': self.two_square_form,
            '4': self.permutation_form,
            '5': self.config_change,
            '0': sys.exit,
        }
        menu_string = [
            '|===================== Меню =====================|\n',
            '| 1. Метод Цезаря с ключевым словом              |\n',
            '| 2. Метод Цезаря с аффинной перестановкой       |\n',
            '| 3. Метод "Двойной квадрат Уинстона"            |\n',
            '| 4. Метод перестановки                          |\n',
            '| 5. Изменить параметром в конфиге               |\n',
            '| 0. Выйти из программы                          |\n',
            '|================================================|\n'
        ]

        cprint(''.join(menu_string), 'cyan')
        choice = input('> ')
        if choice not in menu_choices:
            self.main()

        action = menu_choices.get(choice, None)
        action()

        self.main()


if __name__ == "__main__":
    menu = Menu()
    menu.main()
