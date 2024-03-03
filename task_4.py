from datetime import datetime
from datetime import timedelta


def get_upcoming_birthdays(users: list) -> list:
    today = datetime.today().date()  # отримуємо поточну дату
    congratulation_list = []  # створюємо список для результатів
    for user in users:  # перебираємо всіх користувачів по одному
        birthday = user["Дата_народження"]  # отримуємо дату народження конкретного користувача
        birthday = str(today.year) + birthday[4:]  # змінюємо рік народження на поточний
        birthday = (datetime.strptime(birthday, "%Y.%m.%d")).date()  # перетворюємо дату народження в об'єкт datetime
        if (0 <= (birthday - today).days <= 7):  # перевіряємо, чи наступає дата впродовж тижня, включаючи поточний день
            day_week = (birthday.weekday())  # отримуємо день тижня, на який припадає день народження
            user_dict = {"Ім'я": user["Ім'я"], "День_народження": birthday.strftime("%Y.%m.%d"),}  # створюємо словник з іменем користувача та датою народження
            if day_week == 5:  # перевіряємо чи не випадає на субботу
                congratulations_day = birthday + timedelta(days=2)  # день для привітання на 2 дні пізніше, якщо так
            elif day_week == 6:  # перевіряємо чи не випадає на неділю
                congratulations_day = birthday + timedelta(days=1)  # день для привітання на день пізніше, якщо так
            else:  # всі інші припадають на будній день
                congratulations_day = birthday  # вітати треба в той же день
            user_dict["День_для_привітання"] = congratulations_day.strftime("%Y.%m.%d")  # додаємо до словника день привітання
            congratulation_list.append(user_dict)  # додаємо в список результатів
        else:
            continue
    # для покращення сприйняття результат виводим у вигляді таблиці
    print("Список привітань на поточному тижні:")
    A = "Ім'я"
    B = "День_народження"
    C = "Вітатимемо"
    string = f"|| {A:>20} | {B:>15} | {C:>15} ||"
    print(string)
    for line in congratulation_list:
        A = line["Ім'я"]
        B = line["День_народження"]
        C = line["День_для_привітання"]
        # string = f"|| {A:>20} | {B:>15} | {C:>15} ||"
        print(string)
    return congratulation_list  # повертаємо список іменинників


# Список днів народження колег
users = [
    {"Ім'я": "Іван Микитенко", "Дата_народження": "1985.01.23"},
    {"Ім'я": "Вікторія Астаф'єва", "Дата_народження": "1990.01.27"},
    {"Ім'я": "Віталій Тихонов", "Дата_народження": "1995.01.28"},
    {"Ім'я": "Ольга Антоненко", "Дата_народження": "1991.01.29"},
    {"Ім'я": "Олександра Гонарова", "Дата_народження": "1987.01.30"},
    {"Ім'я": "Дмитро Шмалько", "Дата_народження": "1999.01.31"},
    {"Ім'я": "Вероніка Савчук", "Дата_народження": "1986.03.01"},
    {"Ім'я": "Людмила Нечипоренко", "Дата_народження": "1992.03.02"},
    {"Ім'я": "Марина Сусловець", "Дата_народження": "1989.03.03"},
    {"Ім'я": "Серафим Фомін", "Дата_народження": "1994.03.04"},
    {"Ім'я": "Філіп Кравченко", "Дата_народження": "1990.03.05"},
    {"Ім'я": "Марія Голуб", "Дата_народження": "1991.03.06"},
    {"Ім'я": "Владислав Князюк", "Дата_народження": "1985.03.07"},
    {"Ім'я": "Наталія Порох", "Дата_народження": "1988.03.08"},
]

get_upcoming_birthdays(users)
