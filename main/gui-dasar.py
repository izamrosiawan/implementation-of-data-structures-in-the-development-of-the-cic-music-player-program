import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# App utama
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CIC Music Player")
        self.geometry("1100x650")

        # Container untuk halaman
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        for F in (PageMenu, PageUser, PageAdmin):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.show_frame(PageMenu)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


# Halaman 1 — Menu (Pengguna / Admin)
class PageMenu(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        ctk.CTkLabel(self, text="Selamat Datang di CIC Player",
                    font=("Arial", 22, "bold")).pack(pady=50)

        ctk.CTkButton(self, text="Masuk sebagai User",
                    width=300, command=lambda: controller.show_frame(PageUser)).pack(pady=20)

        ctk.CTkButton(self, text="Masuk sebagai Admin",
                    width=300, command=lambda: controller.show_frame(PageAdmin)).pack(pady=20)


# Halaman 2 — Halaman Pengguna (versi perbaikan)
class PageUser(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

    # Tombol 'Kembali' untuk kembali ke menu utama
        ctk.CTkButton(self, text="Kembali",
                    width=100, command=lambda: controller.show_frame(PageMenu)).place(x=10, y=10)

    # Kiri — Playlist (daftar putar pengguna)
        self.frame_playlist = ctk.CTkFrame(self, width=250, height=500, corner_radius=10)
        self.frame_playlist.place(x=10, y=60)

        ctk.CTkLabel(self.frame_playlist, text="Playlist", font=("Arial", 14, "bold")).place(x=10, y=10)
        self.playlist_box = ctk.CTkTextbox(self.frame_playlist, width=230, height=440)
        self.playlist_box.place(x=10, y=50)

    # Tengah — Daftar lagu (koleksi)
        self.frame_library = ctk.CTkFrame(self, width=350, height=500, corner_radius=10)
        self.frame_library.place(x=270, y=60)

        ctk.CTkLabel(self.frame_library, text="Daftar Lagu", font=("Arial", 14, "bold")).place(x=10, y=10)
        self.library_box = ctk.CTkTextbox(self.frame_library, width=330, height=440)
        self.library_box.place(x=10, y=50)

    # Kanan — Info lagu / album (detail)
        self.frame_info = ctk.CTkFrame(self, width=450, height=500, corner_radius=10)
        self.frame_info.place(x=630, y=60)

        ctk.CTkLabel(self.frame_info, text="Info Lagu / Album", font=("Arial", 14, "bold")).place(x=10, y=10)
        self.info_label = ctk.CTkLabel(self.frame_info, text="Tidak ada lagu diputar", anchor="w")
        self.info_label.place(x=10, y=50)

    # Bawah — Kontrol pemutar
        self.frame_control = ctk.CTkFrame(self, width=1070, height=70)
        self.frame_control.place(x=10, y=570)

        self.current_label = ctk.CTkLabel(self.frame_control, text="Lagu yang sedang diputar:")
        self.current_label.pack(pady=5)

        control_btns = ctk.CTkFrame(self.frame_control, fg_color="transparent")
        control_btns.pack()

        ctk.CTkButton(control_btns, text="Play", width=120).grid(row=0, column=0, padx=10)
        ctk.CTkButton(control_btns, text="Next", width=120).grid(row=0, column=1, padx=10)
        ctk.CTkButton(control_btns, text="Previous", width=120).grid(row=0, column=2, padx=10)


# Halaman 3 — Halaman Admin (versi perbaikan)
class PageAdmin(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        ctk.CTkButton(self, text="Kembali",
                    width=100, command=lambda: controller.show_frame(PageMenu)).place(x=10, y=10)

    # Kiri — Menu Admin (aksi pengelolaan lagu)
        self.frame_admin_menu = ctk.CTkFrame(self, width=250, height=500, corner_radius=10)
        self.frame_admin_menu.place(x=10, y=60)

        ctk.CTkLabel(self.frame_admin_menu, text="Admin Menu", font=("Arial", 14, "bold")).place(x=10, y=10)

    # Tombol operasi admin (tambah / hapus / update / lihat)
        ctk.CTkButton(self.frame_admin_menu, text="Tambah Lagu", width=200).place(x=25, y=60)
        ctk.CTkButton(self.frame_admin_menu, text="Hapus Lagu", width=200).place(x=25, y=110)
        ctk.CTkButton(self.frame_admin_menu, text="Update Lagu", width=200).place(x=25, y=160)


    # Tengah — Daftar lagu (Library)
        self.frame_library = ctk.CTkFrame(self, width=350, height=500, corner_radius=10)
        self.frame_library.place(x=270, y=60)

        ctk.CTkLabel(self.frame_library, text="Library Lagu", font=("Arial", 14, "bold")).place(x=10, y=10)
        self.library_box = ctk.CTkTextbox(self.frame_library, width=330, height=440)
        self.library_box.place(x=10, y=50)


    # Kanan — Detail lagu dan form untuk admin
        self.frame_detail = ctk.CTkFrame(self, width=450, height=500, corner_radius=10)
        self.frame_detail.place(x=630, y=60)

        ctk.CTkLabel(self.frame_detail, text="Detail Lagu / Form Admin",
                    font=("Arial", 14, "bold")).place(x=10, y=10)

        self.detail_box = ctk.CTkTextbox(self.frame_detail, width=430, height=440)
        self.detail_box.place(x=10, y=50)


    # Bawah — Panel kontrol admin
        self.frame_control = ctk.CTkFrame(self, width=1070, height=70)
        self.frame_control.place(x=10, y=570)

        ctk.CTkLabel(self.frame_control, text="Admin Action Panel").pack(pady=5)

        button_frame = ctk.CTkFrame(self.frame_control, fg_color="transparent")
        button_frame.pack()

        ctk.CTkButton(button_frame, text="Simpan", width=120).grid(row=0, column=0, padx=10)
        ctk.CTkButton(button_frame, text="Update", width=120).grid(row=0, column=1, padx=10)
        ctk.CTkButton(button_frame, text="Hapus", width=120).grid(row=0, column=2, padx=10)



# Jalankan aplikasi
app = App()
app.mainloop()
