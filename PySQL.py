import psycopg2
from functions import create_db, add_client, add_phone, update_client, delete_client, delete_phones, find_client

with psycopg2.connect(database='HW_PySQL', user='postgres', password='postgres') as conn:
    cur = conn.cursor()

    if __name__ == '__main__':
        create_db()
        print('База данных успешно создана')

        add_client('Ivan', 'Ivanov', 'iivanov@gmail.com')
        add_client('Petr', 'Smirnov', 'petsmirnov@gmail.com')
        print('Клиент добавлен')

        add_phone(1, ['+79000000000', '+79000000001', '+79000000002'])
        add_phone(2, ['+79101101010'])
        print('Номер телефона добавлен')

        update_client(1, first_name='Semen')
        print('Данные успешно обновлены')

        delete_client(1)
        print('Клиент удален')

        delete_phones((3,))
        print('Номер телефона удален')

        find_client(search_query='Ivanov')

conn.close()
