import tkinter as tk
from tkinter import messagebox
import pyperclip

class StreamingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Torrent Kódközpont")

        self.data = {
            "Netflix": ".nf.",
            "Amazon Prime": ".amzn.",
            "Hbo Max": ".hmax.",
            "Disney Plus": ".dsnp.",
            "Sky Show Time": ".skst.",
            "HULU": ".hulu.",  
            "Tv2": ".tv2.",
            "RTL PLUSZ": ".rtlp."
        }

        self.setup_ui()

    def setup_ui(self):
        # Fő cím
        title_label = tk.Label(self.root, text="Streaming Szolgáltatások és Kódjaik", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.setup_listbox(1, 0)
        self.setup_listbox(1, 1, width=10)

        self.setup_scrollbars()
        self.setup_exit_button()

        self.disable_elements_without_dot(None)

        # Egy változó a jobb kattintás követéséhez
        self.right_click_triggered = False

        # Az időkorlát (60 másodperc) beállítása
        self.time_limit = 60000

        # Az időzítő inicializálása
        self.timer = None

        # Az események hozzárendelése
        self.table2.bind("<Button-1>", self.left_click_handler)
        self.table2.bind("<Button-3>", self.right_click_handler)

        # Státusz sor
        self.status_label = tk.Label(self.root, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.grid(row=3, column=0, columnspan=2, sticky=tk.W + tk.E)

    def setup_listbox(self, row, column, **kwargs):
        listbox = tk.Listbox(
            self.root,
            selectmode="browse",
            exportselection=0,
            justify="center",
            font=("Helvetica", 20),
            selectbackground="black",
            foreground="black",
            bg="white",
            **kwargs
        )

        listbox.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)
        listbox.bind("<Button-1>", self.handle_first_row_selection)

        if column == 1:
            listbox.bind("<Button-1>", self.disable_elements_without_dot)

        setattr(self, f"table{column + 1}", listbox)
        self.root.grid_columnconfigure(column, weight=1)

        for item in self.data.keys():
            getattr(self, f"table{column + 1}").insert(tk.END, item)

    def setup_scrollbars(self):
        scrollbar1 = tk.Scrollbar(self.root, command=self.table1.yview)
        scrollbar1.grid(row=1, column=0, sticky='nse')
        self.table1.configure(yscrollcommand=scrollbar1.set)

        scrollbar2 = tk.Scrollbar(self.root, command=self.table2.yview)
        scrollbar2.grid(row=1, column=1, sticky='nse')
        self.table2.configure(yscrollcommand=scrollbar2.set)

    def setup_exit_button(self):
        quit_button = tk.Button(self.root, text="Kilépés", command=self.root.destroy)
        quit_button.grid(row=2, column=0, columnspan=2, pady=10)

    def handle_first_row_selection(self, event):
        selected_item_index = self.table1.nearest(event.y)
        selected_item = self.table1.get(selected_item_index)

        if selected_item and selected_item in self.data:
            self.table2.delete(0, tk.END)
            self.table2.insert(tk.END, self.data[selected_item])
            self.show_message("Sikeres kiválasztás", f"{selected_item} kódjai megjelenítve")

        return "break"

    def disable_elements_without_dot(self, event):
        self.table2.selection_clear(0, tk.END)
        self.table2.delete(0, tk.END)

    def show_message(self, title, message):
        self.status_label.config(text=message)
        self.root.after(60000, self.clear_status)  # Törölje a státusz sort 60 másodperc után

    def clear_status(self):
        self.status_label.config(text="")  # Törölje a státusz sort

    def left_click_handler(self, event):
        # Bal kattintás esetén megszakítjuk az időzítőt
        self.reset_timer()

    def right_click_handler(self, event):
        # Jobb kattintás esetén elindítjuk az időzítőt
        self.start_timer()

    def start_timer(self):
        # Az időzítő indítása
        self.timer = self.root.after(self.time_limit, self.timeout_handler)

    def reset_timer(self):
        # Az időzítő újraindítása
        if self.timer:
            self.root.after_cancel(self.timer)
            self.timer = None

    def timeout_handler(self):
        # Időkorlát lejártakor végrehajtandó műveletek
        if not self.right_click_triggered:
            self.show_message("Figyelem", "Nyomj jobb kattintást 60 másodpercig!")
        else:
            # Ha sikerült másolni a kódot, akkor üzenetet jelenítünk meg
            self.show_message("Sikeres másolás", "Kód másolva a vágólapra!")

    def copy_to_clipboard(self):
        selected_items = [item for item in self.table2.get(0, tk.END) if item.startswith(".")]
        if selected_items:
            joined_items = " ".join(selected_items)
            pyperclip.copy(joined_items)
            self.show_message("Sikeres másolás", f"{joined_items} másolva a vágólapra")

if __name__ == "__main__":
    root = tk.Tk()
    app = StreamingApp(root)

    # Gomb a kód másolásához
    copy_button = tk.Button(root, text="Kód másolása", command=app.copy_to_clipboard)
    copy_button.grid(row=4, column=0, columnspan=2, pady=10)

    root.mainloop()