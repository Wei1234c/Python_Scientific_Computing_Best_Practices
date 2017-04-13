import os
import json
 
for dirPath, dirNames, files in os.walk("."):  
    for file in files:
        file_path = os.path.join(dirPath, file)
        if file_path.endswith('.txt') or file_path.endswith('.csv'):
            try:
                with open(file_path, encoding = 'utf-8-sig') as f:
                    content = f.read()
                with open(file_path, 'w') as f:
                    f.write(content)
                print('successful', file_path)
            except Exception as e:
                print(e, file_path)