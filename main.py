import os
import win32api
import win32gui
import win32comext.shell


# Windows message constants
LVM_FIRST = 4096
LVM_GETITEMCOUNT = LVM_FIRST + 4
LVM_SETITEMPOSITION = LVM_FIRST + 15
LVM_GETITEMPOSITION = LVM_FIRST + 16

# Find shell desktop handle
handle = win32gui.FindWindow("Progman", None)
handle = win32gui.FindWindowEx(handle, 0, "SHELLDLL_DefView", None)
handle = win32gui.FindWindowEx(handle, 0, "SysListView32", None)

# Enumerate WorkerW if SysListView32 is not found in Progman
def window_enumeration_handler(handle, desktop_handle):
    if win32gui.FindWindowEx(handle, 0, "SHELLDLL_DefView", None) != 0:
        shelldll_handle = win32gui.FindWindowEx(handle, 0, "SHELLDLL_DefView", None)
        if win32gui.FindWindowEx(shelldll_handle, 0, "SysListView32", None) != 0:
            desktop_handle.append(win32gui.FindWindowEx(shelldll_handle, 0, "SysListView32", None))

if handle == 0:
    desktop_handle = []
    handle = win32gui.FindWindow("WorkerW", None)
    win32gui.EnumWindows(window_enumeration_handler, desktop_handle)
    handle = desktop_handle[0]

item_count = win32api.SendMessage(handle, LVM_GETITEMCOUNT, 0, 0)

print (item_count)



# Input path to desktop
print("For example, C:/Users/John/Desktop ")
desktopPath = input("Enter your desktop path: ")

# Returns desktop files and directories
def walkLevel(some_dir, level=0):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

result = walkLevel(desktopPath)

for file in result:
    print (file)

exit (0)