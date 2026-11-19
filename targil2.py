import win32gui

def window_callback(hwnd, extra):
    #בדיקה האם החלון גלוי למשתמש
    if win32gui.IsWindowVisible(hwnd):
        # שליפת כותרת החלון לפי מזהה החלון
        title = win32gui.GetWindowText(hwnd)
        # הדפסה רק אם לחלון יש כותרת לא ריקה
        if title:
            print(f"HWND: {hwnd} | Title: {title}")



print("רשימת החלונות הפתוחים:")
win32gui.EnumWindows(window_callback, None)