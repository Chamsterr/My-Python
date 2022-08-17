def task_1():
    letters_amazon ='''
                     We spent several years building our own database engine,
                     Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible
                     service with the same or better durability and availability as
                     the commercial engines, but at one-tenth of the cost. We were
                     not surprised when this worked.
                    '''
    find = lambda txt, word: txt[txt.find(word)-18:txt.find(word)+18] if word in txt else -1
    print(find(letters_amazon, 'SQL'))

def task_2():
    price = [[9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
            [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
            [8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
            [7.1, 5.9, 4.8, 4.8, 4.7, 3.9]]

    sample = [line[::2] for line in price]
    print(sample)

def task_3():
    visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
                    'Safari', 'corrupted', 'Safari', 'corrupted',
                    'Chrome', 'corrupted', 'Firefox', 'corrupted']
    visitors[1::2] = visitors[::2]
    print(visitors)

def task_4():
    import matplotlib.pyplot as plt

    cardiac_cycle = [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62]
    expected_cycles = cardiac_cycle[1:-2] * 10
    plt.plot(expected_cycles)
    plt.show()

def task_5():
    companies = {
        'CoolCompany' : {'Alice' : 33, 'Bob' : 28, 'Frank' : 29},
        'CheapCompany' : {'Ann' : 4, 'Lee' : 9, 'Chrisi' : 7},
        'SosoCompany' : {'Esther' : 38, 'Cole' : 8, 'Paris' : 18}}
    
    illegal = [company[0] for company in companies.items() if any(salary < 9 for salary in company[1].values())]

    illegal = [company for company in companies if any(salary < 9 for salary in companies[company].values())]
    print(illegal)

def task_6():
    column_names = ['name', 'salary', 'job']
    db_rows = [('Alice', 180000, 'data scientist'),
               ('Bob', 99000, 'mid-level manager'),
               ('Frank', 87000, 'CEO')]

    table = [dict(zip(column_names, db_row)) for db_row in db_rows]
    print(table)

