import re
from datetime import date


regex = re.compile("[가-힣\s]+")


class Menu:
    class Time:
        BREAKFAST = "breakfast"
        LUNCH = "lunch"
        DINNER = "dinner"

    def __init__(self, menu_list):
        self.menu = self.parse_menu_list(menu_list)
        self.today = self.menu[date.today().day]

    def __str__(self):
        return str(self.menu)

    def parse_menu_list(self, menu_list):
        result = {}

        for item in menu_list:
            index = None
            menu = {
                Menu.Time.BREAKFAST: [],
                Menu.Time.LUNCH: [],
                Menu.Time.DINNER: []
            }

            if item.contents:
                for text in item.strings:
                    if text.isdigit():
                        result[int(text)] = menu
                    else:
                        index = self.__set_index(index, text)
                        match_result = regex.match(text)

                    if index is not None:
                        if match_result:
                            menu[index].append(match_result.group())

        return result

    def __set_index(self, index, text):
        if text == "[조식]":
            return Menu.Time.BREAKFAST
        elif text == "[중식]":
            return Menu.Time.LUNCH
        elif text == "[석식]":
            return Menu.Time.DINNER
        else:
            return index
