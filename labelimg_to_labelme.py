import json
import xml.etree.ElementTree as ET


def main(input_xml_path, output_json_path):
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
