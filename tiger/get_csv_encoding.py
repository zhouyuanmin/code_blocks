# 获取csv文件的编码格式
import csv


def get_csv_encoding(
    filename, encodings=("utf-8", "gbk", "GB2312", "gb18030", "utf-8-sig")
):
    """获取csv文件的编码格式"""
    for en in encodings:
        try:
            with open(filename, encoding=en) as f:
                reader = csv.reader(f)
                header = next(reader)
            return en
        except:
            pass
    return False


if __name__ == "__main__":
    headers = ["学号", "姓名", "分数"]
    rows = [("202001", "张三", "98"), ("202002", "李四", "95"), ("202003", "王五", "92")]
    file = "../resources/score.csv"
    with open(file, "w", encoding="utf8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    encoding = get_csv_encoding(file)
    print(encoding)
    with open(file, "r", encoding=encoding, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
