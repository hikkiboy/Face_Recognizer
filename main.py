import tkinter as tk
import util
import cv2
from PIL import Image, ImageTk

class App:
    def __init__(self) -> None:
        self.main_window = tk.Tk()
        self.main_window.geometry("1200x520+350+100"),
        
        self.loginbutton = util.get_button(self.main_window, 'Login', 'green', self.login)
        
        self.loginbutton.place(x=750, y=300)
        
        self.registerbutton = util.get_button(self.main_window, 'Registrar', 'gray', self.register, fg ='black')
        
        self.registerbutton.place(x=750, y = 400)
        
        self.webcam_label = util.get_img_label(self.main_window)
        
        self.webcam_label.place(x = 10, y= 0, width= 700, height=500)
        
        self.add_webcam(self.webcam_label)
        
    def add_webcam(self, label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)
        self._label = label
        
        self.process_webcam()    

    def process_webcam(self):
        #read from webcam
        ret,frame = self.cap.read()
        
        #convert
        self.most_recent_capture_arr = frame
        
        
        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
        self.most_recent_capture_pil = Image.fromarray(img_)
        
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        
        self._label.imgtk = imgtk
        
        self._label.configure(image = imgtk)
        
        self._label.after(20, self.process_webcam)
        
    def add_image_to_label(self,label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        
        label.imgtk = imgtk
        
        label.configure(image = imgtk)
        
        self.register_new_user_capture = self.most_recent_capture_arr.copy()
        

    
    def login(self):
        pass
    def register(self):
        self.register_new_window = tk.Toplevel(self.main_window)
        self.register_new_window.geometry("1200x520+370+120")
        
        self.acceptbutton = util.get_button(self.register_new_window, 'Aceitar', 'green', self.accept)
        
        self.acceptbutton.place(x=750, y=300)
        
        self.tryagainbutton = util.get_button(self.register_new_window, 'Tentar novamente', 'red', self.try_again)
        
        self.tryagainbutton.place(x=750, y = 400)
        
        self.capture_label = util.get_img_label(self.register_new_window)
        
        self.capture_label.place(x = 10, y= 0, width= 700, height=500)
        
        self.add_image_to_label(self.capture_label)
        
        self.entry_text_new_user = util.get_entry_text(self.register_new_window)
        self.entry_text_new_user.place(x = 750, y =150)
        
    
    def start(self):
        self.main_window.mainloop()
        
    def try_again(self):
        self.register_new_window.destroy()
        
    def accept(self):
        pass   
        
        
    
if __name__ == "__main__":
    app = App() 
    app.start()