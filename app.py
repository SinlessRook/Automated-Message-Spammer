import keyboard
import time
msg_send=input("Enter the Message to be sent:")
n=int(input("Enter the number of messages to be sent:"))
def spm(x,n=5):
    j=0
    while j!=n:
        j+=1
        for i in x:
            if keyboard.is_pressed("1"):
                return
            keyboard.press_and_release(i)
        if j==1:
            time.sleep(0.2)
        keyboard.press_and_release("enter")

while True:
    keyboard.add_hotkey('shift + .',spm, args =(msg_send,n))
    keyboard.wait("esc")
    keyboard.remove_hotkey('shift + .')
    msg_send=input("Enter the Message to be sent:")
    n=int(input("Enter the number of messages to be sent:"))
