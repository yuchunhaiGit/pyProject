import os
target_dir = ".\\backup\\"
del_command = "del /S /Q "+target_dir
if os.system(del_command)==0:
    print("All files have been deleted in",target_dir)
else:
    print("Deleting files failed!")

input("Press Enter to continue!")
