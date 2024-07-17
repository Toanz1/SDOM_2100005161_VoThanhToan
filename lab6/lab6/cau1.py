import tkinter as tk
from tkinter import ttk, messagebox

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Frame Recorder')  # Đặt tiêu đề cho cửa sổ
        self.geometry('600x300')  # Đặt kích thước cửa sổ
        self.configure(bg='#CCCCCC')  # Đặt màu nền cho cửa sổ chính

        # Tạo nhãn tiêu đề
        self.title_label = tk.Label(self, text='Frame Recorder', font=('Arial', 24, 'bold'), bg='lightgray')
        self.title_label.pack(pady=10)  # Thêm nhãn vào cửa sổ và đặt khoảng cách trên dưới

        # Tạo khung cho FPS
        self.fps_frame = tk.Frame(self, bg='lightgray')
        self.fps_frame.pack(pady=10)  # Thêm khung FPS vào cửa sổ và đặt khoảng cách trên dưới

        self.fps_label = tk.Label(self.fps_frame, text='create an fps video ', font=('Arial', 10), bg='lightgray')
        self.fps_label.pack(side=tk.LEFT, padx=5)  # Thêm nhãn FPS vào khung và đặt khoảng cách trái phải

        self.fps_input = tk.Entry(self.fps_frame, font=('Arial', 14))
        self.fps_input.pack(side=tk.LEFT, padx=5)  # Thêm ô nhập FPS vào khung và đặt khoảng cách trái phải

        # Tạo khung cho các nút
        self.button_frame = tk.Frame(self, bg='lightgray')
        self.button_frame.pack(pady=10)  # Thêm khung các nút vào cửa sổ và đặt khoảng cách trên dưới

        self.pause_button = tk.Button(self.button_frame, text='Pause', command=self.pause_action, bg='lightblue')
        self.pause_button.pack(side=tk.LEFT, padx=5)  # Thêm nút Pause vào khung và đặt khoảng cách trái phải

        self.start_button = tk.Button(self.button_frame, text='Start', command=self.start_action, bg='lightgreen')
        self.start_button.pack(side=tk.LEFT, padx=5)  # Thêm nút Start vào khung và đặt khoảng cách trái phải

        self.stop_button = tk.Button(self.button_frame, text='End', command=self.stop_action, bg='lightcoral')
        self.stop_button.pack(side=tk.LEFT, padx=5)  # Thêm nút End vào khung và đặt khoảng cách trái phải

        # Tạo nhãn trạng thái
        self.status_label = tk.Label(self, text='', font=('Arial', 18), bg='lightgray')
        self.status_label.pack(pady=10)  # Thêm nhãn trạng thái vào cửa sổ và đặt khoảng cách trên dưới

    def pause_action(self):
        messagebox.showinfo("Recording", "Pause")  # Hiển thị thông báo khi nhấn nút Pause

    def start_action(self):
        messagebox.showinfo("Recording", "Start")  # Hiển thị thông báo khi nhấn nút Start

    def stop_action(self):
        messagebox.showinfo("Recording", "End")  # Hiển thị thông báo khi nhấn nút End

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()  # Bắt đầu vòng lặp sự kiện chính của ứng dụng
