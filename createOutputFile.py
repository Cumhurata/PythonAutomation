import os
import pathlib
from pathlib import Path
import time
import datetime

folder_name = Path(__file__).absolute().parent;
fileName = time.strftime("%Y%m%d-%H%M%S") + ".txt"
folder_to_save_files = folder_name

f=open(fileName, 'x');
f=open(fileName, "r+");
f.truncate(0);
f.write("Caglar deneneme 1124");
t=open("C:\\Users\\Cumhur Ata\\PycharmProjects\\PythonAutomation\outputfile.txt", "r");
print(t.read);
# os_path = pathlib.Path(__file__).parent.resolve(); print(os_path); os_path = os_path + "//outputs"; print(os_path);

# IF no such folder exists, create one automatically
# if not os.path.exists(folder_to_save_files):
   # os.mkdir(folder_to_save_files)

