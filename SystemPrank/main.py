from kivy.app import App
from kivy.lang import Builder
from datetime import datetime
from kivy.clock import Clock
import random

PASSWORD = "Mypass1234@"

FILES = [
    "Documents/report.docx",
    "Desktop/passwords.txt",
    "Photos/family.jpg",
    "Downloads/project.zip",
    "Videos/movie.mp4",
    "Music/song.mp3"
]


class SystemPrank(App):

    def add_log(self, message):
        now = datetime.now().strftime("%H:%M:%S")
        self.root.ids.log.text += f"[{now}] {message}\n"

    def build(self):
        self.root = Builder.load_file("ui.kv")
        self.progress = 0
        Clock.schedule_interval(self.update, 0.15)
        return self.root

    def update(self, dt):
        if self.progress >= 100:
            self.root.ids.status.text = "SYSTEM LOCKED"
            self.root.ids.password_box.opacity = 1
            self.root.ids.password_box.disabled = False
            return False

        self.progress += random.randint(1, 3)
        self.progress = min(self.progress, 100)

        self.root.ids.progress.value = self.progress
        self.root.ids.percent.text = f"{self.progress}%"

        file = random.choice(FILES)
        self.root.ids.log.text += f"\nEncrypting {file}..."

        return True

    def check_password(self):
        entered = self.root.ids.password.text

        if entered == PASSWORD:
            self.root.ids.status.text = "ACCESS GRANTED"
            self.stop()
        else:
            self.root.ids.status.text = "ACCESS DENIED"
            self.root.ids.password.text = ""


if __name__ == "__main__":
    SystemPrank().run()