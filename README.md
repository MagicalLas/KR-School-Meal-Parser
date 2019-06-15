# KR-School-Meal-Parser
**Python 전국 학교 급식 파싱 API**

[Node.js 급식 파싱 라이브러리](https://github.com/leegeunhyeok/node-school-kr)를 참고하여 Python 버전으로 개량해보았습니다.

사용하기 전에 각 학교마다 붙어있는 학교의 고유 코드를 알아내야 합니다.

학교 고유 코드 검색은 [여기](https://code.schoolmenukr.ml/)서 해주시기 바랍니다.

### 사용법

- 이번 달의 전체 식단표 받아오기

```Python
from menu_parser import MenuParser
from school import School


school = School(School.Region.GWANGJU, School.Type.HIGH, "F100000120")
parser = MenuParser(school)
menus = parser.get_menu()

print(menus)
```

- 결과

```JSON
{
    "1": {
        "breakfast": [],
        "lunch": [],
        "dinner": []
    },
    "2": {
        "breakfast": [],
        "lunch": [],
        "dinner": []
    },
    "3": {
        "breakfast": [
            "백미밥",
            "제육채소볶음",
            "오징어브로컬리다시마초장",
            "깍두기",
            "야쿠르트",
            "미니버터크로와상",
            "두부된장국"
        ],
        "lunch": [
            "쇠고기미역국",
            "돈까스샐러드",
            "열무김치",
            "파인애플",
            "검정쌀밥",
            "고구마대새콤무침",
            "굴비오븐구이"
        ],
        "dinner": [
            "대패삼겹데리덮밥",
            "감자채볶음",
            "쭈꾸미채소무침",
            "배추김치",
            "치킨너겟",
            "사과당근쥬스"
        ]
    },
    "4": {
        "breakfast": [
            "백미밥",
            "닭곰탕",
            "꽈리고추달걀장조림",
            "깍두기",
            "소이라떼",
            "메이플피칸파이",
            "볶음김치"
        ],
        "lunch": [
            "카레덮밥",
            "우렁살미나리초무침",
            "거꾸로요구르트",
            "깍두기",
            "순살닭강정",
            "갓김치"
        ],
        "dinner": [
            "백미밥",
            "시금치된장국",
            "돼지갈비김치찜",
            "새송이버섯볶음",
            "식빵튀김",
            "깍두기",
            "사과"
        ]
    },
    "5": {
        "breakfast": [
            "백미밥",
            "콩나물무침",
            "닭정육칠리소스볶음",
            "배추김치",
            "블루베리푸딩",
            "참치김치찌개",
            "쥐손채볶음"
        ],
        "lunch": [
            "어묵무국",
            "돼지고기편육",
            "찰보리밥",
            "오이스틱",
            "청경채생채",
            "방울토마토"
        ],
        "dinner": []
    },

    "..." : {
        "..."
    },

    "30": {
        "breakfast": [],
        "lunch": [],
        "dinner": []
    }
}
```

- 오늘 날짜의 식단표

```Python
from menu_parser import MenuParser
from school import School


school = School(School.Region.GWANGJU, School.Type.HIGH, "F100000120")
parser = MenuParser(school)
menus = parser.get_menu()

print(menus.today)
```

- 원하는 날짜의 1개월 식단표

```Python
from menu_parser import MenuParser
from school import School


school = School(School.Region.GWANGJU, School.Type.HIGH, "F100000120")
parser = MenuParser(school)
menus = parser.get_menu(2019, 5)

print(menus)
```

- JSON 파일로 저장하기

```Python
from menu_parser import MenuParser, save_to_json
from school import School


school = School(School.Region.GWANGJU, School.Type.HIGH, "F100000120")
parser = MenuParser(school)
menus = parser.get_menu()

# 이름을 지정하지 않으면 기본으로 result.json으로 저장됨
# save_to_json(menu.today)

save_to_json(menu.today, "today.json")
```