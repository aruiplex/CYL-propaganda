import string
from openpyxl.drawing.image import Image
import io
import requests
import json
import openpyxl


def get_pic(url):
    r = requests.get(url)
    print(r.status_code)
    pic = io.BytesIO(r.content)
    return pic


wb = openpyxl.Workbook()
ws = wb.active


def json_to_xlsx(json_file: str, xlsx_file: str):
    row_index = 2
    data = json.load(open(json_file, 'r', encoding='utf-8'))
    for k in data:
        for video in data[k]:
            for i, v in enumerate(video.values()):
                col_index = i+1
                try:
                    if type(v) == str and v.startswith("http"):
                        pic = Image(get_pic(v))
                        height_origin = pic.height
                        pic.height = 100
                        pic.width *= 100/height_origin
                        ws.add_image(
                            pic, f"{string.ascii_uppercase[col_index]}{row_index}")
                        ws.row_dimensions[row_index].height = 100

                    else:
                        ws.cell(row=row_index, column=col_index, value=v)
                except Exception as e:
                    print(e)

            row_index += 1

    wb.save(xlsx_file)


if __name__ == "__main__":
    json_to_xlsx("choices.json", "choice.xlsx")
