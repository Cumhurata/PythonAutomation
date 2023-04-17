from pathlib import Path
import time

folder_name = Path(__file__).absolute().parent;
fileName = time.strftime("%Y%m%d-%H%M%S") + ".txt"
folder_to_save_files = folder_name

f=open(fileName, 'x');
f=open(fileName, "r+");
f.truncate(0);
f.write("Caglar deneneme 112421");

