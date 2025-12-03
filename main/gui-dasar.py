import customtkinter as ctk
from sistem import MusicPlayer
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Spotify Color Scheme
SPOTIFY_BLACK = "#121212"
SPOTIFY_DARK_GRAY = "#181818"
SPOTIFY_GRAY = "#282828"
SPOTIFY_GREEN = "#1DB954"
SPOTIFY_WHITE = "#FFFFFF"
SPOTIFY_LIGHT_GRAY = "#B3B3B3"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.player = MusicPlayer()
        
        # Menambahkan banyak lagu contoh dengan berbagai artis dan album
        self.setup_library()
        
        self.title("CIC Music Player - Spotify Theme")
        self.geometry("1200x700")
        self.configure(fg_color=SPOTIFY_BLACK)
        self.container = ctk.CTkFrame(self, fg_color=SPOTIFY_BLACK)
        self.container.pack(fill="both", expand=True)
        self.frames = {}
        for F in (PageMenu, PageUser, PageAdmin):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.place(x=0, y=0, relwidth=1, relheight=1)
        self.show_frame(PageMenu)

    def setup_library(self):
        """Setup library dengan banyak lagu contoh"""
        music_dir = os.path.join(os.path.dirname(__file__), "music")
        
        # Pop Artists
        taylor = self.player.library.add_artist("Taylor Swift")
        album1 = taylor.add_album("1989")
        album1.add_song(1, "Shake It Off", "3:39", os.path.join(music_dir, "song1.mp3"))
        album1.add_song(2, "Blank Space", "3:51", os.path.join(music_dir, "song2.mp3"))
        album1.add_song(3, "Style", "3:51", os.path.join(music_dir, "song3.mp3"))
        
        ed = self.player.library.add_artist("Ed Sheeran")
        album2 = ed.add_album("÷ (Divide)")
        album2.add_song(4, "Shape of You", "3:53", os.path.join(music_dir, "song4.mp3"))
        album2.add_song(5, "Perfect", "4:23", os.path.join(music_dir, "song5.mp3"))
        album2.add_song(6, "Castle on the Hill", "4:21", os.path.join(music_dir, "song6.mp3"))
        
        # Rock Artists
        coldplay = self.player.library.add_artist("Coldplay")
        album3 = coldplay.add_album("A Head Full of Dreams")
        album3.add_song(7, "Adventure of a Lifetime", "4:23", os.path.join(music_dir, "song7.mp3"))
        album3.add_song(8, "Hymn for the Weekend", "4:18", os.path.join(music_dir, "song8.mp3"))
        
        imagine = self.player.library.add_artist("Imagine Dragons")
        album4 = imagine.add_album("Evolve")
        album4.add_song(9, "Believer", "3:24", os.path.join(music_dir, "song9.mp3"))
        album4.add_song(10, "Thunder", "3:07", os.path.join(music_dir, "song10.mp3"))
        album4.add_song(11, "Whatever It Takes", "3:21", os.path.join(music_dir, "song11.mp3"))
        
        # Hip Hop/R&B
        weeknd = self.player.library.add_artist("The Weeknd")
        album5 = weeknd.add_album("Starboy")
        album5.add_song(12, "Starboy", "3:50", os.path.join(music_dir, "song12.mp3"))
        album5.add_song(13, "I Feel It Coming", "4:29", os.path.join(music_dir, "song13.mp3"))
        
        bruno = self.player.library.add_artist("Bruno Mars")
        album6 = bruno.add_album("24K Magic")
        album6.add_song(14, "24K Magic", "3:46", os.path.join(music_dir, "song14.mp3"))
        album6.add_song(15, "That's What I Like", "3:26", os.path.join(music_dir, "song15.mp3"))
        
        # Alternative/Indie
        billie = self.player.library.add_artist("Billie Eilish")
        album7 = billie.add_album("When We All Fall Asleep")
        album7.add_song(16, "bad guy", "3:14", os.path.join(music_dir, "song16.mp3"))
        album7.add_song(17, "when the party's over", "3:16", os.path.join(music_dir, "song17.mp3"))
        
        # Electronic
        marshmello = self.player.library.add_artist("Marshmello")
        album8 = marshmello.add_album("Joytime III")
        album8.add_song(18, "Happier", "3:34", os.path.join(music_dir, "song18.mp3"))
        album8.add_song(19, "Alone", "4:33", os.path.join(music_dir, "song19.mp3"))
        
        # Classic
        beatles = self.player.library.add_artist("The Beatles")
        album9 = beatles.add_album("Abbey Road")
        album9.add_song(20, "Come Together", "4:19", os.path.join(music_dir, "song20.mp3"))
        album9.add_song(21, "Here Comes the Sun", "3:05", os.path.join(music_dir, "song21.mp3"))

    def show_frame(self, page):
        self.frames[page].tkraise()

class PageMenu(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color=SPOTIFY_BLACK)
        
        # Logo/Title dengan style lebih menarik
        title_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_frame.pack(pady=80)
        
        ctk.CTkLabel(title_frame, text="🎵", font=("Arial", 60)).pack()
        ctk.CTkLabel(title_frame, text="CIC Music Player", font=("Arial", 32, "bold"), text_color=SPOTIFY_WHITE).pack(pady=10)
        ctk.CTkLabel(title_frame, text="Experience Music Like Never Before", font=("Arial", 14), text_color=SPOTIFY_LIGHT_GRAY).pack()
        
        # Buttons dengan style lebih modern
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=40)
        
        ctk.CTkButton(button_frame, text="🎧 Masuk sebagai Pengguna", width=350, height=50, 
                    font=("Arial", 16, "bold"), corner_radius=25,
                    command=lambda: controller.show_frame(PageUser), 
                    fg_color=SPOTIFY_GREEN, hover_color="#1ed760", text_color=SPOTIFY_WHITE).pack(pady=15)
        
        ctk.CTkButton(button_frame, text="⚙️ Masuk sebagai Admin", width=350, height=50,
                    font=("Arial", 16, "bold"), corner_radius=25,
                    command=lambda: controller.show_frame(PageAdmin), 
                    fg_color=SPOTIFY_GRAY, hover_color="#3E3E3E", text_color=SPOTIFY_WHITE).pack(pady=15)

class PageUser(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color=SPOTIFY_BLACK)
        
        # Header dengan tombol kembali dan search
        header = ctk.CTkFrame(self, height=60, fg_color=SPOTIFY_DARK_GRAY, corner_radius=0)
        header.pack(fill="x", padx=0, pady=0)
        
        ctk.CTkButton(header, text="← Kembali", width=100, height=35, corner_radius=20,
                    command=lambda: controller.show_frame(PageMenu), 
                    fg_color=SPOTIFY_GRAY, hover_color="#3E3E3E").place(x=15, y=12)

        # Search bar di header
        self.search_entry = ctk.CTkEntry(header, width=400, height=35, corner_radius=20,
                                        placeholder_text="🔍 Cari lagu, artis, atau album...",
                                        fg_color=SPOTIFY_GRAY, border_color=SPOTIFY_GRAY, 
                                        text_color=SPOTIFY_WHITE)
        self.search_entry.place(x=400, y=12)
        self.search_entry.bind("<Return>", lambda e: self.search_songs(controller))
        
        # Main content area
        content = ctk.CTkFrame(self, fg_color=SPOTIFY_BLACK)
        content.pack(fill="both", expand=True, padx=15, pady=(10, 100))
        
        # Left: Playlist
        self.frame_playlist = ctk.CTkFrame(content, width=380, corner_radius=15, fg_color=SPOTIFY_DARK_GRAY)
        self.frame_playlist.pack(side="left", fill="both", expand=True, padx=(0, 8))
        
        playlist_header = ctk.CTkFrame(self.frame_playlist, height=50, fg_color=SPOTIFY_GRAY, corner_radius=10)
        playlist_header.pack(fill="x", padx=10, pady=10)
        ctk.CTkLabel(playlist_header, text="📋 Playlist Saya", font=("Arial", 16, "bold"), 
                    text_color=SPOTIFY_WHITE).pack(side="left", padx=15, pady=10)
        
        self.playlist_box = ctk.CTkTextbox(self.frame_playlist, fg_color=SPOTIFY_GRAY, 
                                        text_color=SPOTIFY_WHITE, border_color=SPOTIFY_DARK_GRAY,
                                        corner_radius=10, font=("Consolas", 11))
        self.playlist_box.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        self.playlist_box.configure(state="disabled")

        # Middle: Library
        self.frame_library = ctk.CTkFrame(content, width=380, corner_radius=15, fg_color=SPOTIFY_DARK_GRAY)
        self.frame_library.pack(side="left", fill="both", expand=True, padx=8)
        
        library_header = ctk.CTkFrame(self.frame_library, height=50, fg_color=SPOTIFY_GRAY, corner_radius=10)
        library_header.pack(fill="x", padx=10, pady=10)
        ctk.CTkLabel(library_header, text="🎵 Daftar Lagu", font=("Arial", 16, "bold"), 
                    text_color=SPOTIFY_WHITE).pack(side="left", padx=15, pady=10)
        
        self.library_box = ctk.CTkTextbox(self.frame_library, fg_color=SPOTIFY_GRAY, 
                                        text_color=SPOTIFY_WHITE, border_color=SPOTIFY_DARK_GRAY,
                                        corner_radius=10, font=("Consolas", 11))
        self.library_box.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        self.library_items = []
        self.selected_index = None
        self.refresh_library(controller)

        # Right: Playlist Actions
        self.frame_playlist_action = ctk.CTkFrame(content, width=380, corner_radius=15, fg_color=SPOTIFY_DARK_GRAY)
        self.frame_playlist_action.pack(side="left", fill="both", expand=True, padx=(8, 0))
        
        action_header = ctk.CTkFrame(self.frame_playlist_action, height=50, fg_color=SPOTIFY_GRAY, corner_radius=10)
        action_header.pack(fill="x", padx=10, pady=10)
        ctk.CTkLabel(action_header, text="⚡ Kelola Playlist", font=("Arial", 16, "bold"), 
                    text_color=SPOTIFY_WHITE).pack(side="left", padx=15, pady=10)
        
        action_content = ctk.CTkFrame(self.frame_playlist_action, fg_color="transparent")
        action_content.pack(fill="both", expand=True, padx=15, pady=10)
        
        ctk.CTkLabel(action_content, text="ID Lagu:", font=("Arial", 12), 
                    text_color=SPOTIFY_LIGHT_GRAY).pack(anchor="w", pady=(10, 5))
        self.song_id_entry = ctk.CTkEntry(action_content, height=35, corner_radius=10,
                                        placeholder_text="Masukkan ID...",
                                        fg_color=SPOTIFY_GRAY, border_color=SPOTIFY_GRAY, 
                                        text_color=SPOTIFY_WHITE)
        self.song_id_entry.pack(fill="x", pady=(0, 15))
        
        ctk.CTkButton(action_content, text="➕ Tambah ke Playlist", height=40, corner_radius=10,
                    command=lambda: self.add_to_playlist(controller), 
                    fg_color=SPOTIFY_GREEN, hover_color="#1ed760", 
                    font=("Arial", 13, "bold")).pack(fill="x", pady=5)
        
        ctk.CTkButton(action_content, text="➖ Hapus dari Playlist", height=40, corner_radius=10,
                    command=lambda: self.remove_from_playlist(controller), 
                    fg_color=SPOTIFY_GRAY, hover_color="#3E3E3E",
                    font=("Arial", 13, "bold")).pack(fill="x", pady=5)
        
        ctk.CTkButton(action_content, text="🗑️ Kosongkan Playlist", height=40, corner_radius=10,
                    command=lambda: self.clear_playlist(controller), 
                    fg_color="#8B0000", hover_color="#A52A2A",
                    font=("Arial", 13, "bold")).pack(fill="x", pady=5)
        
        self.status_label = ctk.CTkLabel(action_content, text="", font=("Arial", 11),
                                        text_color=SPOTIFY_GREEN, wraplength=300)
        self.status_label.pack(pady=15)

        # Bottom: Player Controls (Fixed at bottom)
        self.frame_control = ctk.CTkFrame(self, height=90, fg_color=SPOTIFY_DARK_GRAY, corner_radius=0)
        self.frame_control.pack(side="bottom", fill="x", padx=0, pady=0)
        
        # Now Playing Label
        self.current_label = ctk.CTkLabel(self.frame_control, text="▶️ Tidak ada lagu yang diputar", 
                                        font=("Arial", 13, "bold"), text_color=SPOTIFY_WHITE)
        self.current_label.pack(pady=(10, 5))
        
        # Control Buttons
        control_btns = ctk.CTkFrame(self.frame_control, fg_color="transparent")
        control_btns.pack()
        
        ctk.CTkButton(control_btns, text="⏮️", width=60, height=40, corner_radius=20,
                    command=lambda: self.previous_song(controller), 
                    fg_color=SPOTIFY_GRAY, hover_color="#3E3E3E",
                    font=("Arial", 16)).grid(row=0, column=0, padx=5)
        
        ctk.CTkButton(control_btns, text="▶️ Putar", width=120, height=40, corner_radius=20,
                    command=lambda: self.play_selected(controller), 
                    fg_color=SPOTIFY_GREEN, hover_color="#1ed760",
                    font=("Arial", 14, "bold")).grid(row=0, column=1, padx=5)
        
        ctk.CTkButton(control_btns, text="⏸️", width=60, height=40, corner_radius=20,
                    command=lambda: self.pause_resume(controller), 
                    fg_color=SPOTIFY_GRAY, hover_color="#3E3E3E",
                    font=("Arial", 16)).grid(row=0, column=2, padx=5)
        
        ctk.CTkButton(control_btns, text="⏹️", width=60, height=40, corner_radius=20,
                    command=lambda: self.stop_music(controller), 
                    fg_color=SPOTIFY_GRAY, hover_color="#3E3E3E",
                    font=("Arial", 16)).grid(row=0, column=3, padx=5)
        
        ctk.CTkButton(control_btns, text="⏭️", width=60, height=40, corner_radius=20,
                    command=lambda: self.next_song(controller), 
                    fg_color=SPOTIFY_GRAY, hover_color="#3E3E3E",
                    font=("Arial", 16)).grid(row=0, column=4, padx=5)
        
        # Volume Control
        volume_frame = ctk.CTkFrame(self.frame_control, fg_color="transparent")
        volume_frame.pack(side="right", padx=20)
        
        ctk.CTkLabel(volume_frame, text="🔊", font=("Arial", 14)).pack(
            side="left", padx=5)
        self.volume_slider = ctk.CTkSlider(
            volume_frame, from_=0, to=100, width=120,
            command=lambda v: self.change_volume(controller, v),
            button_color=SPOTIFY_GREEN, 
            button_hover_color="#1ed760",
            progress_color=SPOTIFY_GREEN)
        self.volume_slider.set(70)
        self.volume_slider.pack(side="left", padx=5)

    def refresh_library(self, controller):
        self.library_box.configure(state="normal")
        self.library_box.delete("1.0", "end")
        self.library_items = []
        art = controller.player.library.artists_head
        while art:
            alb = art.albums_head
            while alb:
                song = alb.songs_head
                while song:
                    text = (f"{song.id}. {song.title} — {song.duration} "
                        f"({art.artist_name} / {alb.album_name})\n")
                    self.library_box.insert("end", text)
                    self.library_items.append(song)
                    song = song.next
                alb = alb.next
            art = art.next
        self.library_box.configure(state="disabled")
        self.selected_index = None

    def search_songs(self, controller):
        keyword = self.search_entry.get().strip().lower()
        if not keyword:
            self.refresh_library(controller)
            return
        
        self.library_box.configure(state="normal")
        self.library_box.delete("1.0", "end")
        self.library_items = []
        art = controller.player.library.artists_head
        found_count = 0
        while art:
            alb = art.albums_head
            while alb:
                song = alb.songs_head
                while song:
                    if (keyword in song.title.lower() or 
                        keyword in art.artist_name.lower() or 
                        keyword in alb.album_name.lower()):
                        text = (f"{song.id}. {song.title} — {song.duration} "
                            f"({art.artist_name} / {alb.album_name})\n")
                        self.library_box.insert("end", text)
                        self.library_items.append(song)
                        found_count += 1
                    song = song.next
                alb = alb.next
            art = art.next
        
        if found_count == 0:
            self.library_box.insert("end", "Tidak ada hasil ditemukan.\n")
        self.library_box.configure(state="disabled")
        self.selected_index = None


    def get_first_song(self, controller):
        art = controller.player.library.artists_head
        return art.albums_head.songs_head if art and art.albums_head else None

    def play_selected(self, controller):
        song = self.get_first_song(controller)
        if song:
            msg = controller.player.play_song(song)
            self.current_label.configure(text=msg)
            self.selected_index = 0

    def pause_resume(self, controller):
        """Toggle pause/resume"""
        if controller.player.is_paused:
            msg = controller.player.resume_song()
        else:
            msg = controller.player.pause_song()
        self.status_label.configure(text=msg, text_color=SPOTIFY_GREEN)

    def stop_music(self, controller):
        """Stop musik"""
        msg = controller.player.stop_song()
        self.current_label.configure(text="⏹️ Musik dihentikan")
        self.status_label.configure(text=msg, text_color=SPOTIFY_GREEN)

    def change_volume(self, controller, value):
        """Ubah volume"""
        volume = float(value) / 100
        msg = controller.player.set_volume(volume)
        # Tidak perlu update status label karena terlalu sering dipanggil

    def add_to_playlist(self, controller):
        song_id_str = self.song_id_entry.get().strip()
        if not song_id_str:
            return self.status_label.configure(text="Masukkan ID lagu!", text_color="#FF6B6B")
        try:
            song_id = int(song_id_str)
        except ValueError:
            return self.status_label.configure(text="ID harus angka!", text_color="#FF6B6B")
        
        found_song = None
        art = controller.player.library.artists_head
        while art and not found_song:
            alb = art.albums_head
            while alb and not found_song:
                song = alb.songs_head
                while song:
                    if str(song.id) == str(song_id):
                        found_song = song
                        break
                    song = song.next
                alb = alb.next
            art = art.next
        
        if found_song:
            controller.player.playlist.add_song(found_song)
            self.refresh_playlist(controller)
            self.status_label.configure(
                text=f"'{found_song.title}' ditambahkan!", 
                text_color=SPOTIFY_GREEN)
            self.song_id_entry.delete(0, 'end')
        else:
            self.status_label.configure(
                text=f"Lagu ID {song_id} tidak ditemukan!", 
                text_color="#FF6B6B")

    def remove_from_playlist(self, controller):
        song_id_str = self.song_id_entry.get().strip()
        if not song_id_str:
            return self.status_label.configure(
                text="Masukkan ID lagu yang ingin dihapus!", 
                text_color="#FF6B6B")
        try:
            song_id = int(song_id_str)
        except ValueError:
            return self.status_label.configure(text="ID harus angka!", text_color="#FF6B6B")
        
        playlist = controller.player.playlist
        if not playlist.head:
            return self.status_label.configure(text="Playlist kosong!", text_color="#FF6B6B")
        
        if str(playlist.head.song.id) == str(song_id):
            if playlist.head == playlist.tail:
                playlist.head = playlist.tail = None
            else:
                playlist.head = playlist.head.next
                if playlist.head:
                    playlist.head.prev = None
            self.refresh_playlist(controller)
            self.status_label.configure(
                text=f"Lagu ID {song_id} dihapus dari playlist!", 
                text_color=SPOTIFY_GREEN)
            self.song_id_entry.delete(0, 'end')
            return
        
        curr = playlist.head
        while curr:
            if str(curr.song.id) == str(song_id):
                if curr.prev:
                    curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                if curr == playlist.tail:
                    playlist.tail = curr.prev
                self.refresh_playlist(controller)
                self.status_label.configure(
                    text=f"Lagu ID {song_id} dihapus dari playlist!", 
                    text_color=SPOTIFY_GREEN)
                self.song_id_entry.delete(0, 'end')
                return
            curr = curr.next
        self.status_label.configure(
            text=f"Lagu ID {song_id} tidak ada di playlist!", 
            text_color="#FF6B6B")

    def clear_playlist(self, controller):
        controller.player.playlist.head = None
        controller.player.playlist.tail = None
        self.refresh_playlist(controller)
        self.status_label.configure(text="Playlist dikosongkan!", text_color=SPOTIFY_GREEN)

    def refresh_playlist(self, controller):
        self.playlist_box.configure(state="normal")
        self.playlist_box.delete("1.0", "end")
        curr = controller.player.playlist.head
        if not curr:
            self.playlist_box.insert("end", "Playlist kosong\n")
        else:
            while curr:
                self.playlist_box.insert("end", f"{curr.song.id}. {curr.song.title} — {curr.song.duration}\n")
                curr = curr.next
        self.playlist_box.configure(state="disabled")

    def next_song(self, controller):
        if self.selected_index is None:
            self.selected_index = 0 if self.library_items else None
            if self.selected_index is None: return
        else:
            self.selected_index = min(self.selected_index + 1, len(self.library_items) - 1)
        if 0 <= self.selected_index < len(self.library_items):
            msg = controller.player.play_song(self.library_items[self.selected_index])
            self.current_label.configure(text=msg)

    def previous_song(self, controller):
        if self.selected_index is None: 
            self.selected_index = 0
        else:
            self.selected_index = max(self.selected_index - 1, 0)
        if 0 <= self.selected_index < len(self.library_items):
            msg = controller.player.play_song(self.library_items[self.selected_index])
            self.current_label.configure(text=msg)

class PageAdmin(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color=SPOTIFY_BLACK)
        
        # Header
        header = ctk.CTkFrame(self, height=60, fg_color=SPOTIFY_DARK_GRAY, corner_radius=0)
        header.pack(fill="x", padx=0, pady=0)
        
        ctk.CTkButton(header, text="← Kembali", width=100, height=35, corner_radius=20,
                    command=lambda: controller.show_frame(PageMenu), 
                    fg_color=SPOTIFY_GRAY, hover_color="#3E3E3E").place(x=15, y=12)
        
        ctk.CTkLabel(header, text="⚙️ Admin Panel - Kelola Musik", font=("Arial", 18, "bold"),
                    text_color=SPOTIFY_WHITE).place(x=450, y=15)
        
        # Content
        content = ctk.CTkFrame(self, fg_color=SPOTIFY_BLACK)
        content.pack(fill="both", expand=True, padx=15, pady=(10, 20))

        # Left: Library Display
        self.frame_library = ctk.CTkFrame(content, width=580, corner_radius=15, fg_color=SPOTIFY_DARK_GRAY)
        self.frame_library.pack(side="left", fill="both", expand=True, padx=(0, 8))
        
        library_header = ctk.CTkFrame(self.frame_library, height=50, fg_color=SPOTIFY_GRAY, corner_radius=10)
        library_header.pack(fill="x", padx=10, pady=10)
        ctk.CTkLabel(library_header, text="📚 Library Lagu", font=("Arial", 16, "bold"), 
                    text_color=SPOTIFY_WHITE).pack(side="left", padx=15, pady=10)
        
        self.admin_library_box = ctk.CTkTextbox(self.frame_library, fg_color=SPOTIFY_GRAY, 
                                            text_color=SPOTIFY_WHITE, border_color=SPOTIFY_DARK_GRAY,
                                            corner_radius=10, font=("Consolas", 11))
        self.admin_library_box.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        self.refresh_admin_library(controller)

        # Right: Form
        self.frame_detail = ctk.CTkFrame(content, width=580, corner_radius=15, fg_color=SPOTIFY_DARK_GRAY)
        self.frame_detail.pack(side="left", fill="both", expand=True, padx=(8, 0))
        
        form_header = ctk.CTkFrame(self.frame_detail, height=50, fg_color=SPOTIFY_GRAY, corner_radius=10)
        form_header.pack(fill="x", padx=10, pady=10)
        ctk.CTkLabel(form_header, text="✏️ Form Tambah/Edit Lagu", font=("Arial", 16, "bold"), 
                    text_color=SPOTIFY_WHITE).pack(side="left", padx=15, pady=10)
        
        form_content = ctk.CTkFrame(self.frame_detail, fg_color="transparent")
        form_content.pack(fill="both", expand=True, padx=15, pady=10)
        
        # Form fields dengan styling lebih baik
        ctk.CTkLabel(form_content, text="Artis:", font=("Arial", 12, "bold"), 
                    text_color=SPOTIFY_LIGHT_GRAY).pack(anchor="w", pady=(5, 2))
        self.artist_entry = ctk.CTkEntry(form_content, height=35, corner_radius=10,
                                        fg_color=SPOTIFY_GRAY, border_color=SPOTIFY_GRAY, 
                                        text_color=SPOTIFY_WHITE, placeholder_text="Nama artis...")
        self.artist_entry.pack(fill="x", pady=(0, 10))
        
        ctk.CTkLabel(form_content, text="Album:", font=("Arial", 12, "bold"), 
                    text_color=SPOTIFY_LIGHT_GRAY).pack(anchor="w", pady=(5, 2))
        self.album_entry = ctk.CTkEntry(form_content, height=35, corner_radius=10,
                                    fg_color=SPOTIFY_GRAY, border_color=SPOTIFY_GRAY, 
                                    text_color=SPOTIFY_WHITE, placeholder_text="Nama album...")
        self.album_entry.pack(fill="x", pady=(0, 10))
        
        row1 = ctk.CTkFrame(form_content, fg_color="transparent")
        row1.pack(fill="x", pady=(0, 10))
        
        id_frame = ctk.CTkFrame(row1, fg_color="transparent")
        id_frame.pack(side="left", fill="x", expand=True, padx=(0, 5))
        ctk.CTkLabel(id_frame, text="ID (opsional):", font=("Arial", 12, "bold"), 
                    text_color=SPOTIFY_LIGHT_GRAY).pack(anchor="w", pady=(5, 2))
        self.id_entry = ctk.CTkEntry(id_frame, height=35, corner_radius=10,
                                    fg_color=SPOTIFY_GRAY, border_color=SPOTIFY_GRAY, 
                                    text_color=SPOTIFY_WHITE, placeholder_text="Auto...")
        self.id_entry.pack(fill="x")
        
        duration_frame = ctk.CTkFrame(row1, fg_color="transparent")
        duration_frame.pack(side="left", fill="x", expand=True, padx=(5, 0))
        ctk.CTkLabel(duration_frame, text="Durasi:", font=("Arial", 12, "bold"), 
                    text_color=SPOTIFY_LIGHT_GRAY).pack(anchor="w", pady=(5, 2))
        self.duration_entry = ctk.CTkEntry(duration_frame, height=35, corner_radius=10,
                                        fg_color=SPOTIFY_GRAY, border_color=SPOTIFY_GRAY, 
                                        text_color=SPOTIFY_WHITE, placeholder_text="mm:ss")
        self.duration_entry.pack(fill="x")
        
        ctk.CTkLabel(form_content, text="Judul Lagu:", font=("Arial", 12, "bold"), 
                    text_color=SPOTIFY_LIGHT_GRAY).pack(anchor="w", pady=(5, 2))
        self.title_entry = ctk.CTkEntry(form_content, height=35, corner_radius=10,
                                    fg_color=SPOTIFY_GRAY, border_color=SPOTIFY_GRAY, 
                                    text_color=SPOTIFY_WHITE, placeholder_text="Judul lagu...")
        self.title_entry.pack(fill="x", pady=(0, 10))
        
        self.error_label = ctk.CTkLabel(form_content, text="", font=("Arial", 11, "bold"),
                                    text_color="#FF6B6B", wraplength=500)
        self.error_label.pack(pady=10)
        
        # Action buttons
        btn_frame = ctk.CTkFrame(form_content, fg_color="transparent")
        btn_frame.pack(fill="x", pady=10)
        
        ctk.CTkButton(btn_frame, text="💾 Simpan", height=45, corner_radius=10,
                    command=lambda: self.save_song_from_form(controller), 
                    fg_color=SPOTIFY_GREEN, hover_color="#1ed760",
                    font=("Arial", 14, "bold")).pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        ctk.CTkButton(btn_frame, text="✏️ Perbarui", height=45, corner_radius=10,
                    command=lambda: self.update_song(controller), 
                    fg_color=SPOTIFY_GRAY, hover_color="#3E3E3E",
                    font=("Arial", 14, "bold")).pack(side="left", fill="x", expand=True, padx=5)
        
        ctk.CTkButton(btn_frame, text="🗑️ Hapus", height=45, corner_radius=10,
                    command=lambda: self.delete_song(controller), 
                    fg_color="#8B0000", hover_color="#A52A2A",
                    font=("Arial", 14, "bold")).pack(side="left", fill="x", expand=True, padx=(5, 0))
        
        self.form_mode = "add"
        self.current_edit_song = None

    def refresh_admin_library(self, controller):
        self.admin_library_box.configure(state="normal")
        self.admin_library_box.delete("1.0", "end")
        art = controller.player.library.artists_head
        while art:
            alb = art.albums_head
            while alb:
                song = alb.songs_head
                while song:
                    self.admin_library_box.insert("end", f"{song.id}. {song.title} — {song.duration} ({art.artist_name} / {alb.album_name})\n")
                    song = song.next
                alb = alb.next
            art = art.next
        self.admin_library_box.configure(state="disabled")

    def clear_form(self):
        self.artist_entry.delete(0, 'end')
        self.album_entry.delete(0, 'end')
        self.id_entry.delete(0, 'end')
        self.title_entry.delete(0, 'end')
        self.duration_entry.delete(0, 'end')
        self.error_label.configure(text="")
        self.form_mode = "add"
        self.current_edit_song = None

    def save_song_from_form(self, controller):
        artist_name, album_name, title, duration = self.artist_entry.get().strip(), self.album_entry.get().strip(), self.title_entry.get().strip(), self.duration_entry.get().strip()
        if not artist_name:
            return self.error_label.configure(text="Artis wajib diisi!")
        if not title:
            return self.error_label.configure(text="Judul lagu wajib diisi!")
        if not duration:
            return self.error_label.configure(text="Durasi wajib diisi!")
        try:
            song_id = int(self.id_entry.get().strip()) if self.id_entry.get().strip() else None
        except ValueError:
            return self.error_label.configure(text="ID harus berupa angka!")

        lib = controller.player.library
        found_artist = None
        art = lib.artists_head
        while art:
            if art.artist_name == artist_name:
                found_artist = art
                break
            art = art.next
        if not found_artist:
            found_artist = lib.add_artist(artist_name)

        found_album = None
        alb = found_artist.albums_head
        while alb:
            if alb.album_name == album_name:
                found_album = alb
                break
            alb = alb.next
        if not found_album:
            found_album = found_artist.add_album(album_name or "Album Baru")

        if song_id is None:
            max_id = 0
            a = lib.artists_head
            while a:
                b = a.albums_head
                while b:
                    s = b.songs_head
                    while s:
                        try:
                            if int(s.id) > max_id:
                                max_id = int(s.id)
                        except Exception:
                            pass
                        s = s.next
                    b = b.next
                a = a.next
            song_id = max_id + 1

        found_album.add_song(song_id, title, duration)
        controller.frames[PageUser].refresh_library(controller)
        self.refresh_admin_library(controller)
        self.clear_form()
        self.error_label.configure(text="Lagu berhasil ditambahkan!", text_color=SPOTIFY_GREEN)

    def delete_song(self, controller):
        song_id_str = self.id_entry.get().strip()
        if not song_id_str:
            return self.error_label.configure(
                text="Masukkan ID lagu yang ingin dihapus!", 
                text_color="#FF6B6B")
        try:
            song_id = int(song_id_str)
        except ValueError:
            return self.error_label.configure(text="ID harus berupa angka!", text_color="#FF6B6B")
        
        lib, found = controller.player.library, False
        art = lib.artists_head
        while art and not found:
            alb = art.albums_head
            while alb and not found:
                if alb.songs_head and str(alb.songs_head.id) == str(song_id):
                    alb.songs_head = alb.songs_head.next
                    found = True
                    break
                prev_song = alb.songs_head
                if prev_song:
                    curr_song = prev_song.next
                    while curr_song:
                        if str(curr_song.id) == str(song_id):
                            prev_song.next = curr_song.next
                            found = True
                            break
                        prev_song, curr_song = curr_song, curr_song.next
                alb = alb.next
            art = art.next
        
        if found:
            controller.frames[PageUser].refresh_library(controller)
            self.refresh_admin_library(controller)
            self.clear_form()
            self.error_label.configure(
                text=f"Lagu ID {song_id} berhasil dihapus!", 
                text_color=SPOTIFY_GREEN)
        else:
            self.error_label.configure(
                text=f"Lagu dengan ID {song_id} tidak ditemukan!", 
                text_color="#FF6B6B")

    def update_song(self, controller):
        song_id_str = self.id_entry.get().strip()
        if not song_id_str:
            return self.error_label.configure(
                text="Masukkan ID lagu yang ingin diperbarui!", 
                text_color="#FF6B6B")
        title, duration = self.title_entry.get().strip(), self.duration_entry.get().strip()
        if not title:
            return self.error_label.configure(text="Judul lagu wajib diisi!", text_color="#FF6B6B")
        if not duration:
            return self.error_label.configure(text="Durasi wajib diisi!", text_color="#FF6B6B")
        try:
            song_id = int(song_id_str)
        except ValueError:
            return self.error_label.configure(text="ID harus berupa angka!", text_color="#FF6B6B")
        
        lib, found = controller.player.library, False
        art = lib.artists_head
        while art and not found:
            alb = art.albums_head
            while alb and not found:
                song = alb.songs_head
                while song:
                    if str(song.id) == str(song_id):
                        song.title, song.duration, found = title, duration, True
                        break
                    song = song.next
                alb = alb.next
            art = art.next
        
        if found:
            controller.frames[PageUser].refresh_library(controller)
            self.refresh_admin_library(controller)
            self.clear_form()
            self.error_label.configure(
                text=f"Lagu ID {song_id} berhasil diperbarui!", 
                text_color=SPOTIFY_GREEN)
        else:
            self.error_label.configure(
                text=f"Lagu dengan ID {song_id} tidak ditemukan!", 
                text_color="#FF6B6B")

app = App()
app.mainloop()
