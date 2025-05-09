import pyautogui as pg
import time
import keyboard
import threading
import pyperclip

r = "/rec"
l = "/l"
s = "/s"
stop = False

def escape():
    global stop
    while True:
        if keyboard.is_pressed('esc'):
            stop = True
            print("Выход")
            break
        time.sleep(0.1)

threading.Thread(target=escape, daemon=True).start()

response = pg.alert("Если хотите начать рекрутинг, нажмите ОК", "Serenity", button="ОК")
if response is None:
    exit()

message = pg.prompt("Введите текст для рекрутинга")
n_input = pg.prompt("Введите количество сообщений")
try:
    n = int(n_input)
except (TypeError, ValueError):
    pg.alert("Некорректный ввод")
    exit()

time.sleep(5)

def copy_to_clipboard(text):
    pyperclip.copy(text)

for _ in range(1, n + 1):
    if stop:
        break
    pg.press("enter")
    time.sleep(3)
    pg.write(r)
    time.sleep(3)
    pg.press("enter")
    time.sleep(3)
    pg.press("enter")
    time.sleep(3)
    copy_to_clipboard(message)
    time.sleep(3)
    pg.hotkey('ctrl', 'v')
    time.sleep(3)
    pg.press("enter")
    time.sleep(3)
    pg.press("enter")
    time.sleep(3)
    pg.write(l)
    time.sleep(3)
    pg.press("enter")
    time.sleep(3)
    pg.press("enter")
    time.sleep(3)
    copy_to_clipboard(message)
    time.sleep(3)
    pg.hotkey('ctrl', 'v')
    time.sleep(3)
    pg.press("enter")
    time.sleep(3)
    pg.press("enter")
    time.sleep(3)
    pg.write(s)
    time.sleep(3)
    pg.press("enter")
    time.sleep(3)
    pg.press("enter")
    time.sleep(3)
    copy_to_clipboard(message)
    time.sleep(3)
    pg.hotkey('ctrl', 'v')
    time.sleep(3)
    pg.press("enter")
    time.sleep(3)
    pg.press("enter")
    time.sleep(3)
    pg.write(s)
    time.sleep(3)
    pg.press("enter")
    time.sleep(3)
    pg.press("enter")
    time.sleep(3)
    copy_to_clipboard(message)
    time.sleep(3)
    pg.hotkey('ctrl', 'v')
    time.sleep(3)
    pg.press("enter")
    time.sleep(60)

pg.alert("Рекрутинг завершен", "Serenity")