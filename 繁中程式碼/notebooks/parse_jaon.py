import os
import json
 
for dirPath, dirNames, files in os.walk("."):  
    for file in files:
        file_path = os.path.join(dirPath, file)
        if file_path.endswith('.ipynb'):
            try:
                with open(file_path, encoding = 'utf-8-sig') as f:
                    json_text = json.load(f)
                with open(file_path, 'w') as f:
                    json.dump(json_text, f)
                print('successful', file_path)
            except Exception as e:
                print(e, file_path)