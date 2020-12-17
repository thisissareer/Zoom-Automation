import keyboard, time, subprocess
import pandas as pd
from datetime import datetime
import pyautogui

df = pd.read_csv('meetingschedule.csv')
df_new = pd.DataFrame()

while(True):
    timestr = datetime.now().strftime("%H:%M")
    if timestr in df.Time.values:
        df_new = df[df['Time'].astype(str).str.contains(timestr)]

        #open Zoom
        subprocess.Popen("C:\\Users\\saree\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
        time.sleep(10)

        #LOCATE JOIN BUTTON ON THE SCREEN
        position = pyautogui.locateOnScreen("buttons\\join_button.png")
        pyautogui.moveTo(position)
        pyautogui.click()
        time.sleep(2)

        #WRITE THE MEETING ID
        keyboard.write(df_new.iloc[0,1])
        time.sleep(2)

        #CLICK THE JOIN BUTTTON 

        position = pyautogui.locateOnScreen("buttons\\join_button2.png")
        pyautogui.moveTo(position)
        pyautogui.click()
        time.sleep(2)

        #PUT IN THE PASSWORD FROM THE DATAFRAME
        keyboard.write(str(int(df_new.iloc[0,2])))
        time.sleep(3)

        #FINAL STEP TO CLICK ON THE JOIN BUTTON

        position = pyautogui.locateOnScreen("buttons\\join_button3.png")
        pyautogui.moveTo(position)
        pyautogui.click()


        #WAIT FOR ONE MINUTE BEFORE THE NEXT CLASS STARTS 

        time.sleep(60)





