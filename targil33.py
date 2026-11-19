import time
import win32clipboard
import win32con


def get_clipboard_text():
    text = ""
    try:
        win32clipboard.OpenClipboard()
        if win32clipboard.IsClipboardFormatAvailable(win32con.CF_UNICODETEXT):
            text = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
    except Exception as e:
        pass
    finally:
        try:
            win32clipboard.CloseClipboard()
        except Exception:
            pass

    return text


def monitor_clipboard():
    last_text = ""
    while True:
        current_text = get_clipboard_text()
        if current_text and current_text != last_text:
            last_text = current_text
            print(f"\nהועתק טקסט חדש:\n{current_text}")
            print("-" * 30)
        time.sleep(0.5)


if __name__ == "__main__":
    monitor_clipboard()