# This is a sample Python script.
import requests
from bs4 import BeautifulSoup
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def get_menus(date):
    response = requests.get(f'https://wis.hufs.ac.kr/jsp/HUFS/cafeteria/viewWeek.jsp?startDt={date}&endDt={date}&caf_name=%EC%9D%B8%EB%AC%B8%EA%B4%80%EC%8B%9D%EB%8B%B9&caf_id=h101')
    soup = BeautifulSoup(response.text, 'html.parser')
    menus = soup.find_all('table', height='100%')
    return menus


def lunch_menu(date):
    menus = get_menus(date)
    return extract_menu_string(menus[1]), extract_menu_string(menus[2])


def dinner_menu(date):
    menus = get_menus(date)
    return extract_menu_string(menus[4])


def extract_menu_string(menu):
    menu_list = []
    for td_tag in menu.find_all('td'):
        if td_tag.text != '':
            menu_list.append(td_tag.text)
    return menu_list


def get_today():
    import datetime
    today = datetime.date.today()
    return today.strftime('%Y%m%d')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(get_today())
    print(lunch_menu('20230424'))
    print(dinner_menu('20230424'))