import customtkinter
from ctypes import windll
from PIL import Image

customtkinter.set_appearance_mode("Light") # Dark or Light
customtkinter.set_default_color_theme("blue") # Blue, Dark-blue, Green

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Setting application variables:
        self.window_title = 'Custom Title Bar in CustomTkinter by Metor' # Change here title of your app

        self.put_icon = False # If you want have icon on your title bar, change that bool from False to True and save your icon(.png) in: assets/images/
        self.dark_mode_icon_path = 'assets\images\my_icon_light.png' # Here put path to light image(for dark mode) for example: assets/images/<Your light icon name>.png
        self.light_mode_icon_path = 'assets\images\my_icon_dark.png' # Here put path to dark image(for light mode) for example: assets/images/<Your dark icon name>.png
        # You can put same path to both variables if toy want to have same icon in dark and light theme

        self.maximized = False

        # Creating fonts:
        self.small_calibri_font = customtkinter.CTkFont(family='Calibri', size=15)
        self.small_helvetica_font = customtkinter.CTkFont(family='Helvetica', size=12)

        # Configuring window:
        self.geometry(f"{550}x{350}")
        self.resizable(False, False)
        self.title(self.window_title)
        self.overrideredirect(True)
        #self.attributes('-topmost', True, '-alpha', 0.9)

        # Creating title bar:
        self.theme = customtkinter.get_appearance_mode()
        if self.theme == 'Dark':
            self.title_bar_color = '#3b3a3a'
            self.text_color = 'white'
            self.hover_button_color = '#7c7d7c'
            self.hover_close_button_color = '#ff4d4d'
        elif self.theme == 'Light':
            self.title_bar_color = '#bebebe'
            self.text_color = 'black'
            self.hover_button_color = '#b3b3b3'
            self.hover_close_button_color = '#e85f5f'            
        else:
            self.title_bar_color = '#000000' # If you are using your own theme, set the color hex here (to match your theme with title bar) 
            self.text_color = 'white' # Here change color of text on title bar
            self.hover_button_color = '#000000' # Here change hover color of buttons for your own theme
            self.hover_close_button_color = '#ff4d4d'    
            print('Warning: You use your own color theme, configure color of title bar in line: 45')

        self.w_width = self.winfo_width()
        self.title_bar = customtkinter.CTkFrame(self, fg_color=self.title_bar_color, width=self.w_width, height=28, corner_radius=0)
        self.title_bar.grid_propagate(False)
        self.title_bar.grid(row=0, column=0, sticky='w')
        self.title_bar.columnconfigure(0, weight=1)

        self.s_width = self.winfo_screenwidth()
        self.s_height = self.winfo_screenheight()
        self.title_bar_height = self.title_bar.winfo_height()
        self.main_frame_maximized_height = self.s_height - self.title_bar_height
        def maximize_me():
            if self.maximized == False:
                self.overrideredirect(False)
                self.wm_state("zoomed")
                self.overrideredirect(True)
                self.expand_button.configure(text=" 🗗 ")
                self.maximized = True

                self.title_bar.configure(width=self.s_width)
                self.main_frame.configure(width=self.s_width, height=self.main_frame_maximized_height)
            else:
                self.overrideredirect(False)
                self.wm_state("normal")
                self.overrideredirect(True)
                self.expand_button.configure(text=" 🗖 ")
                self.maximized = False

                self.title_bar.configure(width=self.w_width)

        def minimize(hide=False):
            hwnd = windll.user32.GetParent(self.winfo_id())
            windll.user32.ShowWindow(hwnd, 0 if hide else 6)           

        # Creating buttons, label and icon on title bar:
        self.minimize_button = customtkinter.CTkButton(self.title_bar, text='  🗕  ', command=minimize, font=self.small_calibri_font, height=28, width=45, corner_radius=0, fg_color=self.title_bar_color, hover_color=self.hover_button_color, text_color=self.text_color)
        self.minimize_button.grid(row=0, column=1, sticky='w')

        self.expand_button = customtkinter.CTkButton(self.title_bar, text='  🗖  ', command=maximize_me,font=self.small_calibri_font, height=28, width=45, corner_radius=0, fg_color=self.title_bar_color, hover_color=self.hover_button_color, text_color=self.text_color)
        self.expand_button.grid(row=0, column=2, sticky='e')

        self.close_button = customtkinter.CTkButton(self.title_bar, text='  🗙  ', command=self.destroy, font=self.small_calibri_font, height=28, width=45, corner_radius=0, fg_color=self.title_bar_color, hover_color=self.hover_close_button_color, text_color=self.text_color)
        self.close_button.grid(row=0, column=3, sticky='e')

        self.title_bar_title = customtkinter.CTkLabel(self.title_bar, text=self.window_title, fg_color=self.title_bar_color, font=self.small_helvetica_font)
        self.title_bar_title.grid(row=0, column=0, sticky='w', padx=5)

        if self.put_icon == True:
            self.app_icon = customtkinter.CTkImage(light_image=Image.open(self.light_mode_icon_path), dark_image=Image.open(self.dark_mode_icon_path), size=(15, 15))
            self.title_bar_title.configure(image=self.app_icon, compound='left', text=(f' {self.window_title}'))

        # Creating main frame and your main app:
        self.main_frame = customtkinter.CTkFrame(self, bg_color='#1f1e1e', corner_radius=0, height=422, width=650)
        self.main_frame.grid_propagate(False)
        self.main_frame.grid(row=1, column=0, sticky='nw')


        # Put your code between the lines:
        # ――――――――――

        #self.example_button = customtkinter.CTkButton(self.main_frame, text='Your app here!', width=130)
        #self.example_button.grid(row=0, column=0, padx=20, pady=20)

        # ――――――――――

        def get_pos(event):
            if self.maximized == False:
                xwin = self.winfo_x()
                ywin = self.winfo_y()
                startx = event.x_root
                starty = event.y_root

                ywin = ywin - starty
                xwin = xwin - startx

                def move_window(event):
                    #self.config(cursor="fleur")
                    self.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')

                def release_window(event):
                    self.config(cursor="arrow")

                self.title_bar.bind('<B1-Motion>', move_window)
                self.title_bar.bind('<ButtonRelease-1>', release_window)
                self.title_bar_title.bind('<B1-Motion>', move_window)
                self.title_bar_title.bind('<ButtonRelease-1>', release_window)
            else:
                self.expand_button.config(text=" 🗖 ")
                self.maximized = not self.maximized


        self.title_bar.bind('<Button-1>', get_pos)
        self.title_bar_title.bind('<Button-1>', get_pos)

        def set_appwindow(mainWindow):
            GWL_EXSTYLE = -20
            WS_EX_APPWINDOW = 0x00040000
            WS_EX_TOOLWINDOW = 0x00000080

            hwnd = windll.user32.GetParent(mainWindow.winfo_id())
            stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
            stylew = stylew & ~WS_EX_TOOLWINDOW
            stylew = stylew | WS_EX_APPWINDOW
            res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)

            mainWindow.wm_withdraw()
            mainWindow.after(10, lambda: mainWindow.wm_deiconify())

        set_appwindow(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()
