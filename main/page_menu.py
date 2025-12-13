import customtkinter as ctk

CIC_BLACK = "#121212"
CIC_DARK_GRAY = "#181818"
CIC_GRAY = "#282828"
CIC_GREEN = "#1DB954"
CIC_WHITE = "#FFFFFF"
CIC_LIGHT_GRAY = "#B3B3B3"

class PageMenu(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color=CIC_BLACK)
        
        self.controller = controller
        
        title_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_frame.pack(pady=100)
        
        ctk.CTkLabel(title_frame, text="🎵", font=("Arial", 60)).pack()
        ctk.CTkLabel(title_frame, text="CIC Music Player", 
                    font=("Arial", 32, "bold"), 
                    text_color=CIC_WHITE).pack(pady=10)
        ctk.CTkLabel(title_frame, text="Experience Music Like Never Before", 
                    font=("Arial", 14), 
                    text_color=CIC_LIGHT_GRAY).pack()
        
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=20)
        
        ctk.CTkButton(button_frame, text="🎧 Masuk sebagai Pengguna", 
                    width=350, height=50, 
                    font=("Arial", 16, "bold"), corner_radius=25,
                    command=lambda: controller.show_frame("PageUser"), 
                    fg_color=CIC_GREEN, hover_color="#1ed760", 
                    text_color=CIC_WHITE).pack(pady=15)
        
        ctk.CTkButton(button_frame, text="⚙️ Masuk sebagai Admin", 
                    width=350, height=50,
                    font=("Arial", 16, "bold"), corner_radius=25,
                    command=lambda: controller.show_frame("PageAdmin"), 
                    fg_color=CIC_GRAY, hover_color="#3E3E3E", 
                    text_color=CIC_WHITE).pack(pady=15)
