import win32gui



# פונקציית callback שמופעלת עבור כל חלון שנמצא על ידי EnumWindows
def window_callback(hwnd, extra):
    # בדיקה אם החלון גלוי למשתמש (מסנן חלונות נסתרים או רקע שאינם נראים)
    if win32gui.IsWindowVisible(hwnd):
        # שליפת כותרת החלון (Title) לפי מזהה החלון (HWND)
        title = win32gui.GetWindowText(hwnd)
        # הדפסה רק אם לחלון יש כותרת לא ריקה
        if title:
            print(f"HWND: {hwnd} | Title: {title}")


# הדפסת כותרת פתיחה וקו מפריד
print("רשימת החלונות הפתוחים:")
print("-" * 40)

# מעבר על כל החלונות העליונים (Top-level windows) במערכת והפעלת window_callback על כל אחד
win32gui.EnumWindows(window_callback, None)