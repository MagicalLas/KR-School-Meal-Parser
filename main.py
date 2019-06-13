import requests


class School:
    class Region:
        SEOUL = "stu.sen.go.kr"
        INCHEON = "stu.ice.go.kr"
        BUSAN = "stu.pen.go.kr"
        GWANGJU = "stu.gen.go.kr"
        DAEJEON = "stu.dge.go.kr"
        DEAGU = "stu.dge.go.kr"
        SEJONG = "stu.sje.go.kr"
        ULSAN = "stu.use.go.kr"
        GYEONGGI = "stu.goe.go.kr"
        KANGWON = "stu.kwe.go.kr"
        CHUNGBUK = "stu.cbe.go.kr"
        CHUNGNAM = "stu.cne.go.kr"
        GYEONGBUK = "stu.gbe.go.kr"
        GYEONGNAM = "stu.gne.go.kr"
        JEONBUK = "stu.jbe.go.kr"
        JEONNAM = "stu.jne.go.kr"
        JEJU = "stu.jje.go.kr"

    class Type:
        KINDERGARTEN = 1
        ELEMENTARY = 2
        MIDDLE = 3
        HIGH = 4

    def __init__(self, school_region, school_type, school_code):
        self.region = school_region
        self.type = school_type
        self.code = school_code


class MealParser:
    def __init__(self, school):
        self.school = school

    def create_url(self, year, month):
        url = f"https://{self.school.region}/sts_sci_md00_001.do?"
        url += f"schulCode={self.school.code}&"
        url += f"schulCrseScCode={self.school.type}&"
        url += f"schulKndScCode={self.school.type:02d}&"
        url += f"ay={year}&"
        url += f"mm={month:02d}&"

        return url


if __name__ == "__main__":
    school = School(School.Region.GWANGJU, School.Type.HIGH, "F100000120")
    parser = MealParser(school)
    print(parser.create_url(2019, 6))
