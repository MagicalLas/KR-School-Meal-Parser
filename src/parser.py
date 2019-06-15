from bs4 import BeautifulSoup
import datetime
import json
import logging
import requests

from menu import Menu
from school import School


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s:: %(message)s",
    datefmt='%Y/%m/%d %H:%M:%S'
)


def save_to_json(result, name="result.json"):
    logging.info(f"Started saving json file as {name}.")

    try:
        with open(name, "w", encoding="UTF-8") as f:
            json.dump(result, f, ensure_ascii=True, indent=4)
    except Exception as e:
        logging.error(e)
    else:
        logging.info("Finished saving.")


class MenuParser:
    def __init__(self, school):
        self.school = school

    def get_menu(self, year=None, month=None):
        """
        해당 학교로부터 급식을 가져온다.
        year와 month가 모두 주어졌다면 해당하는 정보를 가져온다.
        주어지지 않았을 때에는 자동으로 가져오게 된다.
        """
        if year is None or month is None:
            today = datetime.date.today()
            url = self.__create_url(today.year, today.month)
        else:
            url = self.__create_url(year, month)

        page = self.__get_page(url)
        soup = BeautifulSoup(page, "html.parser")
        items = soup.select("#contents > div > table > tbody > tr > td > div")

        return Menu(items)

    def __get_page(self, url):
        try:
            page = requests.get(url).text
        except Exception as e:
            logging.error(e)

        return page

    def __create_url(self, year, month):
        today = datetime.date(year, month, 1)

        url = f"https://{self.school.region}/sts_sci_md00_001.do?"
        url += f"schulCode={self.school.code}&"
        url += f"schulCrseScCode={self.school.type}&"
        url += f"schulKndScCode={self.school.type:02d}&"
        url += f"ay={today.year}&"
        url += f"mm={today.month:02d}"

        return url


if __name__ == "__main__":
    school = School(School.Region.GWANGJU, School.Type.HIGH, "F100000120")
    parser = MenuParser(school)

    menu = parser.get_menu()
    save_to_json(menu.today, "today.json")
