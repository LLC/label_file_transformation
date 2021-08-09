import json
import xml.etree.ElementTree as ET


def xml_to_json(xml_path):
    """
    Args:
        xml_path: full input path of xml label file
            e.g., /LLC/Downloads/test.xml

    Returns:
        json_output: label file in json type
    """
    tree = ET.parse(xml_path)
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
    return json_output


def save_json_file(output_path):
    """
    將 json 格式的內容存成 json file (.json)
    """
    with open(output_path, 'w') as f:
        json.dump(output_path, f, indent=4)
