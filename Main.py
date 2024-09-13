import webbrowser
import obswebsocket
from obswebsocket import requests
from tkinter import Tk, Button, Label, Frame

# OBS WebSocket connection settings
OBS_HOST = 'localhost'
OBS_PORT = 4455
OBS_PASSWORD = '123456'  # Set this in the WebSocket plugin settings

# Create OBS WebSocket client
client = obswebsocket.obsws(OBS_HOST, OBS_PORT, OBS_PASSWORD)

def start_recording():
    try:
        response = client.call(requests.StartRecord())
        if response.status == obswebsocket.constants.OBSWebSocketStatus.SUCCESS:
            print("Recording started!")
        else:
            print(f"Failed to start recording: {response.error}")
    except Exception as e:
        print(f"Error starting recording: {e}")

def stop_recording():
    try:
        response = client.call(requests.StopRecord())
        if response.status == obswebsocket.constants.OBSWebSocketStatus.SUCCESS:
            print("Recording stopped!")
        else:
            print(f"Failed to stop recording: {response.error}")
    except Exception as e:
        print(f"Error stopping recording: {e}")

def open_browser_game():
    webbrowser.open('https://www.youtube.com/')  # Replace with the URL of your browser game
    print("Browser game started!")

def start_all():
    try:
        client.connect()
        start_recording()
        open_browser_game()
    except Exception as e:
        print(f"Error: {e}")

def stop_all_and_exit():
    try:
        stop_recording()
    finally:
        client.disconnect()
        root.quit()  # Exit the Tkinter application

# Create a simple GUI
root = Tk()
root.title("OBS and Game Control")

# Create a frame to hold the content
frame = Frame(root, padx=100, pady=100)
frame.pack(padx=100, pady=100)

# Add a label
label = Label(frame, text="Control OBS and Start Game", font=('Arial', 14))
label.pack(pady=10)

# Add a button to start recording, open the browser game
start_button = Button(frame, text="Start Recording and Game", command=start_all, width=30)
start_button.pack(pady=10)

# Add a button to stop recording and exit
end_button = Button(frame, text="Stop Recording and Exit", command=stop_all_and_exit, width=30)
end_button.pack(pady=10)

root.mainloop()
