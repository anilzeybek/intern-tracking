from company import Company


def add_company(company_name, country):
    comp = Company(company_name, country)
    comp.save()
    comp.remove()


def main():
    print('Welcome')

    command = input()
    command_list = command.split()

    if command_list[0] == 'add':
        add_company(command_list[1], command_list[2])
    if command_list[0] == 'rm':
        pass
    if command_list[0] == 'update':
        pass


if __name__ == '__main__':
    main()
