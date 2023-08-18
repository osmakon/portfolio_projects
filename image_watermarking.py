import tkinter.messagebox
from tkinter import *
import tkinter as tk
from tkinter import filedialog

# import os
#
# import sys
from PIL import Image, ImageTk, ImageDraw, ImageFont


class WatermarkApp:
    def __init__(self, title="Image Loader"):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.canvas = tk.Canvas(master=self.window, bg="white")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.btn_frm = Frame(master=self.window)
        self.btn_frm.grid(row=1, column=0, sticky="ew")
        self.open_btn = Button(
            master=self.btn_frm, text="Open", pady=5, padx=5, command=self.open_file
        )
        self.open_btn.grid(row=0, column=0, sticky="ew")
        self.save_btn = Button(
            master=self.btn_frm,
            text="Save",
            pady=5,
            padx=5,
            command=self.save_file,
            state="disabled",
        )
        self.save_btn.grid(row=0, column=1, sticky="ew")
        self.edit_btn = Button(
            master=self.btn_frm, text="Edit", padx=5, pady=5, command=self.add_mark
        )
        self.edit_btn.grid(row=0, column=2, sticky="ew")
        self.entry_btn = Entry(master=self.btn_frm)
        self.entry_btn.grid(row=0, column=3, sticky="ew")
        self.window.update()
        self.window.resizable(True, True)
        self.upload = None
        self.width = None
        self.height = None
        self.im = None
        self.edited = None
        self.output = None
        self.file_name = None

    def open_file(self):
        """Uploading the file to the canvas for viewing"""
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Image files", ["*.jpg", "*.jpeg", "*.png"]),
                ("All files", "*.*"),
            ]
        )

        if file_path:
            self.file_name = file_path.split("/")[-1].strip(".*")
            print(self.file_name)
            self.upload = tk.PhotoImage(file=file_path, master=self.window)
            self.width, self.height = self.upload.width(), self.upload.height()
            self.canvas.config(width=self.width, height=self.height)
            self.canvas.create_image(0, 0, image=self.upload, anchor=tk.NW)
            with Image.open(file_path).convert("RGBA") as base:
                self.im = base

    def save_file(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".png")
        with self.output as file:
            im = file.convert("RGB")
            im.save(filepath)
            tkinter.messagebox.showinfo(title="success", message="saved")
            self.save_btn.config(state="disabled")
            self.entry_btn.delete(0, END)

    def add_mark(self):
        """Adding the watermark text on the uploaded image"""
        insert_text = self.entry_btn.get()
        print(self.im.size)
        text = Image.new("RGBA", self.im.size, (255, 255, 255, 0))
        font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
        draw_text = ImageDraw.Draw(text)
        draw_text.text(
            (100, 350),
            f"{insert_text}",
            font=font,
            fill=(255, 255, 255, 255),
            align="center",
        )
        self.output = Image.alpha_composite(self.im, text)
        self.edited = ImageTk.PhotoImage(self.output)
        edited_w, edited_h = self.edited.width(), self.edited.height()
        self.canvas.config(width=edited_w, height=edited_h)
        self.canvas.create_image(0, 0, image=self.edited, anchor=tk.NW)
        self.save_btn.config(state="active")


if __name__ == "__main__":
    load_app = WatermarkApp()
    load_app.window.mainloop()
