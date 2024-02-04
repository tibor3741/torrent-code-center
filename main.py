import tkinter as tk
from tkinter import messagebox
import pyperclip
from PIL import Image, ImageTk
import os

class CodeCenterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kód Központ")
        self.root.geometry("800x600")
        self.root.configure(bg='#000000')  # Fekete háttér

        # Adattag hozzáadása
        self.setup_data()
        self.setup_ui()

    def setup_data(self):
        self.data = {
            "Netflix": {"code": ".nf.", "icon": "netflix_logo.png"},
            "Amazon Prime Video": {"code": ".amzn.", "icon": "amazon_prime_video_logo.png"},
            "Disney Plus": {"code": ".dsnp.", "icon": "disney_logo.png"},
            "Hbo Max": {"code": ".hmax.", "icon": "hbo_logo.png"},
            "Sky Show Time": {"code":".skst.", "icon": "skyshowtime_logo.png"},
            "Hulu": {"code": ".hulu.", "icon": "hulu_logo.png"},
            "RTL Klub": {"code": ".rtlp.", "icon": "rtl_logo.png"},
            "TV2 Play": {"code": ".tv2.", "icon": "tv2_play_logo.png"},
        }

    def setup_ui(self):
        # Fő keret
        main_frame = tk.Frame(self.root, bg='#000000')  # Fekete háttér
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Háttérkép beállítása
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "Images", "wallpaper.jpg")
        background_image = Image.open(image_path)
        background_photo = ImageTk.PhotoImage(background_image)

        # Háttérkép widget
        background_label = tk.Label(main_frame, image=background_photo)
        background_label.image = background_photo
        background_label.place(relwidth=1, relheight=1)

        # Cím
        title_label = tk.Label(main_frame, text="Kód Központ", font=("Courier", 20, "bold"), fg='#00ff00', bg='#000000')  # Zöld szöveg, fekete háttér
        title_label.pack(pady=20)

        # Szolgáltatók gombjai tartalmazó Frame
        buttons_frame = tk.Frame(main_frame, bg='#000000')
        buttons_frame.pack()

        # Gombok és kódok listaszerű elrendezése
        row_count = 0
        col_count = 0
        for service, info in self.data.items():
            icon_path = os.path.join("Images", info["icon"])
            icon_image = Image.open(icon_path)
            icon_photo = ImageTk.PhotoImage(icon_image)

            button = tk.Button(buttons_frame, text=service, command=lambda s=service, c=info["code"]: self.update_selected_service(s, c), bg='#1a1a1a', fg='#00ff00', bd=1, relief=tk.FLAT, font=("Courier", 14), image=icon_photo, compound="top")
            button.image = icon_photo
            button.grid(row=row_count, column=col_count, pady=5, padx=10)

            col_count += 1
            if col_count == 4:
                col_count = 0
                row_count += 1

        # Kód megjelenítő
        self.code_label = tk.Label(main_frame, text="", font=("Courier", 14), fg='#00ff00', bg='#000000')  # Zöld szöveg, fekete háttér
        self.code_label.pack(pady=50)

        # Kilépés és Másolás gombok
        quit_button = tk.Button(main_frame, text="Kilépés", command=self.root.destroy, bg='#ff0000', fg='#ffffff', bd=0, padx=10, pady=5, font=("Courier", 12, "bold"))
        quit_button.place(relx=0.4, rely=0.95, anchor="s")

        copy_button = tk.Button(main_frame, text="Másolás", command=self.copy_to_clipboard, bg='#337ab7', fg='#ffffff', bd=0, padx=10, pady=5, font=("Courier", 12, "bold"))
        copy_button.place(relx=0.6, rely=0.95, anchor="s")
        # Időzítő változók
        self.right_click_triggered = False
        self.time_limit = 60000
        self.timer = None

    def update_selected_service(self, service, code):
        self.show_message(f"Sikeres kiválasztás - {service}", f"{service} kódjai megjelenítve")
        self.code_label.config(text=code)

    def show_message(self, title, message):
        # Törlés a címkéről
        self.clear_status()
        # Megjelenítés a címkén
        self.code_label.config(text=message)
        # Időzített törlés
        if self.timer:
            self.root.after_cancel(self.timer)
            self.timer = None
        self.timer = self.root.after(60000, self.clear_status)

    def clear_status(self):
        self.code_label.config(text="")

    def copy_to_clipboard(self):
        selected_code = self.code_label.cget("text")
        if selected_code:
            pyperclip.copy(selected_code)
            self.show_message("Sikeres másolás", f"{selected_code} másolva a vágólapra")

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeCenterApp(root)
    root.mainloop()
