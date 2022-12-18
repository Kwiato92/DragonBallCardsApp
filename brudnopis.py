items = {
    1: {
        'name': 'Red Leicester',
        'qty': 12,
        'price': 25
    },
    2: {
        'name': 'Cheddar',
        'qty': 23,
        'price': 3
    },
}

users = {
    'admin': {
        'email': 'admin@cheeseshop.com',
        'password': 'admin1',
        'admin': True,
        'purchase_history': []
    },
    'johncleese': {
        'email': 'john.cleese@mosw.gov.uk',
        'password': 'spam',
        'admin': False,
        'purchase_history': [
            {
                2: {
                    'qty': 1,
                    'total_price': 3
                }
            },
            {
                1: {
                    'qty': 10,
                    'total_price': 250
                },
                2: {
                    'qty': 2,
                    'total_price': 6
                }
            }
        ]
    },
}


def show_menu(menu: dict):
    for action_id, description in menu.items():
        print(f'{action_id}. {description}')


def is_logged_in(session):
    if not session['logged_in']:
        print('Do wykonania tej akcji musisz być zalogowany.')
        return False
    else:
        return True


def log_in(users, session):
    print('Podaj login: ')
    login = input()
    print('Podaj hasło: ')
    password = input()
    if users.get(login) and users[login]['password'] == password:
        session['logged_in'] = True
        session['user_id'] = login
        return session
    else:
        print('Login albo hasło niepoprawne')
        return session


def show_items(session, items):
    if not is_logged_in(session):
        return None
    for item, properties in items.items():
        print(f'{item}. {properties["name"]} dostępne {properties["qty"]} w cenie {properties["price"]}')


def find_item(session, items):
    if not is_logged_in(session):
        return None
    print('Podaj nazwę towaru: ')
    query = input()
    for item_id, item_properties in items.items():
        if item_properties["name"].lower() == query.lower():
            print(f'{item_id}. {item_properties["name"]} dostępne {item_properties["qty"]} w cenie '
                  f'{item_properties["price"]}')


def add_item_to_cart(session, items, cart):
    if not is_logged_in(session):
        return cart
    print('Podaj ID towaru: ')
    item = int(input())
    item_properties = items.get(item)
    if not item_properties:
        print('Nie ma takiego towaru w magazynie.')
        return cart
    if item in cart:
        print('Dodano już ten produkt do koszyka, musisz użyć innej funkcji.')
        return cart
    print('Podaj ile towaru dodać do koszyka: ')
    quantity = int(input())
    if item_properties['qty'] > quantity and item_properties['qty'] > 0:
        cart[item] = {'qty': quantity, 'total_price': quantity * item_properties['price']}
        print(f'Dodano {quantity} {item_properties["name"]} do koszyka.')
        return cart
    else:
        print('Nie ma takiej ilości towaru na stanie.')
        return cart


def remove_item_from_cart(session, cart):
    if not is_logged_in(session):
        return cart
    print('Podaj ID towaru do usunięcia z koszyka')
    item = int(input())
    if cart.pop(item, None):
        print(f'Usunięto {item} z koszyka.')
        return cart
    else:
        print(f'Towaru {item} nie było w koszyku.')
        return cart


def change_item_quantity_in_cart(session, cart):
    if not is_logged_in(session):
        return cart
    print('Podaj ID towaru: ')
    item = int(input())
    if item not in cart:
        print('Nie ma takiego towaru w koszyku')
        return cart
    item_properties = items.get(item)
    print('Podaj nową ilość towaru: ')
    quantity = int(input())
    if item_properties['qty'] > quantity and item_properties['qty'] > 0:
        cart[item] = {'qty': quantity, 'total_price': quantity * item_properties['price']}
        print(f'Zmieniono ilość {item_properties["name"]} w koszyku na {quantity}.')
        return cart
    else:
        print('Nie ma takiej ilości towaru na stanie.')
        return cart


def purchase_cart(session, cart, items, users):
    if not is_logged_in(session):
        return None
    for item, properties in cart.items():
        items[item]['qty'] -= properties['qty']
    users[session['user_id']]['purchase_history'].append(dict(cart))
    cart.clear()
    return cart, items, users


def show_cart(session, cart, items):
    if not is_logged_in(session):
        return None
    cart_total_price = 0
    for item, properties in cart.items():
        print(f'{item}. {items[item]["name"]}, {properties["qty"]} sztuk, koszt {properties["total_price"]} '
              f'({items[item]["price"]} za sztukę)')
        cart_total_price += properties["total_price"]
    print(f'Łączny koszt {cart_total_price}')


MENU = {
    0: 'Zakończ sesję',
    1: 'Zaloguj się',
    2: 'Wyświetl towary',
    3: 'Wyszukaj towar',
    4: 'Dodaj towar do koszyka',
    5: 'Usuń towar z koszyka',
    6: 'Zmień ilość towaru w koszyku',
    7: 'Sfinalizuj zamówienie',
    8: 'Pokaż koszyk'
}

cart = {}
end_session = False
session = {
    'logged_in': False,
    'user_id': None
}

while not end_session:
    show_menu(MENU)
    print('Co chcesz zrobić?')
    action = int(input())

    if action == 0:
        end_session = True
    elif action == 1:
        session = log_in(users, session)
    elif action == 2:
        show_items(session, items)
    elif action == 3:
        find_item(session, items)
    elif action == 4:
        cart = add_item_to_cart(session, items, cart)
    elif action == 5:
        cart = remove_item_from_cart(session, cart)
    elif action == 6:
        cart = change_item_quantity_in_cart(session, cart)
    elif action == 7:
        cart, items, users = purchase_cart(session, cart, items, users)
    elif action == 8:
        show_cart(session, cart, items)
    else:
        print('Nie ma takiej akcji.')

else:
    print('Do zobaczenia!')