import os
import shutil

cwd = os.getcwd()  # Get the current working directory (cwd)
TS_DIR = 'ts'
with open('merged.ts', 'wb') as merged:
    for ts_file in os.listdir(f'{cwd}/{TS_DIR}'):
        with open(f'{cwd}/{TS_DIR}/{ts_file}', 'rb') as mergefile:
            shutil.copyfileobj(mergefile, merged)