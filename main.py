from company import Company
from startup import startup

import os
import platform

def command():
    user_input = input("\n>>> ")
    command_list = user_input.split()

    action = command_list[0]

    if len(command_list) == 3:
        company_name = command_list[1]
        country = command_list[2]

        if action == 'add':
            add_company(company_name, country)
        elif action == 'rm':
            delete_company(company_name, country)
        elif action == 'update':
            update_company(company_name, country)
        elif action == 'check':
            check_company(company_name, country)
        else:
            print(f'Command {action} is not a valid action.')

    elif len(command_list) == 1:
        if action == 'list':
            Company.list_all()
        elif action == 'exit':
            exit(0)
        elif action == 'clear':
            if platform.system() == 'Linux' or platform.system() == 'Darwin':
                os.system('clear')
            else:
                os.system('cls')
        elif action == 'help':
            print_commands()
        else:
            print(f'Command *{action}* is not a valid action.')


def add_company(company_name, country):
    comp = Company(company_name, country)
    comp.save()


def delete_company(company_name, country):
    comp = Company(company_name, country)
    comp.remove()


def update_company(company_name, country):
    comp = Company(company_name, country)
    exist = comp.check_without_print()
    if exist:
        new_name = input('New name (Leave blank if old name): ')
        new_country = input('New country (Leave blank if old name): ')

        comp.update(new_name, new_country)
        print('DONE')
    else:
        print(f'Company {company_name} from {country} doesnt exist.')


def check_company(company_name, country):
    comp = Company(company_name, country)
    comp.check()


def print_commands():
    print('Commands:',
          'add company_name country',
          'rm company_name country',
          'update company_name country',
          'check company_name country',
          'list',
          'clear',
          'exit', 
           sep='\n')


def main():
    startup()

    print('Welcome')
    print_commands()

    while True:
        command()


if __name__ == '__main__':
    main()
