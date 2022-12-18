MENU = {
    0: 'Exit',
    1: 'All Cards',
    2: 'My cards'
}
MENU_1 = {
    1: 'Name',
    2: 'booster',
    3: 'price',
    5: 'come back'
}
MENU_2 = {
    1: 'Name',
    2: 'booster',
    3: 'price',
    5: 'come back'
}
Boosters = {
    1: 'BT1',
    2: 'BT2',
    3: 'BT3'
}


def show_menu(menu: dict):
    for action_id, description in menu.items():
        print(f'{action_id}. {description}')


def show_menu_1(menu: dict):
    for action_id, description in menu.items():
        print(f'{action_id}. {description}')


def show_menu_2(menu: dict):
    for action_id, description in menu.items():
        print(f'{action_id}. {description}')


def show_boosters(menu: dict):
    for action_id, description in menu.items():
        print(f'{action_id}. {description}')


while MENU:
    show_menu(MENU)
    print('Choose option')
    action = int(input())

    if action == 0:
        end_session = True
    if action == 1:
        show_menu_1(MENU_1)
        print('Choose option')
        action = int(input())
        if action == 1:
            print('Choose name')
            action = int(input())
        if action == 2:
            show_boosters(Boosters)
            print('pick booster')
            action = int(input())
        if action == 3:

    if action == 2:
        show_menu_1(MENU_2)
        print('Choose option')
        action = int(input())


