from tkinter import Tk, Frame, BOTH, LEFT, X, Button, RIGHT, Toplevel
from tkinter import NW, Canvas, DISABLED
from tkinter import filedialog
from PIL import Image, ImageTk
import random
import time

from algorithms_drawing_with_pillow import draw_line
from work_with_max_and_min import list_indices_max, list_indices_min, list_indices_max_without_min
from work_with_sorts import sort_indexed_list


# ================================================= Main logic =====================================================
def get_color_data_about_image(px_handle, w: int, h: int) -> tuple:
    """ * Return color data about image.
        * Data is quantity every cast in image"""
    R = [0 for i in range(256)]
    G = R.copy()
    B = R.copy()

    for i in range(w):
        for j in range(h):
            color = px_handle[i, j]
            R[color[0]] += 1            # count pixels define certain cast
            G[color[1]] += 1
            B[color[2]] += 1

    M = [(R[i] + G[i] + B[i]) // 3 for i in range(256)]
    return R, G, B, M


def search_gist_values(px_handle, w, h, min_x = 0, max_x = 256, cl = (0, 0, 0)):
    """ Search histogram data in drawing image """
    if min_x >= max_x:
        raise ValueError("Bad max and min values!!!")
    dx = w / (max_x - min_x)
    x = dx / 2
    data = []
    hh = h - 1

    while x < w:
        y = hh
        while y >= 0:
            if cl == px_handle[int(x), int(y)]:
                data += [1 - y / hh]
                break
            y -= 1
            if y < 0:
                data += [0]
        x += dx
    return data


def draw_bar_graph_in_image(px_handle, w, h, data, min_x = 0, max_x = 256, min_y = 0, max_y = 1, fill = (0, 0, 0)):
    """ Draw histogram in image """
    if min_x >= max_x or min_y >= max_y:
        raise ValueError("Bad max and min values!!!")

    dx = w / (max_x - min_x)
    dy = h / (max_y - min_y)
    h -= 1
    x = 0
    for valy in data:
        x1 = int(x)
        x2 = int(x + dx)
        y1 = int(h - min_y * dy)
        y2 = int(h - valy * dy)
        for mx in range(x1, x2):
                draw_line(px_handle, mx, y1, mx, y2, fill)
        x += dx


def draw_bar_graph_in_canvas(canvas, data, min_x = 0, max_x = 256, fill = "black"):
    """ Draw histogram in canvas """
    if min_x >= max_x:
        raise ValueError("Bad max and min values!!!")
    canvas.delete('all')
    wcnv = canvas.winfo_width()
    hcnv = canvas.winfo_height()
    dx = wcnv / (max_x - min_x)
    max_val = max(data)
    x = 0

    for valy in data:
        canvas.create_rectangle(int(x), hcnv, int(x + dx), int(hcnv - hcnv * valy / max_val),
                                outline=fill, fill=fill)
        x += dx


def get_coords_pixels_this_cast(px_handle, w: int, h: int, pos = 0, val_cast = 255):
    """ return list coords pixels some cast color
        * px_handle - handle pixel context
        * w - width image
        * h - height image
        * pos - 0, 1, 2 (R, G, B)
        * val_cast - value cast (R, G or B)"""
    coords = []
    for i in range(w):
        for j in range(h):
            if val_cast == px_handle[i, j][pos]:
                coords += [(i, j)]
    return coords


def change_image_data(px_handle, w, h, data, new_data, pos_cast = 0):
    # ==================================== step 1: Search coefficient ======================================
    total_count = w * h
    s = total_count + 1
    p = total_count
    # Need search value coefficient for casting of percents in quantity pixels
    if sum(new_data) > 0:
        while s > total_count:  # while sum receive sequence is greater total_count, do
            s = 0
            for i in range(len(new_data)):
                s += int(new_data[i] * p)
            p /= s / total_count

        new_data = [int(e * p) for e in new_data]  # get quantity pixels data
    else:
        v = int(total_count / len(new_data))
        new_data = [v for i in range(len(new_data))]
    # ==============================================================================================

    # ======================================= step 2: Fix error ============================================
    sub_val = sum(new_data) - total_count  # calculate error calculating
    neg_f = sub_val < 0
    sub_val = abs(sub_val)
    if neg_f:
        indices = list_indices_min(new_data, sub_val)
        d = 1
    else:
        indices = list_indices_max_without_min(new_data, sub_val)
        d = -1

    iindex = 0
    while sub_val > 0:
        new_data[indices[iindex]] += d
        sub_val -= 1
        iindex += 1
        if iindex > len(indices) - 1:
            iindex = 0
    # ==============================================================================================

    # =================================== step 3: Indexed and sort data ============================
    for i in range(len(new_data)):
        new_data[i] = [i, new_data[i]]
    sort_indexed_list(new_data, False)
    # ==============================================================================================

    # =================================== step 4: work with image and him data =====================
    # create flags. Flag is sign finished work with column
    flags = [False for i in range(len(data))]
    unneeded_pixels = []
    main_flag = True    # not all flags is True

    while main_flag:    # check all flags
        main_flag = False
        for i in range(len(new_data)):
            if not flags[i]:                                                            # flag is False
                sub = data[new_data[i][0]] - new_data[i][1]                             # calculate difference
                if sub > 0:                                                             # if we have extra pixels in col
                    coords = get_coords_pixels_this_cast(px_handle, w, h, pos_cast, new_data[i][0])
                    sub = new_data[i][1]                                                # count needed pixels
                    while sub > 0:
                        ind = random.randint(0, len(coords) - 1)
                        coords.pop(ind)                                                 # drop needed pixel
                        sub -= 1
                    unneeded_pixels += coords                                           # take unneeded pixels
                    flags[i] = True                                                     # finish work with current col
                elif sub < 0:                                                           # if not enought pixels in col
                    sub = abs(sub)
                    while sub > 0 and len(unneeded_pixels) > 0:         # while we have unneeded and not enought pixels
                        coord = unneeded_pixels.pop(0)                  # take first pixel of queue
                        color = px_handle[coord]                        # take him color
                        if pos_cast == 0:
                            color = (new_data[i][0], color[1], color[2])
                        elif pos_cast == 1:
                            color = (color[0], new_data[i][0], color[2])
                        else:
                            color = (color[0], color[1], new_data[i][0])
                        px_handle[coord] = color                        # change him color
                        new_data[i][1] -= 1                             # remove 1 pixel
                        sub -= 1
                    sub = data[new_data[i][0]] - new_data[i][1]        # calculate diference
                    flags[i] = sub == 0                                # if took all the needed pixels, that work finish
                else:
                    flags[i] = True                                    # if substract is zero, that work with col finish

            if not flags[i]:
                main_flag = True                                        # not all flags is True
    # ====================================================================================================

#=======================================================================================================================


class Window(Frame):
    """Base class for Window"""
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.w = self.parent.winfo_screenwidth()
        self.h = self.parent.winfo_screenheight()
        self.parent.protocol("WM_DELETE_WINDOW", self.close_window)

    def initUi(self):
        """ Function to create a basic user interface """
        pass

    def initEventSlots(self):
        """ Function to set main slots for events interface's objects"""
        pass

    def centerWindow(self):
        """ Function centering the main window on the screen """
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        self.x = int((sw - self.w) / 2)
        self.y = int((sh - self.h) / 2)
        self.parent.geometry(f'{self.w}x{self.h}+{self.x}+{self.y}')

    def close_window(self):
        self.parent.destroy()


class MainWindow(Window):
    def __init__(self, parent):
        super().__init__(parent)

        self.img_filename = ""                              # path to image file

        self.img = None                                     # instance loading image
        self.tk_img = None                                  # instance TKImage for loading image

        self.gist_editor = None
        self.gist_root = None

        self.R, self.G, self.B, self.M = None, None, None, None

        self.initUi()
        self.initEventSlots()


    def initUi(self):
        """ Function to create a basic user interface """
        self.parent.title('Гистограмма изображения')
        self.centerWindow()

        # ================================ Init ui panel histograms ========================================
        self.gist_panel = Frame(self)
        self.canvas_gist1 = Canvas(self.gist_panel, bd=0, highlightthickness=1, highlightbackground="black",
                                   bg="white", cursor="exchange")
        self.canvas_gist1.pack(side=LEFT, fill=BOTH, expand=1, padx=5, pady=5)
        self.canvas_gist2 = Canvas(self.gist_panel, bd=0, highlightthickness=1, highlightbackground="black",
                                   bg="white", cursor="exchange")
        self.canvas_gist2.pack(side=LEFT, fill=BOTH, expand=1, padx=5, pady=5)
        self.canvas_gist3 = Canvas(self.gist_panel, bd=0, highlightthickness=1, highlightbackground="black",
                                   bg="white", cursor="exchange")
        self.canvas_gist3.pack(side=LEFT, fill=BOTH, expand=1, padx=5, pady=5)
        self.canvas_gist4 = Canvas(self.gist_panel, bd=0, highlightthickness=1, highlightbackground="black",
                                   bg="white")
        self.canvas_gist4.pack(side=LEFT, fill=BOTH, expand=1, padx=5, pady=5)
        # =================================================================================================

        # ================================== Init ui panel for displaying Image ===========================
        self.display_panel = Frame(self)
        self.canvas_img = Canvas(self.display_panel, bd=0, highlightthickness=1, highlightbackground="black",
                                 cursor="exchange")
        self.canvas_img.pack(fill=BOTH, expand=1, padx = 5, pady = 5)
        # =================================================================================================

        self.display_panel.pack(fill=BOTH, expand=1, padx=5, pady=5)
        self.gist_panel.pack(fill=BOTH, expand=1, padx=5, pady=5)
        self.pack(fill=BOTH, expand=1)


    def initEventSlots(self):
        # self.parent.protocol("WM_DELETE_WINDOW", self.close_window)

        self.bind("<Configure>", self.resize_img_in_canvas)            # resizing image in canvas at event resizing MainWindow
        self.canvas_img.bind("<Configure>", self.resize_img_in_canvas) # resizing image in canvas at event resizing canvas

        self.canvas_img.bind("<Button-1>", self.open_imgfile)          # load image file in canvas

        self.canvas_gist1.bind("<Button-1>", self.open_R_gist_editor)
        self.canvas_gist2.bind("<Button-1>", self.open_G_gist_editor)
        self.canvas_gist3.bind("<Button-1>", self.open_B_gist_editor)

        self.after(100, self.in_center_canvas_sign)                    # run function for sign "Открыть окно" on canvas_img


    @staticmethod
    def load_img_to_canvas(img, canvas):
        """ * Function placing image on canvas
            * and choosing the right size for him """
        coeff = min(canvas.winfo_width() / img.size[0], canvas.winfo_height() / img.size[1])
        resize_img = (int(img.size[0] * coeff), int(img.size[1] * coeff))
        resized = img.resize(resize_img, Image.ANTIALIAS)
        tk_img = ImageTk.PhotoImage(resized)
        canvas.delete("all")
        canvas.create_image((canvas.winfo_width() - resize_img[0]) // 2,
                            (canvas.winfo_height() - resize_img[1]) // 2,
                            image=tk_img, anchor=NW)
        return tk_img


    def in_center_canvas_sign(self):
        """ Function draw sign "Открыть окно" in canvas_img """
        self.canvas_img.delete('all')
        x = self.canvas_img.winfo_width() / 2
        y = self.canvas_img.winfo_height() / 2
        self.canvas_img.create_text(x, y, fill="black", font="Roboto 20 bold",
                            text="Открыть изображение")


    def resize_img_in_canvas(self, event = None):
        """Function resizing img in canvas_img """
        if self.img:
            self.tk_img = MainWindow.load_img_to_canvas(self.img, self.canvas_img)
        else:
            self.in_center_canvas_sign()


    def open_imgfile(self, event = None):
        """Function call filedialog for opening image file"""
        self.img_filename = filedialog.askopenfilename(filetypes=(("JPEG files", "*.jpg"),
                                                             ("PNG files", "*.png"),
                                                             ("BMP files", "*.bmp")))
        if not self.img_filename:
            return
        self.img = Image.open(self.img_filename)
        self.tk_img = MainWindow.load_img_to_canvas(self.img, self.canvas_img)

        px_handle = self.img.load()
        self.R, self.G, self.B, self.M = get_color_data_about_image(px_handle, self.img.size[0], self.img.size[1])
        draw_bar_graph_in_canvas(self.canvas_gist1, self.R, 0, 256, "red")
        draw_bar_graph_in_canvas(self.canvas_gist2, self.G, 0, 256, "green")
        draw_bar_graph_in_canvas(self.canvas_gist3, self.B, 0, 256, "blue")
        draw_bar_graph_in_canvas(self.canvas_gist4, self.M, 0, 256, "black")


    def open_gist_editor(self, color = (0, 0, 0)):
        """Function fo opening histograms"""
        if self.img:
            self.close_gist_editor()
            self.gist_root = Toplevel()
            self.gist_editor = GistWindow(self.gist_root, self, color)
            self.gist_root.mainloop()

    def open_R_gist_editor(self, event = None):
        """ Open editor for red histogram """
        self.open_gist_editor((255, 0, 0))

    def open_G_gist_editor(self, event = None):
        """ Open editor for green histogram """
        self.open_gist_editor((0, 255, 0))

    def open_B_gist_editor(self, event = None):
        """ Open editor for blue histogram """
        self.open_gist_editor((0, 0, 255))

    def close_gist_editor(self):
        """ Safe closing editor """
        if self.gist_editor:
            self.gist_editor.close_window()
            self.gist_editor = None
            self.gist_root = None

    def close_window(self):
        """ Function closing window """
        self.close_gist_editor()
        self.parent.destroy()

    def change_image_data(self, new_data, color):
        if color[0]:
            data = self.R
            pos_cast = 0
        elif color[1]:
            data = self.G
            pos_cast = 1
        else:
            data = self.B
            pos_cast = 2

        change_image_data(self.img.load(), self.img.size[0], self.img.size[1], data, new_data, pos_cast)
        self.tk_img = MainWindow.load_img_to_canvas(self.img, self.canvas_img)
        self.R, self.G, self.B, self.M = get_color_data_about_image(self.img.load(), self.img.size[0], self.img.size[1])
        draw_bar_graph_in_canvas(self.canvas_gist1, self.R, 0, 256, "red")
        draw_bar_graph_in_canvas(self.canvas_gist2, self.G, 0, 256, "green")
        draw_bar_graph_in_canvas(self.canvas_gist3, self.B, 0, 256, "blue")
        draw_bar_graph_in_canvas(self.canvas_gist4, self.M, 0, 256, "black")




class GistWindow(Window):
    def __init__(self, parent, parent_creater = None, color = (0, 0, 0)):
        super().__init__(parent)
        self.w = 800
        self.h = 600

        self.img = None
        self.tk_img = None

        self.parent_creater = parent_creater

        self.main_color = color
        self.line_color = (0, 0, 0)

        self.points = []

        self.data = None

        self.initUi()
        self.initEventSlots()

    def initUi(self):
        self.parent.title('Изменить гистограмму')

        self.centerWindow()
        self.pack(fill=BOTH, expand=1)

        self.display_panel = Frame(self)
        self.manage_panel = Frame(self)

        # ================================= Init ui canvas for drawing histogramm =============================
        self.canvas_gist = Canvas(self.display_panel, bd=0, highlightthickness=1, highlightbackground="black",
                                   bg="white")
        self.canvas_gist.pack(fill=BOTH, expand=1, padx=5, pady=5)

        self.button_cls = Button(self.manage_panel, text="Отчистить", foreground="red",
                                 command=self.clear_canvas_img)
        self.button_cls.pack(side=RIGHT, padx=5, pady=5)

        self.button_chg = Button(self.manage_panel, text="Изменить", foreground="green", command=self.change_gist)
        self.button_chg.pack(side=RIGHT, padx=5, pady=5)
        self.button_chg["state"] = "disabled"

        self.button_cast = Button(self.manage_panel, text="Преобразовать", foreground="blue", command=self.cast_gist)
        self.button_cast.pack(side=RIGHT, padx=5, pady=5)
        # ======================================================================================================

        self.display_panel.pack(fill=BOTH, expand=1, padx=5, pady=5)
        self.manage_panel.pack(fill=X, padx=5, pady=5)

    def initEventSlots(self):
        self.canvas_gist.bind("<Button-1>", self.draw_line)

    @staticmethod
    def load_img_to_canvas(img, canvas):
        size = (canvas.winfo_width(), canvas.winfo_height())
        resized = img.resize(size, Image.ANTIALIAS)
        tk_img = ImageTk.PhotoImage(resized)
        canvas.delete("all")
        canvas.create_image(0, 0, image=tk_img, anchor=NW)
        return tk_img


    def create_canvas_img(self):
        """ Create new image and new tk_image for canvas """
        if self.img is None:
            self.points.clear()
            self.button_chg["state"] = "disabled"

            self.img = Image.new("RGB", (self.canvas_gist.winfo_width(),
                                         self.canvas_gist.winfo_height()), "white")
            self.tk_img = GistWindow.load_img_to_canvas(self.img, self.canvas_gist)


    def clear_canvas_img(self):
        """ Clear canvas (delete and create new image for canvas) """
        self.canvas_gist.delete("all")

        del self.img
        del self.tk_img
        self.img = None
        self.tk_img = None

        self.create_canvas_img()


    def draw_line(self, event = None):
        """ Drawing line """
        self.create_canvas_img()
        if len(self.points) < 2:
            self.points += [(event.x, event.y)]
        else:
            self.points[0] = self.points[1]
            self.points[1] = (event.x, event.y)

        if len(self.points) == 2:
            px_handle = self.img.load()
            draw_line(px_handle, *self.points[0], *self.points[1], (0, 0, 0))
            self.tk_img = GistWindow.load_img_to_canvas(self.img, self.canvas_gist)


    def cast_gist(self):
        """ Dinamic cast line in histogram values """
        if self.img:
            self.data = search_gist_values(self.img.load(), self.img.size[0], self.img.size[1],
                                           0, 256, self.line_color)
            self.clear_canvas_img()
            draw_bar_graph_in_image(self.img.load(), self.img.size[0],
                                               self.img.size[1],
                                    self.data, 0, 256, 0, 1, self.main_color)
            self.tk_img = GistWindow.load_img_to_canvas(self.img, self.canvas_gist)
            self.button_chg["state"] = "normal"

            del self.img
            self.img = None

    def change_gist(self):
        if self.data is None:
            self.button_chg["state"] = "disabled"
            return

        if len(self.data) != 256:
            self.button_chg["state"] = "disabled"
            return

        if self.parent_creater:
            self.parent_creater.change_image_data(self.data, self.main_color)
            self.close_window()





def main():
    """The main function to enter in program """
    root = Tk()                                     # create MainWindow
    main_window = MainWindow(root)                  # create MainFrame on the MainWindow
    root.mainloop()                                 # run event loop


if __name__ == "__main__":
    main()                                          # run main function on the program