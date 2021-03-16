token='1641800457:AAGyKQuCJvtAnFM3cvYQpX0M5s80tgBNbwE'
my_chat_id=1481914600
def decorator_func(simple_func):
    def inner_func():
        print('Инструкции до ...')
        simple_func()
        print('Инструкции после ...')
    return inner_func

@decorator_func
def simple_func():
    print('Я простая одинокая функция')

if __name__ == '__main__':
    simple_func()