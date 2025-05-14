import os
import sys
import tkinter as tk
from PIL import Image, ImageTk


def resource_path(relative_path):
    """ 获取资源的绝对路径，适用于开发环境和PyInstaller打包后 """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class InteractiveApp:
    def __init__(self, root):
        self.root = root

        # 加载图片
        image1_path = resource_path("文字消除版可以.png")
        image2_path = resource_path("比心.png")

        self.image1 = Image.open(image1_path)
        self.image2 = Image.open(image2_path)
        self.tk_image1 = ImageTk.PhotoImage(self.image1)
        self.tk_image2 = ImageTk.PhotoImage(self.image2)

        # 创建画布并设置图片
        canvas_width = self.tk_image1.width()
        canvas_height = self.tk_image1.height()
        self.canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
        self.canvas.pack()

        # ---------- 新增内容：设置窗口不可缩放 ----------
        self.root.resizable(width=False, height=False)
        self.root.geometry(f"{canvas_width}x{canvas_height}")
        # ---------------------------------------------

        # 放置第一张图片
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor="nw", image=self.tk_image1)

        # 添加提示文字（无背景色）
        self.text_label = tk.Label(
            root,
            text="可以做我的恋人么？",
            font=("华文行楷", 16),
            fg="black",    # 字体颜色保持黑色
            bg="#F3CAC7",  # 使用图片背景色
            borderwidth=0,
            highlightthickness=0
        )
        self.text_label.place(x=366, y=100)  # 新位置

        # 按钮状态
        self.no_click_count = 0

        # 创建按钮
        self.yes_button = tk.Button(
            root,
            text="可以",
            font=("微软雅黑", 12),
            command=self.on_yes,
            bg="#ffcccc",   # 淡红色背景
            fg="white"
        )

        self.no_button = tk.Button(
            root,
            text="不行",
            font=("微软雅黑", 12),
            command=self.on_no,
            bg="#cce5ff",   # 淡蓝色背景
            fg="white"
        )

        # 定位按钮
        self.yes_button.place(x=366, y=300)   # 固定位置
        self.no_button.place(x=490, y=300)   # 不行按钮位置不变

    def on_yes(self):
        """点击“可以”后切换图片，并移除所有控件"""
        # 切换图片
        self.canvas.itemconfig(self.image_on_canvas, image=self.tk_image2)

        # 移除控件
        self.yes_button.place_forget()
        self.no_button.place_forget()
        self.text_label.place_forget()

        # 可选：调整窗口大小以适应新图片尺寸
        canvas_width = self.tk_image2.width()
        canvas_height = self.tk_image2.height()
        self.canvas.config(width=canvas_width, height=canvas_height)
        self.root.geometry(f"{canvas_width}x{canvas_height}")

    def on_no(self):
        """点击“不行”后改变按钮状态"""
        self.no_click_count += 1
        responses = [
            "?你认真的么...",
            "这个选不了呢！",
            "不行:(",
            "不行:("  # 默认保持这个状态
        ]
        if self.no_click_count <= len(responses):
            self.no_button.config(text=responses[self.no_click_count - 1])
        else:
            self.no_button.config(text=responses[-1])

        # 增大“可以”按钮字体
        current_font_size = self.yes_button.cget("font").split()[-1]
        new_font_size = int(current_font_size) + 2
        self.yes_button.config(font=("微软雅黑", new_font_size))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("表白神器")
    app = InteractiveApp(root)
    root.mainloop()