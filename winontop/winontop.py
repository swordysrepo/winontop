import sys
### added for Select
import win32gui
import time
import win32con
####
def enumHandler(hwnd, lParam):
    """The windows on top functionality is taken here
    Source: http://stackoverflow.com/questions/1482565/how-to-make-python-window-run-as-always-on-top"""
    if win32gui.IsWindowVisible(hwnd):
        if sys.argv[1].lower() in win32gui.GetWindowText(hwnd).lower():
            win32gui.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0001)
            return True


def showDoc():
    print(
        """Help Documentation
Hey folks this is an easy to use tool to keep windows on top of others.
You have to specify only a part of the name in windows name. No need to install any third party software.
If you want a chrome tab to be on top just mention any word in the title.

For eg. if you want youtube video "Game of Thrones Season 6: Episode #9 Preview (HBO)" on top
>>> winontop thrones
or
>>> winontop games

or to select bring to front the currently selected window

>>> winontop Select


For help doc
>>> winontop -h

Tested on Windows 10/Python2
Feel free to contribute or report any issues at https://github.com/jithurjacob/winontop"""
        )

def main():
    """
    Argument Parsing and help documentation
    """
    if len(sys.argv) != 2:
        print("Incorrect number of arguments. Use -h for help")
    else:
        if sys.argv[1] in ["-h", "--h", "-help"]:
            showDoc()
        elif sys.argv[1] in ["select", "Select"]: 
            
  
        else:
            win32gui.EnumWindows(enumHandler, None)
 
 
 
 def Select_window():
'''
 '''

print("Select the window to bring to front ")


loading = True  # a simple var to keep the loading status
loading_speed = 4  # number of characters to print out per second
loading_string = "." * 6  # characters to print out one by one (6 dots in this example)
loading_seconds = 0 #4 seconds to load 

while loading_seconds < 4:
    loading_seconds += 1
    #  track both the current character and its index for easier backtracking later
    for index, char in enumerate(loading_string):
        # you can check your loading status here
        # if the loading is done set `loading` to false and break
        sys.stdout.write(char)  # write the next char to STDOUT
        sys.stdout.flush()  # flush the output
        time.sleep(1.0 / loading_speed)  # wait to match our speed
    index += 1  # lists are zero indexed, we need to increase by one for the accurate count
    sys.stdout.flush()  # flush the output
activewindow=win32gui.GetForegroundWindow()
print(f" \n set window to top (process id : {activewindow})\
    \
    ")
win32gui.SetWindowPos(activewindow, win32con.HWND_TOPMOST, 900, 100, 800, 800, 0) #these last are position pixel x, y.. then size width ,height.

     
if __name__ == '__main__':
    main()
