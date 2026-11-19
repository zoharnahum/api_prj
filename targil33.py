import time
import win32clipboard
import win32con


def get_clipboard_text():
    '''
    :return:מחזיר מחרוזת עם תוכן הלוח או מחרוזת ריקה במקרה של שגיאה / היעדר טקסט
    '''
    text = ""
    try:
        win32clipboard.OpenClipboard()
        if win32clipboard.IsClipboardFormatAvailable(win32con.CF_UNICODETEXT):
            text = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
    except Exception as e:
        pass
    try:
        win32clipboard.CloseClipboard()
    except Exception as e:
        pass
    return text


def monitor_clipboard():
    '''
    :return: none
     עוקב אחר שינויים בלוח העתיק ומדפיסה כל טקסט חדש שהועתק
    '''
    last_text = ""
    while True:
        current_text = get_clipboard_text()
        if current_text and current_text != last_text:
            last_text = current_text
            print(current_text)
        time.sleep(0.5)



if __name__ == "__main__":
    monitor_clipboard()