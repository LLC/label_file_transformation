# label_file_transformation

## labelimg_to_labelme

- 將 Labelimg 的 label 檔 (.xml) 無痛轉成 Labelme 的 label 檔 (.json)

### How to use this code
```
from labelimg_tools import labelimg_to_labelme


labelimg_to_labelme(
    input_xml_path='./examples/test_001.xml',
    output_json_path='./examples/test_001.json'
)
```

- use labelimg to read xml file
![Alt text](https://i.imgur.com/ip8yLby.png "Optional title")

- use labelme to read json file
![Alt text](https://i.imgur.com/Gou9OkJ.png "Optional title")

## labelimg_to_df

- 將 Labelimg 的 label 檔 (.xml) 無痛轉成 DataFrame

### How to use this code
```
from labelimg_tools import labelimg_to_df


labelimg_to_df(
    input_xml_dir='./examples/'
)
```

