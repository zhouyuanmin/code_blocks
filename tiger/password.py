import logging
import string

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


def get_password_by_date(begin_year=1990, end_year=2100, path=""):
    if not path:
        path = f"../trash/{begin_year}_{end_year}.txt"
    with open(path, "w") as f:
        for year in range(begin_year, end_year):
            for month in range(1, 13):
                for day in range(1, 32):
                    date = f"{year}{month:0>2}{day:0>2}"
                    f.write(date)
                    f.write("\n")
            logging.info(year)


def get_password(path=""):
    """字母2+数字6,字母3+数字5,字母4+数字4"""
    if not path:
        path = f"../trash/password44.txt"
    with open(path, "w") as f:
        for _letter, _digit in [[2, 6], [3, 5], [4, 4]]:
            chars = []
            for _ in range(_letter):
                chars.append(string.ascii_lowercase)
            for _ in range(_digit):
                chars.append(string.digits)
            for _1 in chars[0]:
                for _2 in chars[1]:
                    for _3 in chars[2]:
                        for _4 in chars[3]:
                            for _5 in chars[4]:
                                for _6 in chars[5]:
                                    for _7 in chars[6]:
                                        for _8 in chars[7]:
                                            date = f"{_1}{_2}{_3}{_4}{_5}{_6}{_7}{_8}"
                                            f.write(date + "\n")
                logging.info(_1)


if __name__ == "__main__":
    pass
