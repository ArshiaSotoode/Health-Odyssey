import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import Meter, Button, Label, Frame
from ttkbootstrap.tableview import Tableview
from ttkbootstrap import PhotoImage
import pathlib


path = pathlib.Path(__file__).parent.resolve()
assets_path = path.joinpath("assets")

class App(ttk.Window):
    def __init__(self):
        super().__init__()
        # main-setup
        self.title("Weight tracker")
        self.geometry("1600x900")

        # layout\widgets
        self.topbar = TopBar(self)
        self.mainframe = MainFrame(self)
        # run
        self.mainloop()


class TopBar(Frame):
    def __init__(self, parent):
        super().__init__(parent, width=900, height=100, style=DANGER)
        # setup
        self.pack(side=TOP, fill=X)
        self.create_widgets()
        self.create_layout()

    """
    need to make the buttons square and change the hit point
    """

    def create_widgets(self):
        self.user_img = PhotoImage(file=rf"{assets_path}\user.png")
        self.user_button = Button(self, image=self.user_img, style="link.TButton")

        self.name = ttk.StringVar(value="Arshia Sotoode")
        self.user_name = Label(
            self, textvariable=self.name, font="roboto 25 underline bold"
        )

        self.height = ttk.StringVar(value="189cm")
        self.user_height = Label(
            self, textvariable=self.height, font="roboto 12 underline"
        )

        self.edit_img = PhotoImage(file=rf"{assets_path}\edit.png")
        self.edit_button = Button(self, image=self.edit_img, style="link.TButton")

        self.switch_user_img = PhotoImage(file=rf"{assets_path}\switch_user.png")
        self.switch_user_button = Button(
            self, image=self.switch_user_img, style="link.TButton"
        )

        self.setting_img = PhotoImage(file=rf"{assets_path}\setting.png")
        self.setting_button = Button(self, image=self.setting_img, style="link.TButton")

    def create_layout(self):
        self.user_button.pack(side=LEFT, padx=10, pady=10)
        self.user_name.pack(side=LEFT, padx=5, pady=10)
        self.user_height.pack(side=LEFT, padx=5, pady=10)
        self.edit_button.pack(side=LEFT, padx=5, pady=10)
        self.switch_user_button.pack(side=LEFT, padx=5, pady=10)
        self.setting_button.pack(side=RIGHT, padx=10, pady=10)


class MainFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # setup

        self.grid_main_frame()
        self.time_percent_frame = self.TimePercentFrame(self)
        self.BMI_frame = self.BMIFrame(self)
        self.progress_frame = self.ProgressFrame(self)
        self.info_enter_frame = self.InfoEnterFrame(self)
        self.table_frame = self.TableFrame(self)
        self.pack(expand=True, fill=BOTH)

    def grid_main_frame(self):
        self.columnconfigure(index=1, weight=1, uniform="a")
        self.columnconfigure(index=2, weight=1, uniform="a")
        self.columnconfigure(index=3, weight=1, uniform="a")
        self.rowconfigure(index=1, weight=4, uniform="a")
        self.rowconfigure(index=2, weight=3, uniform="a")

    class TimePercentFrame(Frame):
        def __init__(self, parent):
            super().__init__(parent, style=SUCCESS)
            # setup
            self.grid(column=1, row=1, sticky=NSEW)
            self.create_grid()
            self.create_widgets()
            self.create_layout()

        def create_grid(self):
            self.columnconfigure(1, weight=1, uniform="a")
            self.columnconfigure(2, weight=1, uniform="a")
            self.rowconfigure(1, weight=10)
            self.rowconfigure(2, weight=1)

        def create_widgets(self):
            self.time_percent = 74
            self.time_percent = Meter(
                self,
                metertype=SEMI,
                amountused=self.time_percent,
                subtext="Time",
                textright="%",
                subtextfont="roboto 20 bold",
                subtextstyle=DARK,
                stripethickness=10,
                interactive=True,
                metersize=300,
                meterthickness=30,
            )

            self.total_time_frame = Frame(self)
            self.tot_time = ttk.StringVar(value="37 days")
            self.total_time = Label(
                self.total_time_frame, textvariable=self.tot_time, font="roboto 15 bold"
            )
            self.total_time_lable = Label(
                self.total_time_frame, text="total time", font="roboto 12"
            )

            self.days_past_frame = Frame(self)
            self.past = ttk.IntVar(value=81)
            self.days_past = Label(
                self.days_past_frame, textvariable=self.past, font="roboto 15 bold"
            )
            self.days_past_lable = Label(
                self.days_past_frame, text="Days past", font="roboto 12"
            )

            self.days_remaining_frame = Frame(self)
            self.remaining = ttk.IntVar(value=81)
            self.days_remaining = Label(
                self.days_remaining_frame,
                textvariable=self.remaining,
                font="roboto 15 bold",
            )
            self.days_remaining_lable = Label(
                self.days_remaining_frame, text="Days remaining", font="roboto 12"
            )

        def create_layout(self):
            self.total_time.pack(side=TOP)
            self.total_time_lable.pack(side=TOP)
            self.days_past.pack(side=TOP)
            self.days_past_lable.pack(side=TOP)
            self.days_remaining.pack(side=TOP)
            self.days_remaining_lable.pack(side=TOP)
            self.time_percent.grid(column=1, row=1, columnspan=2)
            self.total_time_frame.grid(column=1, row=2)
            self.days_past_frame.grid(column=2, row=2)
            self.days_remaining_frame.grid(column=2, row=2)

    class BMIFrame(Frame):
        def __init__(self, parent):
            super().__init__(parent, style=PRIMARY)
            # setup
            self.grid(column=2, row=1, sticky=NSEW)
            self.create_grid()
            self.create_widgets()
            self.create_layout()

        def create_grid(self):
            self.columnconfigure(1, weight=1, uniform="a")
            self.columnconfigure(2, weight=1, uniform="a")
            self.rowconfigure(1, weight=10)
            self.rowconfigure(2, weight=1)

        def create_widgets(self):
            self.BMI = 74
            self.BMI_meter = Meter(
                self,
                metertype=SEMI,
                amountused=self.BMI,
                subtext="BMI",
                subtextfont="roboto 20 bold",
                subtextstyle=DARK,
                stripethickness=10,
                interactive=True,
                metersize=400,
                meterthickness=30,
            )

            self.cw_frame = Frame(self)
            self.cw = ttk.IntVar(value=87)
            self.current_weight = Label(
                self.cw_frame, textvariable=self.cw, font="roboto 15 bold"
            )
            self.cw_lable = Label(
                self.cw_frame, text="Current weight", font="roboto 12"
            )

            self.gw_frame = Frame(self)
            self.gw = ttk.IntVar(value=81)
            self.goal_weight = Label(
                self.gw_frame, textvariable=self.gw, font="roboto 15 bold"
            )
            self.gw_lable = Label(self.gw_frame, text="Goal weight", font="roboto 12")

        def create_layout(self):
            self.BMI_meter.grid(column=1, row=1, columnspan=2)

            self.current_weight.pack(side=TOP)
            self.cw_lable.pack(side=TOP)

            self.goal_weight.pack(side=TOP)
            self.gw_lable.pack(side=TOP)

            self.cw_frame.grid(column=1, row=2)
            self.gw_frame.grid(column=2, row=2)

    class ProgressFrame(Frame):
        def __init__(self, parent):
            super().__init__(parent, style=SECONDARY)
            # setup
            self.grid(column=3, row=1, sticky=NSEW)
            self.create_grid()
            self.create_widgets()
            self.create_layout()

        def create_grid(self):
            self.columnconfigure(1, weight=1, uniform="a")
            self.columnconfigure(2, weight=1, uniform="a")
            self.rowconfigure(1, weight=10)
            self.rowconfigure(2, weight=1)

        def create_widgets(self):
            self.progress_percent = 74
            self.progress_percent = Meter(
                self,
                metertype=SEMI,
                amountused=self.progress_percent,
                subtext="Progress",
                textright="%",
                subtextfont="roboto 20 bold",
                subtextstyle=DARK,
                stripethickness=10,
                interactive=True,
                metersize=300,
                meterthickness=30,
            )

            self.lost_frame = Frame(self)
            self._lost = ttk.StringVar(value="16KG")
            self.lost = Label(
                self.lost_frame, textvariable=self._lost, font="roboto 15 bold"
            )
            self.lost_lable = Label(self.lost_frame, text="Lost", font="roboto 12")

            self.remaining_frame = Frame(self)
            self._remaining = ttk.StringVar(value="9KG")
            self.remaining = Label(
                self.remaining_frame,
                textvariable=self._remaining,
                font="roboto 15 bold",
            )
            self.remaining_lable = Label(
                self.remaining_frame, text="Remaining", font="roboto 12"
            )

        def create_layout(self):
            self.lost.pack(side=TOP)
            self.lost_lable.pack(side=TOP)
            self.remaining.pack(side=TOP)
            self.remaining_lable.pack(side=TOP)
            self.progress_percent.grid(column=1, row=1, columnspan=2)
            self.lost_frame.grid(column=1, row=2)
            self.remaining_frame.grid(column=2, row=2)

    class InfoEnterFrame(Frame):
        def __init__(self, parent):
            super().__init__(parent, style=WARNING)
            # setup
            self.create_grid()
            self.create_widgets()
            self.create_layout()
            self.grid(column=2, row=2, sticky=NSEW)

        def create_grid(self):
            self.columnconfigure(1, weight=1, uniform="a")
            self.columnconfigure(2, weight=1, uniform="a")
            self.columnconfigure(3, weight=1, uniform="a")
            self.rowconfigure(1, weight=1, uniform="a")
            self.rowconfigure(2, weight=1, uniform="a")

        def create_widgets(self):
            self.avg_day_lost_frame = Frame(self)
            self.avg_day_lost = ttk.StringVar(value="0.25KG")
            self.avg_daily_lost = Label(
                self.avg_day_lost_frame,
                textvariable=self.avg_day_lost,
                font="roboto 15 bold",
            )
            self.avg_daily_lost_label = Label(
                self.avg_day_lost_frame, text="Avg daily lost", font="roboto 12"
            )

            self.body_fat_frame = Frame(self)
            self.body_fat = ttk.StringVar(value="27%")
            self.body_fat_percent = Label(
                self.body_fat_frame,
                textvariable=self.body_fat,
                font="roboto 15 bold",
            )
            self.body_fat_label = Label(
                self.body_fat_frame, text="Body fat", font="roboto 12"
            )

            self.avg_week_lost_frame = Frame(self)
            self.avg_week_lost = ttk.StringVar(value="27%")
            self.avg_weekly_lost = Label(
                self.avg_week_lost_frame,
                textvariable=self.avg_week_lost,
                font="roboto 15 bold",
            )
            self.avg_weekly_lost_label = Label(
                self.avg_week_lost_frame, text="Body fat", font="roboto 12"
            )

            self.enter_butt_img = PhotoImage(file=rf"{assets_path}\enter_butt.png")
            self.enter_button = Button(
                self, image=self.enter_butt_img, style="link.TButton"
            )

        def create_layout(self):
            self.avg_daily_lost.pack(side=TOP)
            self.avg_daily_lost_label.pack(side=TOP)

            self.body_fat_percent.pack(side=TOP)
            self.body_fat_label.pack(side=TOP)

            self.avg_weekly_lost.pack(side=TOP)
            self.avg_weekly_lost_label.pack(side=TOP)

            self.avg_day_lost_frame.grid(column=1, row=1)
            self.body_fat_frame.grid(column=2, row=1)
            self.avg_week_lost_frame.grid(column=3, row=1)
            self.enter_button.grid(column=1, row=2, columnspan=3)

    class TableFrame(Frame):
        def __init__(self, parent):
            super().__init__(parent)
            # setup
            self.create_widgets()
            self.create_layout()
            self.grid(column=3, row=2, sticky=NSEW)

        def create_widgets(self):
            self.coldata = [
                {"text": "weight", "stretch": False},
                {"text": "lost", "stretch": False},
                {"text": "date", "stretch": False},
            ]
            self.rowdata = [
                ("86KG", "-1.0KG", "nov/26/2023"),
                ("85KG", "-15.0KG", "nov/15/2023"),
                ("96KG", "-2.0KG", "nov/3/2023"),
            ]
            self.table = Tableview(
                self,
                coldata=self.coldata,
                rowdata=self.rowdata,
                paginated=True,
                searchable=True,
                bootstyle=PRIMARY,
            )

        def create_layout(self):
            self.table.pack(fill=BOTH, expand=YES, padx=10, pady=10)


App()
