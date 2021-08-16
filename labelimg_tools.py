import glob
import json
import xml.etree.ElementTree as ET
import pandas as pd


def labelimg_to_labelme(input_xml_path, output_json_path):
    """
    將 labelimg 所產出的 label 檔 (.xml) 無痛轉換成 labelme 所產出的 label 檔 (.json)

    Args:
        - input_xml_path: full path of xml label file
            e.g., ./examples/test_001.xml
        - output_json_path: full path of json label file
            e.g., ./examples/test_001.json
    """
    tree = ET.parse(input_xml_path)
    root = tree.getroot()
    json_output = {
        "version": "4.5.9",
        "flags": {},
        "shapes": [],
        "imagePath": root.find('filename').text,
        "imageData": None,
        "imageHeight": int(float(root.find('size')[0].text)),
        "imageWidth": int(float(root.find('size')[1].text))
    }
    for member in root.findall('object'):
        shape_dict = {
            "label": member[0].text,
            "points": [
                [
                    float(member[4][0].text),
                    float(member[4][1].text)
                ],
                [
                    float(member[4][2].text),
                    float(member[4][3].text)
                ]
            ],
            "group_id": None,
            "shape_type": "rectangle",
            "flags": {}
        }
        json_output["shapes"].append(shape_dict)

    with open(output_json_path, 'w') as f:
        json.dump(json_output, f, indent=4)


def labelimg_to_df(input_xml_dir):
    """
    將 labelimg 所產出的 label 檔 (.xml) 無痛轉換成 DataFrame

    Args:
        - input_xml_dir: label 檔 (.xml) 所在的資料夾路徑
            e.g., ./examples/

    Returns:
        - xml_df: 用 xml 的資訊輸出成 DataFrame 格式
            filename: 標註的檔名
            width: 影像的寬
            height: 影像的高
            class: 貼標的內容
            x_min：矩形框左上角的 x 座標
            y_min：矩形框左上角的 y 座標
            x_max：矩形框右下角的 x 座標
            y_max：矩形框右下角的 y 座標
            
    """
    xml_list = []
    for xml_file in glob.glob(input_xml_dir + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(float(root.find('size')[0].text)),
                     int(float(root.find('size')[1].text)),
                     member[0].text,
                     int(float(member[4][0].text)),
                     int(float(member[4][1].text)),
                     int(float(member[4][2].text)),
                     int(float(member[4][3].text))
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'x_min', 'y_min', 'x_max', 'y_max']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df
