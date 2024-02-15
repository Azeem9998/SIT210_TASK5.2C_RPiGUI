import tkinter as tk
import RPi.GPIO as GPIO

class LightControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Light Control")

        self.RED_PIN = 17
        self.BLUE_PIN = 18
        self.GREEN_PIN = 27

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.RED_PIN, GPIO.OUT)
        GPIO.setup(self.BLUE_PIN, GPIO.OUT)
        GPIO.setup(self.GREEN_PIN, GPIO.OUT)

        self.led_states = {self.RED_PIN: False, self.BLUE_PIN: False, self.GREEN_PIN: False}

        self.create_widgets()

    def toggle_led_state(self, pin):
        self.led_states[pin] = not self.led_states[pin]
        GPIO.output(pin, self.led_states[pin])

    def exit_application(self):
        self.root.destroy()

    def create_widgets(self):
        self.heading_label = tk.Label(self.root, text="Light Control", font=("Helvetica", 24))
        self.heading_label.grid(row=0, column=0, columnspan=2, pady=20)

        self.button1 = tk.Button(self.root, text="RED", command=lambda: self.toggle_led_state(self.RED_PIN), bg="red", width=10, height=2)
        self.button2 = tk.Button(self.root, text="BLUE", command=lambda: self.toggle_led_state(self.BLUE_PIN), bg="blue", width=10, height=2)
        self.button3 = tk.Button(self.root, text="GREEN", command=lambda: self.toggle_led_state(self.GREEN_PIN), bg="green", width=10, height=2)

        self.button1.grid(row=1, column=0, pady=10)
        self.button2.grid(row=2, column=0, pady=10)
        self.button3.grid(row=3, column=0, pady=10)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_application, bg="gray", width=10, height=2)
        self.exit_button.grid(row=5, column=0, pady=10)

if __name__ == '__main__':
    root = tk.Tk()
    app = LightControlApp(root)
    root.mainloop()