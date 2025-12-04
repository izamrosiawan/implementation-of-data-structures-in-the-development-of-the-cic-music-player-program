# Backend — Struktur Data
import pygame
import os

# Inisialisasi pygame mixer untuk audio
pygame.mixer.init()

class SongNode:
    def __init__(self, id, title, duration, file_path=None):
        self.id = id
        self.title = title
        self.duration = duration
        self.file_path = file_path  # Path ke file MP3
        self.next = None


class AlbumNode:
    def __init__(self, album_name):
        self.album_name = album_name
        self.songs_head = None
        self.next = None

    def add_song(self, id, title, duration, file_path=None):
        new_song = SongNode(id, title, duration, file_path)
        if not self.songs_head:
            self.songs_head = new_song
        else:
            curr = self.songs_head
            while curr.next:
                curr = curr.next
            curr.next = new_song
        return new_song


class ArtistNode:
    def __init__(self, artist_name):
        self.artist_name = artist_name
        self.albums_head = None
        self.next = None

    def add_album(self, album_name):
        new_album = AlbumNode(album_name)
        if not self.albums_head:
            self.albums_head = new_album
        else:
            curr = self.albums_head
            while curr.next:
                curr = curr.next
            curr.next = new_album
        return new_album


class MusicLibrary:
    def __init__(self):
        self.artists_head = None

    def add_artist(self, name):
        new_artist = ArtistNode(name)
        if not self.artists_head:
            self.artists_head = new_artist
        else:
            curr = self.artists_head
            while curr.next:
                curr = curr.next
            curr.next = new_artist
        return new_artist


# Playlist

class PlaylistNode:
    def __init__(self, song):
        self.song = song
        self.prev = None
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_song(self, song):
        new_node = PlaylistNode(song)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node


# Stack & Queue

class PlayHistory:
    def __init__(self):
        self.stack = []

    def push(self, song):
        self.stack.append(song)

    def pop(self):
        return self.stack.pop() if self.stack else None


class PlayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, song):
        self.queue.append(song)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None


# Music Player (wrapper)

class MusicPlayer:
    def __init__(self):
        self.library = MusicLibrary()
        self.playlist = Playlist()
        self.history = PlayHistory()
        self.queue = PlayQueue()
        self.current_song = None
        self.is_playing = False
        self.is_paused = False
        self.volume = 0.7  # Volume default 70%
        pygame.mixer.music.set_volume(self.volume)

    def play_song(self, song_node):
        if self.current_song:
            self.history.push(self.current_song)
        
        self.current_song = song_node
        
        # Jika ada file path, mainkan audio
        if song_node.file_path and os.path.exists(song_node.file_path):
            try:
                pygame.mixer.music.load(song_node.file_path)
                pygame.mixer.music.play()
                self.is_playing = True
                self.is_paused = False
                return f"🎵 Memutar: {song_node.title}"
            except Exception as e:
                return f"⚠️ Error memutar {song_node.title}: {str(e)}"
        else:
            # Jika tidak ada file, hanya tampilkan info
            self.is_playing = False
            return f"▶️ Memutar: {song_node.title} (audio tidak tersedia)"

    def pause_song(self):
        if self.is_playing and not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True
            return "⏸️ Musik dijeda"
        return "Tidak ada musik yang sedang diputar"

    def resume_song(self):
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
            return "▶️ Musik dilanjutkan"
        return "Tidak ada musik yang dijeda"

    def stop_song(self):
        if self.is_playing or self.is_paused:
            pygame.mixer.music.stop()
            self.is_playing = False
            self.is_paused = False
            return "⏹️ Musik dihentikan"
        return "Tidak ada musik yang sedang diputar"

    def set_volume(self, volume):
        self.volume = max(0.0, min(1.0, volume))
        pygame.mixer.music.set_volume(self.volume)
        return f"🔊 Volume: {int(self.volume * 100)}%"

    def get_is_playing(self):
        return pygame.mixer.music.get_busy() and not self.is_paused

