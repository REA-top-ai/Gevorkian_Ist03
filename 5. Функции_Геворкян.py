# def create_spreadsheet(title):
#     print('Создание электронной таблицы с именем '+title+'')
# create_spreadsheet('Загрузки') #Создание электронной таблицы с именем Загрузки

def create_spreadsheet(title, row_count=1000):
    print('Создание электронной таблицы с именем '+title+' и '+str(row_count)+' строками')
create_spreadsheet('Приложения', 10)