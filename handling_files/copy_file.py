#copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directoru
# copy2() = copy() + copies metadata (file's creationa and modification times)

import shutil

shutil.copy2("C:\\Users\\lisha\\Desktop\\test_folder\\test.txt",
"C:\\Users\\lisha\\Desktop\\test_folder\\copy2.txt")   # src (str), dst (str)

