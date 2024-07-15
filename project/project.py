import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import Meter, Button, Label, Frame, Entry
from ttkbootstrap.tableview import Tableview
from ttkbootstrap import PhotoImage
import pathlib
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from tkinter.font import nametofont
from os.path import exists, mkdir
from string import punctuation
from datetime import date

# file variables
punctuation += " "
DATE_FORMAT = "%Y-%m-%d"


def main():
    check_sign_up()


# getting the path and adding the wanted directory to the path
def get_path(join_path=""):
    # getting the path of current working directory
    path = pathlib.Path(__file__).parent.resolve()
    # joining the extra path
    return path.joinpath(join_path)


# check if the user signed up and if not ask theme for it
def check_sign_up():
    if exists(get_path(r"data\user_info.csv")):
        app = App()
    else:
        if not exists(get_path(r"data")):
            mkdir(get_path(r"data"))
        SignUp()


# creating the validating functions
def validate_name(input):
    if any(p in input for p in punctuation) or input.isdigit() or len(input) < 3:
        return False
    else:
        return True


# returns the time percent passed
def give_percentage(elapsed: int, total: int) -> float:
    return round((elapsed / total) * 100, 2)


def calculate_BMI(weight: int, height: int) -> float:
    BMI = weight / (height / 100) ** 2
    return round(BMI, 2)


def calculate_body_fat_percentage(weight: int, age: int, height: int):
    body_fat = (weight * 0.5) + (height * 0.09) + (0.094 * age) - 32
    return round(body_fat, 2)


# creating the sign up page
class SignUp(ttk.Window):
    def __init__(self):
        super().__init__("litera")
        # main-setup
        self.title("Weight tracker")
        self.geometry("700x900")
        self.resizable(width=False, height=False)

        self.create_widgets()
        self.create_layout()

        self.mainloop()

    def create_widgets(self):

        # creating the Main Frame
        self.main_frame = Frame(self)

        # girding the main_frame
        self.main_frame.columnconfigure(index=1, weight=1, uniform="a")
        self.main_frame.columnconfigure(index=2, weight=1, uniform="a")
        self.main_frame.rowconfigure(index=1, weight=1, uniform="a")
        self.main_frame.rowconfigure(index=2, weight=1, uniform="a")
        self.main_frame.rowconfigure(index=3, weight=1, uniform="a")
        self.main_frame.rowconfigure(index=4, weight=3, uniform="a")
        self.main_frame.rowconfigure(index=5, weight=4, uniform="a")
        self.main_frame.rowconfigure(index=6, weight=1, uniform="a")

        # registering validation functions
        valid_name = self.register(validate_name)

        # the welcome label
        self.edit_label = Label(
            self.main_frame, text="Welcome😍", font="roboto 40 bold"
        )

        # input name
        self.name_entry_stringvar = ttk.StringVar()
        self.name_entry_frame = Frame(self.main_frame)
        self.name_entry_label = Label(
            self.name_entry_frame, text="Name : ", font="roboto 15 bold"
        )
        self.name_entry = Entry(
            self.name_entry_frame,
            textvariable=self.name_entry_stringvar,
            font="roboto 15",
            validatecommand=(valid_name, "%P"),
            validate="focus",
        )

        # input last_name
        self.last_name_entry_stringvar = ttk.StringVar()
        self.last_name_entry_frame = Frame(self.main_frame)
        self.last_name_entry_label = Label(
            self.last_name_entry_frame, text="Last Name : ", font="roboto 15 bold"
        )
        self.last_name_entry = Entry(
            self.last_name_entry_frame,
            textvariable=self.last_name_entry_stringvar,
            font="roboto 15",
            validatecommand=(valid_name, "%P"),
            validate="focus",
        )

        # input Date of birth
        self.date_of_birth_frame = Frame(self.main_frame)
        self.date_of_birth_entry = ttk.DateEntry(
            self.date_of_birth_frame, dateformat=DATE_FORMAT
        )
        self.date_of_birth_label = Label(
            self.date_of_birth_frame, text="Date of birth : ", font="roboto 15 bold"
        )

        # input gender
        self.gender_frame = Frame(self.main_frame)
        self.gender_label = Label(
            self.gender_frame, text="Gender : ", font="roboto 15 bold"
        )

        # making a list and inserting it to our combobox
        self.gender_combobox_stringvar = ttk.StringVar()
        self.gender_combobox_list = ["Male", "Female"]
        self.gender_combobox = ttk.Combobox(
            self.gender_frame,
            values=self.gender_combobox_list,
            font="roboto 15",
            textvariable=self.gender_combobox_stringvar,
        )
        # setting the default value for combobox
        self.gender_combobox.current(0)

        # height selector

        # making func for increase height arrow
        def increase_height():
            height = self.height_meter.amountusedvar.get()
            if height < 250:
                height += 1
            self.height_meter.amountusedvar.set(height)

        # making func for decrease height arrow
        def decrease_height():
            height = self.height_meter.amountusedvar.get()
            if height > 0:
                height -= 1
            self.height_meter.amountusedvar.set(height)

        self.height_meter = Meter(
            self.main_frame,
            subtext="Height",
            subtextfont="roboto 20 bold",
            metertype=SEMI,
            stripethickness=5,
            interactive=True,
            metersize=250,
            meterthickness=15,
            amounttotal=250,
            amountused=160,
            textright="Cm",
        )
        self.up_arrow_img_path = get_path(r"assets\up_arrow.png")
        self.up_arrow_img = PhotoImage(file=self.up_arrow_img_path)
        self.down_arrow_img_path = get_path(r"assets\down_arrow.png")
        self.down_arrow_img = PhotoImage(file=self.down_arrow_img_path)
        self.increase_height_butt = Button(
            self.main_frame,
            image=self.up_arrow_img,
            style="link.TButton",
            command=increase_height,
        )
        self.decrees_height_butt = Button(
            self.main_frame,
            image=self.down_arrow_img,
            style="link.TButton",
            command=decrease_height,
        )

        # start weight/date
        self.start_wight_meter = Meter(
            self.main_frame,
            subtext="Start Weight",
            subtextfont="roboto 20 bold",
            metertype=SEMI,
            stripethickness=5,
            interactive=True,
            metersize=300,
            meterthickness=15,
            amounttotal=180,
            amountused=80,
            textright="KG",
        )

        self.start_date = ttk.DateEntry(self.main_frame, dateformat=DATE_FORMAT)

        # target weight/date
        self.target_wight_meter = Meter(
            self.main_frame,
            subtext="Target Weight",
            subtextfont="roboto 20 bold",
            metertype=SEMI,
            stripethickness=5,
            interactive=True,
            metersize=300,
            meterthickness=15,
            amounttotal=180,
            amountused=80,
            textright="KG",
        )

        self.target_date = ttk.DateEntry(self.main_frame, dateformat=DATE_FORMAT)

        # styling the sign up butt
        self.sign_up_style = ttk.Style()
        self.sign_up_style.configure("sign_up.TButton", font=("roboto", 25))
        # sign up button

        self.sign_up_butt = Button(
            self.main_frame,
            text="Sign up",
            style="sign_up.TButton",
            width=8,
            command=self.save_info,
        )

    def create_layout(self):
        self.edit_label.grid(column=1, columnspan=2, row=1)
        # packing the name_entry
        self.name_entry_label.pack(side=LEFT)
        self.name_entry.pack(side=LEFT)
        self.name_entry_frame.grid(column=1, row=2, padx=10, pady=10)
        # packing the last_name_entry
        self.last_name_entry_label.pack(side=LEFT)
        self.last_name_entry.pack(side=LEFT)
        self.last_name_entry_frame.grid(column=2, row=2, padx=10, pady=10)

        # packing date of birth
        self.date_of_birth_label.pack(side=LEFT)
        self.date_of_birth_entry.pack(side=RIGHT, padx=10)
        self.date_of_birth_frame.grid(column=1, row=3)

        # packing gender combobox
        self.gender_label.pack(side=LEFT)
        self.gender_combobox.pack(side=RIGHT)
        self.gender_frame.grid(column=2, row=3)

        # packing height input
        self.height_meter.grid(column=1, row=4, columnspan=2)
        self.increase_height_butt.grid(column=2, row=4)
        self.decrees_height_butt.grid(column=1, row=4)

        # pack start weight and start date
        self.start_wight_meter.grid(column=1, row=5)
        self.start_date.grid(column=1, row=5, sticky=S)

        # pack target weight and start date
        self.target_wight_meter.grid(column=2, row=5)
        self.target_date.grid(column=2, row=5, sticky=S)

        # pack sign up butt
        self.sign_up_butt.grid(column=1, row=6, columnspan=2)

        # packing the main_frame
        self.main_frame.pack()

    # saving sign up info in a csv file
    def save_info(self):
        # storing the data in a dict
        self.user_data = {
            "name": self.name_entry_stringvar.get().capitalize(),
            "last_name": self.last_name_entry_stringvar.get().capitalize(),
            "date of birth": self.date_of_birth_entry.entry.get(),
            "gender": self.gender_combobox_stringvar.get(),
            "height": self.height_meter.amountusedvar.get(),
            "start weight": self.start_wight_meter.amountusedvar.get(),
            "target weight": self.target_wight_meter.amountusedvar.get(),
            "start date": self.start_date.entry.get(),
            "target date": self.target_date.entry.get(),
        }
        self.user_info_df = pd.DataFrame(self.user_data, index=[0])
        self.user_info_df.to_csv(get_path(r"data\user_info.csv"), index=False)
        # creating the main data file
        self.main_data = self.user_info_df.filter(items=["start weight", "start date"])
        # changing the columns names to match the main data file
        self.main_data.rename(
            columns={"start weight": "weights", "start date": "dates"}, inplace=True
        )
        self.main_data.to_csv(get_path(r"data\main_data.csv"), index=False)
        # closing the sign up window
        self.destroy()


# creating the main app
class App(ttk.Window):
    def __init__(self):
        super().__init__("litera")
        # main-setup
        self.title("Weight tracker")
        self.geometry("1600x900")

        # load data
        self.load_update_main_data()
        # layout\widgets
        self.topbar = self.TopBar(self)
        self.mainframe = self.MainFrame(self)

        # run
        self.mainloop()

    @classmethod
    def load_update_main_data(cls):
        cls.load_user_data()
        cls.load_main_data()
        cls.process_dates()
        cls.process_weights()
        # cls.load_update_frames_data()

    @classmethod
    def save_main_data(cls):
        cls.main_data = cls.main_data.sort_values(by="dates")
        cls.main_data.to_csv(get_path(r"data\main_data.csv"), index=False)
        cls.load_update_main_data()

    # loading the user data
    @classmethod
    def load_user_data(cls):
        # loading the user data and change the date strings to date format
        try:
            cls.user_info = pd.read_csv(
                get_path(
                    r"data\user_info.csv",
                ),
                parse_dates=["date of birth", "start date", "target date"],
            )
        except FileNotFoundError:
            pass

    @classmethod
    def load_main_data(cls):
        try:
            cls.main_data = pd.read_csv(
                get_path(r"data\main_data.csv"),
                parse_dates=["dates"],
            )
        except pd.errors.EmptyDataError:
            App.main_data = pd.DataFrame()

    @classmethod
    def process_dates(cls):
        cls.today = date.today()
        # get age
        cls.user_age = round(
            (pd.to_datetime(cls.today) - App.user_info.at[0, "date of birth"]).days
            / 365
        )

        # get the total time
        cls.total_time = (
            App.user_info.at[0, "target date"] - App.user_info.at[0, "start date"]
        ).days

        # get the elapsed days
        cls.elapsed_days = (
            App.main_data["dates"].iloc[-1] - App.user_info.at[0, "start date"]
        ).days

        # get the remaining days
        cls.remaining_days = cls.total_time - cls.elapsed_days

    @classmethod
    def process_weights(cls):
        cls.current_weight = App.main_data["weights"].iloc[-1]

        cls.weight_lost = App.main_data["weights"].iloc[0] - cls.current_weight
        cls.weight_remaining = cls.current_weight - App.user_info.at[0, "target weight"]
        cls.weight_lost_total = (
            App.user_info.at[0, "start weight"] - App.user_info.at[0, "target weight"]
        )
        if cls.elapsed_days > 0:
            cls.average_daily_lost = round(cls.weight_lost / cls.elapsed_days, 3)
        else:
            cls.average_daily_lost = 0
        if cls.elapsed_days > 7:
            cls.average_weekly_lost = round(cls.average_daily_lost * 7, 3)
        else:
            cls.average_weekly_lost = 0

    def load_update_frames_data(self):
        self.mainframe.TimePercentFrame.load_update_data(
            self.mainframe.time_percent_frame
        )
        self.mainframe.BMIFrame.load_update_data(self.mainframe.BMI_frame)
        self.mainframe.ProgressFrame.load_update_data(self.mainframe.progress_frame)
        self.mainframe.InfoEnterFrame.load_update_data(self.mainframe.info_enter_frame)
        self.mainframe.plot_frame.load_update_data()
        self.mainframe.table_frame.load_update_data()

    # creating the top bar
    class TopBar(Frame):
        def __init__(self, parent):
            super().__init__(
                parent,
                width=900,
                height=100,
            )
            # setup
            self.pack(side=TOP, fill=X)
            self.create_widgets()
            self.create_layout()

        """
        need to make the buttons square and change the hit point
        """

        def create_widgets(self):
            # user info button
            # getting the path for user butt img
            self.user_img_path = get_path(r"assets\user.png")
            self.user_img = PhotoImage(file=self.user_img_path)
            self.user_button = Button(self, image=self.user_img, style="link.TButton")

            self.name = App.user_info["name"].to_string(index=False)
            self.last_name = App.user_info["last_name"].to_string(index=False)
            self.height = App.user_info["height"].to_string(index=False)
            # user name text
            self.name = ttk.StringVar(value=f"{self.name} {self.last_name}")
            self.user_name = Label(
                self, textvariable=self.name, font="roboto 25 underline bold"
            )

            # user height text
            self.height = ttk.StringVar(value=f"{self.height} Cm")
            self.user_height = Label(
                self, textvariable=self.height, font="roboto 12 underline"
            )

            # editing user info button
            # getting the path for user butt img
            self.edit_img_path = get_path(r"assets\edit.png")
            self.edit_img = PhotoImage(file=self.edit_img_path)
            self.edit_button = Button(
                self, image=self.edit_img, style="link.TButton", command=self.edit_info
            )

            # user switch button
            # getting the path for user butt img
            self.switch_user_img_path = get_path(r"assets\switch_user.png")
            self.switch_user_img = PhotoImage(file=self.switch_user_img_path)
            self.switch_user_button = Button(
                self, image=self.switch_user_img, style="link.TButton"
            )

            # setting button
            # getting the path for user butt img
            self.setting_img_path = get_path(r"assets\setting.png")
            self.setting_img = PhotoImage(file=self.setting_img_path)
            self.setting_button = Button(
                self, image=self.setting_img, style="link.TButton"
            )

        def create_layout(self):
            # placing the widgets
            self.user_button.pack(side=LEFT, padx=10, pady=10)
            self.user_name.pack(side=LEFT, padx=5, pady=10)
            self.user_height.pack(side=LEFT, padx=5, pady=10)
            self.edit_button.pack(side=LEFT, padx=5, pady=10)
            self.switch_user_button.pack(side=LEFT, padx=5, pady=10)
            self.setting_button.pack(side=RIGHT, padx=10, pady=10)

        class edit_info(ttk.Toplevel):
            def __init__(self):
                super().__init__("litera")
                # main-setup
                self.title("Editing User Information")
                self.geometry("700x900")
                self.resizable(width=False, height=False)

                self.create_widgets()
                self.create_layout()

                self.mainloop()

            def create_widgets(self):

                # creating the Main Frame
                self.main_frame = Frame(self)

                # girding the main_frame
                self.main_frame.columnconfigure(index=1, weight=1, uniform="a")
                self.main_frame.columnconfigure(index=2, weight=1, uniform="a")
                self.main_frame.rowconfigure(index=1, weight=1, uniform="a")
                self.main_frame.rowconfigure(index=2, weight=1, uniform="a")
                self.main_frame.rowconfigure(index=3, weight=1, uniform="a")
                self.main_frame.rowconfigure(index=4, weight=3, uniform="a")
                self.main_frame.rowconfigure(index=5, weight=4, uniform="a")
                self.main_frame.rowconfigure(index=6, weight=1, uniform="a")

                # registering validation functions
                valid_name = self.register(validate_name)

                # the welcome label
                self.edit_label = Label(
                    self.main_frame, text="Editing Info !!!", font="roboto 40 bold"
                )

                # input name
                self.name_entry_stringvar = ttk.StringVar(
                    value=App.user_info.at[0, "name"]
                )
                self.name_entry_frame = Frame(self.main_frame)
                self.name_entry_label = Label(
                    self.name_entry_frame, text="Name : ", font="roboto 15 bold"
                )
                self.name_entry = Entry(
                    self.name_entry_frame,
                    textvariable=self.name_entry_stringvar,
                    font="roboto 15",
                    validatecommand=(valid_name, "%P"),
                    validate="focus",
                )

                # input last_name
                self.last_name_entry_stringvar = ttk.StringVar(
                    value=App.user_info.at[0, "last_name"]
                )
                self.last_name_entry_frame = Frame(self.main_frame)
                self.last_name_entry_label = Label(
                    self.last_name_entry_frame,
                    text="Last Name : ",
                    font="roboto 15 bold",
                )
                self.last_name_entry = Entry(
                    self.last_name_entry_frame,
                    textvariable=self.last_name_entry_stringvar,
                    font="roboto 15",
                    validatecommand=(valid_name, "%P"),
                    validate="focus",
                )

                # input Date of birth
                self.date_of_birth_frame = Frame(self.main_frame)
                self.date_of_birth_entry = ttk.DateEntry(
                    self.date_of_birth_frame,
                    dateformat=DATE_FORMAT,
                    startdate=App.user_info.at[0, "date of birth"],
                )
                self.date_of_birth_label = Label(
                    self.date_of_birth_frame,
                    text="Date of birth : ",
                    font="roboto 15 bold",
                )

                # input gender
                self.gender_frame = Frame(self.main_frame)
                self.gender_label = Label(
                    self.gender_frame, text="Gender : ", font="roboto 15 bold"
                )

                # making a list and inserting it to our combobox
                self.gender_combobox_stringvar = ttk.StringVar(
                    value=App.user_info.at[0, "gender"]
                )
                self.gender_combobox_list = ["Male", "Female"]
                self.gender_combobox = ttk.Combobox(
                    self.gender_frame,
                    values=self.gender_combobox_list,
                    font="roboto 15",
                    textvariable=self.gender_combobox_stringvar,
                )
                # setting the default value for combobox
                self.gender_combobox.current(0)

                # height selector

                # making func for increase height arrow
                def increase_height():
                    height = self.height_meter.amountusedvar.get()
                    if height < 250:
                        height += 1
                    self.height_meter.amountusedvar.set(height)

                # making func for decrease height arrow
                def decrease_height():
                    height = self.height_meter.amountusedvar.get()
                    if height > 0:
                        height -= 1
                    self.height_meter.amountusedvar.set(height)

                self.height_meter = Meter(
                    self.main_frame,
                    subtext="Height",
                    subtextfont="roboto 20 bold",
                    metertype=SEMI,
                    stripethickness=5,
                    interactive=True,
                    metersize=250,
                    meterthickness=15,
                    amounttotal=250,
                    amountused=App.user_info.at[0, "height"],
                    textright="Cm",
                )
                self.up_arrow_img_path = get_path(r"assets\up_arrow.png")
                self.up_arrow_img = PhotoImage(file=self.up_arrow_img_path)
                self.down_arrow_img_path = get_path(r"assets\down_arrow.png")
                self.down_arrow_img = PhotoImage(file=self.down_arrow_img_path)
                self.increase_height_butt = Button(
                    self.main_frame,
                    image=self.up_arrow_img,
                    style="link.TButton",
                    command=increase_height,
                )
                self.decrees_height_butt = Button(
                    self.main_frame,
                    image=self.down_arrow_img,
                    style="link.TButton",
                    command=decrease_height,
                )

                # start weight/date
                self.start_wight_meter = Meter(
                    self.main_frame,
                    subtext="Start Weight",
                    subtextfont="roboto 20 bold",
                    metertype=SEMI,
                    stripethickness=5,
                    interactive=True,
                    metersize=300,
                    meterthickness=15,
                    amounttotal=180,
                    amountused=App.user_info.at[0, "start weight"],
                    textright="KG",
                )

                self.start_date = ttk.DateEntry(
                    self.main_frame,
                    dateformat=DATE_FORMAT,
                    startdate=App.user_info.at[0, "start date"],
                )

                # target weight/date
                self.target_wight_meter = Meter(
                    self.main_frame,
                    subtext="Target Weight",
                    subtextfont="roboto 20 bold",
                    metertype=SEMI,
                    stripethickness=5,
                    interactive=True,
                    metersize=300,
                    meterthickness=15,
                    amounttotal=180,
                    amountused=App.user_info.at[0, "target weight"],
                    textright="KG",
                )

                self.target_date = ttk.DateEntry(
                    self.main_frame,
                    dateformat=DATE_FORMAT,
                    startdate=App.user_info.at[0, "target date"],
                )

                # styling the sign up butt
                self.sign_up_style = ttk.Style()
                self.sign_up_style.configure("sign_up.TButton", font=("roboto", 25))
                # sign up button

                self.sign_up_butt = Button(
                    self.main_frame,
                    text="Edit",
                    style="sign_up.TButton",
                    width=8,
                    command=self.save_info,
                )

            def create_layout(self):
                self.edit_label.grid(column=1, columnspan=2, row=1)
                # packing the name_entry
                self.name_entry_label.pack(side=LEFT)
                self.name_entry.pack(side=LEFT)
                self.name_entry_frame.grid(column=1, row=2, padx=10, pady=10)
                # packing the last_name_entry
                self.last_name_entry_label.pack(side=LEFT)
                self.last_name_entry.pack(side=LEFT)
                self.last_name_entry_frame.grid(column=2, row=2, padx=10, pady=10)

                # packing date of birth
                self.date_of_birth_label.pack(side=LEFT)
                self.date_of_birth_entry.pack(side=RIGHT, padx=10)
                self.date_of_birth_frame.grid(column=1, row=3)

                # packing gender combobox
                self.gender_label.pack(side=LEFT)
                self.gender_combobox.pack(side=RIGHT)
                self.gender_frame.grid(column=2, row=3)

                # packing height input
                self.height_meter.grid(column=1, row=4, columnspan=2)
                self.increase_height_butt.grid(column=2, row=4)
                self.decrees_height_butt.grid(column=1, row=4)

                # pack start weight and start date
                self.start_wight_meter.grid(column=1, row=5)
                self.start_date.grid(column=1, row=5, sticky=S)

                # pack target weight and start date
                self.target_wight_meter.grid(column=2, row=5)
                self.target_date.grid(column=2, row=5, sticky=S)

                # pack sign up butt
                self.sign_up_butt.grid(column=1, row=6, columnspan=2)

                # packing the main_frame
                self.main_frame.pack()

            # saving sign up info in a csv file
            def save_info(self):
                # storing the data in a dict
                self.user_data = {
                    "name": self.name_entry_stringvar.get().capitalize(),
                    "last_name": self.last_name_entry_stringvar.get().capitalize(),
                    "date of birth": self.date_of_birth_entry.entry.get(),
                    "gender": self.gender_combobox_stringvar.get(),
                    "height": self.height_meter.amountusedvar.get(),
                    "start weight": self.start_wight_meter.amountusedvar.get(),
                    "target weight": self.target_wight_meter.amountusedvar.get(),
                    "start date": self.start_date.entry.get(),
                    "target date": self.target_date.entry.get(),
                }
                self.user_info_df = pd.DataFrame(self.user_data, index=[0])
                self.user_info_df.to_csv(get_path(r"data\user_info.csv"), index=False)

                # closing the sign up window
                self.destroy()

    # creating the main frame
    class MainFrame(Frame):
        def __init__(self, parent):
            super().__init__(parent)
            # setup
            self.parent = parent
            self.grid_main_frame()
            # placing the frames inside
            self.time_percent_frame = self.TimePercentFrame(self)
            self.BMI_frame = self.BMIFrame(self)
            self.progress_frame = self.ProgressFrame(self)
            self.info_enter_frame = self.InfoEnterFrame(self)
            self.table_frame = self.TableFrame(self)
            self.plot_frame = self.PlotFrame(self)
            self.pack(expand=True, fill=BOTH)

        def grid_main_frame(self):
            # creating the grid tables
            self.columnconfigure(index=1, weight=1, uniform="a")
            self.columnconfigure(index=2, weight=1, uniform="a")
            self.columnconfigure(index=3, weight=1, uniform="a")
            self.rowconfigure(index=1, weight=1, uniform="a")
            self.rowconfigure(index=2, weight=1, uniform="a")

        # creating the weight entry pop up window
        class WeightEntry(ttk.Toplevel):
            def __init__(self, parent):
                super().__init__("litera")
                self.parent = parent
                # main-setup
                self.title("Weight Entry")
                self.geometry("500x550")
                self.resizable(False, False)
                self.attributes("-topmost", 1)

                # create/pack widgets
                self.create_widgets()
                self.create_layout()

            # creating the widgets
            def create_widgets(self):
                # enter weight label
                self.enter_weight_label = Label(
                    self, text="Please Enter Your Weight", font="roboto 25 bold"
                )

                # creating the weight entry meter with increase and decrease arrows
                self.enter_weight_frame = Frame(self)
                # griding the frame
                self.enter_weight_frame.grid_columnconfigure(
                    index=1, weight=1, uniform="a"
                )
                self.enter_weight_frame.grid_columnconfigure(
                    index=2, weight=5, uniform="a"
                )
                self.enter_weight_frame.grid_columnconfigure(
                    index=3, weight=1, uniform="a"
                )
                self.enter_weight_frame.grid_rowconfigure(
                    index=1, weight=1, uniform="a"
                )
                # loading the images
                self.up_arrow_img_path = get_path(r"assets\up_arrow.png")
                self.up_arrow_img = PhotoImage(file=self.up_arrow_img_path)
                self.down_arrow_img_path = get_path(r"assets\down_arrow.png")
                self.down_arrow_img = PhotoImage(file=self.down_arrow_img_path)

                # making func for increase weight arrow
                def increase_weight():
                    weight = self.weight_meter.amountusedvar.get()
                    if weight < 180:
                        weight += 1
                    self.weight_meter.amountusedvar.set(weight)

                # making func for decrease weight arrow
                def decrease_weight():
                    weight = self.weight_meter.amountusedvar.get()
                    if weight > 0:
                        weight -= 1
                    self.weight_meter.amountusedvar.set(weight)

                # creating the buttons
                self.increase_weight_butt = Button(
                    self.enter_weight_frame,
                    image=self.up_arrow_img,
                    style="link.TButton",
                    command=increase_weight,
                )
                self.decrease_weight_butt = Button(
                    self.enter_weight_frame,
                    image=self.down_arrow_img,
                    style="link.TButton",
                    command=decrease_weight,
                )

                # creating the weight meter
                self.weight_meter = Meter(
                    self.enter_weight_frame,
                    subtext="Weight",
                    subtextfont="roboto 20 bold",
                    metertype=SEMI,
                    stripethickness=5,
                    interactive=True,
                    metersize=300,
                    meterthickness=15,
                    amounttotal=180,
                    amountused=70,
                    textright="Kg",
                )

                # create date entry
                self.date_entry = ttk.DateEntry(self, dateformat=DATE_FORMAT)

                # styling save button
                self.sign_up_style = ttk.Style()
                self.sign_up_style.configure("save.TButton", font=("roboto", 25))
                # create save button
                self.save_butt = Button(
                    self,
                    text="Save",
                    style="save.TButton",
                    width=7,
                    command=self.save_data,
                )

            # packing the widgets
            def create_layout(self):
                # packing enter weight label
                self.enter_weight_label.pack(side=TOP)

                # packing weight meter and arrows
                self.decrease_weight_butt.grid(column=1, row=1)
                self.weight_meter.grid(column=2, row=1)
                self.increase_weight_butt.grid(column=3, row=1)
                self.enter_weight_frame.pack(side=TOP, pady=25)

                # packing date entry
                self.date_entry.pack(side=TOP, expand=True)

                # packing save button
                self.save_butt.pack(expand=TRUE)

            # saving the info to the csv file and updating all of the frames to show the new info
            def save_data(self):
                # prepare the data
                self.weight = self.weight_meter.amountusedvar.get()
                self.date = self.date_entry.entry.get()
                # changing the main data data-frame
                self.new_data = pd.DataFrame(
                    data={"weights": [self.weight], "dates": [self.date]}
                )
                App.main_data = pd.concat(
                    [App.main_data, self.new_data], ignore_index=True
                )
                App.main_data["dates"] = pd.to_datetime(App.main_data["dates"])

                # calling the corresponding functions to save and update the data

                self.destroy()
                App.save_main_data()
                # updating the frames data
                # self.parent.parent refers to self.Mainframe.App
                App.load_update_frames_data(self.parent.parent)

        class TimePercentFrame(Frame):
            def __init__(self, parent):
                super().__init__(parent)
                # setup
                self.grid(column=1, row=1, sticky=NSEW)
                self.initialize_variables()
                self.load_update_data()
                self.create_grid()
                self.create_widgets()
                self.create_layout()

            def create_grid(self):
                # creating the grid tables
                self.columnconfigure(1, weight=1, uniform="a")
                self.columnconfigure(2, weight=1, uniform="a")
                self.columnconfigure(3, weight=1, uniform="a")
                self.rowconfigure(1, weight=10)
                self.rowconfigure(2, weight=1)

            def initialize_variables(self):
                self.total_duration_var = ttk.StringVar()
                self.remaining_duration_var = ttk.StringVar()
                self.past_days_var = ttk.StringVar()
                self.time_percent_var = ttk.DoubleVar()

            def load_update_data(self):
                self.total_duration_var.set(str(App.total_time) + " days")

                self.remaining_duration_var.set(str(App.remaining_days) + " days")

                self.past_days_var.set(str(App.elapsed_days) + " days")

                self.time_percent_var.set(
                    give_percentage(
                        elapsed=App.elapsed_days,
                        total=App.total_time,
                    )
                )
                # for update only: checking if meter variable exists and if it exists update the value
                try:
                    self.time_percent_meter.configure(
                        amountused=self.time_percent_var.get()
                    )
                except AttributeError:
                    pass

            def create_widgets(self):

                # creating the time percent meter

                self.time_percent_meter = Meter(
                    self,
                    metertype=SEMI,
                    amountused=self.time_percent_var.get(),
                    subtext="Time",
                    textright="%",
                    subtextfont="roboto 20 bold",
                    subtextstyle=DARK,
                    stripethickness=10,
                    metersize=350,
                    meterthickness=30,
                )
                # creating the total time frame and putting the time value and label inside
                self.total_time_frame = Frame(self)
                self.tot_time = ttk.StringVar(value="37 days")
                self.total_time = Label(
                    self.total_time_frame,
                    textvariable=self.total_duration_var,
                    font="roboto 15 bold",
                )
                self.total_time_label = Label(
                    self.total_time_frame, text="total time", font="roboto 12"
                )

                # creating the days past frame and putting the days past value and label inside
                self.days_past_frame = Frame(self)
                self.past = ttk.IntVar(value=81)
                self.days_past = Label(
                    self.days_past_frame,
                    textvariable=self.past_days_var,
                    font="roboto 15 bold",
                )
                self.days_past_label = Label(
                    self.days_past_frame, text="Days past", font="roboto 12"
                )

                # creating the days remaining frame and putting the days remaining value and label inside
                self.days_remaining_frame = Frame(self)
                self.remaining = ttk.IntVar(value=81)
                self.days_remaining = Label(
                    self.days_remaining_frame,
                    textvariable=self.remaining_duration_var,
                    font="roboto 15 bold",
                )
                self.days_remaining_label = Label(
                    self.days_remaining_frame, text="Days remaining", font="roboto 12"
                )

            def create_layout(self):
                # placing the widgets inside of frames and then placing frames
                self.total_time.pack(side=TOP)
                self.total_time_label.pack(side=TOP)
                self.days_past.pack(side=TOP)
                self.days_past_label.pack(side=TOP)
                self.days_remaining.pack(side=TOP)
                self.days_remaining_label.pack(side=TOP)
                self.time_percent_meter.grid(column=1, row=1, columnspan=3)
                self.total_time_frame.grid(column=1, row=2)
                self.days_past_frame.grid(column=2, row=2)
                self.days_remaining_frame.grid(column=3, row=2)

        class BMIFrame(Frame):
            def __init__(self, parent):
                super().__init__(parent)
                # setup
                # placing the frame inside of the main frame
                self.grid(column=2, row=1, sticky=NSEW)
                self.initialize_variables()
                self.load_update_data()
                self.create_grid()
                self.create_widgets()
                self.create_layout()

            def create_grid(self):
                # creating the grid tables
                self.columnconfigure(1, weight=1, uniform="a")
                self.columnconfigure(2, weight=1, uniform="a")
                self.rowconfigure(1, weight=10)
                self.rowconfigure(2, weight=1)

            def initialize_variables(self):
                self.BMI_var = ttk.DoubleVar()
                self.current_weight_var = ttk.IntVar()
                self.goal_weight_var = ttk.IntVar()

            def load_update_data(self):
                self.BMI_var.set(
                    calculate_BMI(
                        weight=App.current_weight,
                        height=App.user_info.at[0, "height"],
                    )
                )
                # getting the last item in the main data weight column
                self.current_weight_var.set(App.current_weight)

                self.goal_weight_var.set(App.user_info.at[0, "target weight"])

                # for update only: checking if meter variable exists and if it exists update the value
                try:
                    self.BMI_meter.configure(amountused=self.BMI_var.get())
                except AttributeError:
                    pass

            def create_widgets(self):
                # creating the BMI meter
                self.BMI_meter = Meter(
                    self,
                    metertype=SEMI,
                    amountused=self.BMI_var.get(),
                    subtext="BMI",
                    subtextfont="roboto 20 bold",
                    subtextstyle=DARK,
                    stripethickness=10,
                    metersize=400,
                    meterthickness=30,
                )
                # creating the current weight frame and putting the current weight value and label inside
                self.cw_frame = Frame(self)
                self.current_weight_label = Label(
                    self.cw_frame,
                    textvariable=self.current_weight_var,
                    font="roboto 15 bold",
                )
                self.cw_label = Label(
                    self.cw_frame, text="Current weight", font="roboto 12"
                )
                # creating the goal weight frame and putting the goal weight value and label inside
                self.gw_frame = Frame(self)

                self.goal_weight_label = Label(
                    self.gw_frame,
                    textvariable=self.goal_weight_var,
                    font="roboto 15 bold",
                )
                self.gw_label = Label(
                    self.gw_frame, text="Goal weight", font="roboto 12"
                )

            def create_layout(self):
                # placing the widgets
                self.BMI_meter.grid(column=1, row=1, columnspan=2)

                self.current_weight_label.pack(side=TOP)
                self.cw_label.pack(side=TOP)

                self.goal_weight_label.pack(side=TOP)
                self.gw_label.pack(side=TOP)

                self.cw_frame.grid(column=1, row=2)
                self.gw_frame.grid(column=2, row=2)

        class ProgressFrame(Frame):
            def __init__(self, parent):
                super().__init__(parent)
                # setup
                # placing the frame inside of the main frame
                self.grid(column=3, row=1, sticky=NSEW)
                self.initialize_variables()
                self.load_update_data()
                self.create_widgets()
                self.create_grid()
                self.create_layout()

            def create_grid(self):
                # creating the grid tables
                self.columnconfigure(1, weight=1, uniform="a")
                self.columnconfigure(2, weight=1, uniform="a")
                self.rowconfigure(1, weight=10)
                self.rowconfigure(2, weight=1)

            def initialize_variables(self):
                self.lost_weight_var = ttk.StringVar()
                self.remaining_weight_var = ttk.StringVar()
                self.progress_percent = ttk.DoubleVar()

            def load_update_data(self):
                # loading the values
                self.lost_weight_var.set(str(App.weight_lost) + " KG")
                self.remaining_weight_var.set(str(App.weight_remaining) + " KG")
                self.progress_percent.set(
                    give_percentage(
                        elapsed=App.weight_lost, total=App.weight_lost_total
                    )
                )
                # for update only: checking if meter variable exists and if it exists update the value
                try:
                    self.progress_percent_meter.configure(
                        amountused=self.progress_percent.get()
                    )
                except AttributeError:
                    pass

            def create_widgets(self):
                # creating the progress percent meter
                self.progress_percent_meter = Meter(
                    self,
                    metertype=SEMI,
                    amountused=self.progress_percent.get(),
                    subtext="Progress",
                    textright="%",
                    subtextfont="roboto 20 bold",
                    subtextstyle=DARK,
                    stripethickness=10,
                    metersize=350,
                    meterthickness=30,
                )
                # creating the lost weight frame and putting the lost wight value and label inside
                self.lost_frame = Frame(self)
                self.lost_weight = Label(
                    self.lost_frame,
                    textvariable=self.lost_weight_var,
                    font="roboto 15 bold",
                )
                self.lost_label = Label(self.lost_frame, text="Lost", font="roboto 12")

                # creating the remaining weight frame and putting the remaining wight value and label inside
                self.remaining_frame = Frame(self)
                self.remaining_weight = Label(
                    self.remaining_frame,
                    textvariable=self.remaining_weight_var,
                    font="roboto 15 bold",
                )
                self.remaining_label = Label(
                    self.remaining_frame, text="Remaining", font="roboto 12"
                )

            def create_layout(self):
                # placing the widgets
                self.lost_weight.pack(side=TOP)
                self.lost_label.pack(side=TOP)
                self.remaining_weight.pack(side=TOP)
                self.remaining_label.pack(side=TOP)
                self.progress_percent_meter.grid(column=1, row=1, columnspan=2)
                self.lost_frame.grid(column=1, row=2)
                self.remaining_frame.grid(column=2, row=2)

        class InfoEnterFrame(Frame):
            def __init__(self, parent):
                super().__init__(parent)
                self.parent = parent
                # setup
                self.initialize_variables()
                self.load_update_data()
                self.create_grid()
                self.create_widgets()
                self.create_layout()
                # placing  the frame inside of the main frame
                self.grid(column=2, row=2, sticky=NSEW)

            def create_grid(self):
                # creating the grid tables
                self.columnconfigure(1, weight=1, uniform="a")
                self.columnconfigure(2, weight=1, uniform="a")
                self.columnconfigure(3, weight=1, uniform="a")
                self.rowconfigure(1, weight=1, uniform="a")
                self.rowconfigure(2, weight=1, uniform="a")

            def initialize_variables(self):
                self.body_fat_var = ttk.StringVar()
                self.average_daily_lost_var = ttk.StringVar()
                self.average_weekly_lost_var = ttk.StringVar()

            def load_update_data(self):
                self.body_fat = calculate_body_fat_percentage(
                    height=App.user_info.at[0, "height"],
                    age=App.user_age,
                    weight=App.current_weight,
                )
                self.body_fat_var.set(str(self.body_fat) + " %")

                self.average_daily_lost_var.set(str(App.average_daily_lost) + " KG")
                self.average_weekly_lost_var.set(str(App.average_weekly_lost) + " KG")

            # opening the weight entry popup
            def open_weight_entry(self):
                # passing the main frame instance to the weight entry class
                self.weight_entry = App.MainFrame.WeightEntry(self.parent)

            def create_widgets(self):
                # loading the images of the two cats and loading the images
                self.cat_1_img_path = get_path(r"assets\left_cat.png")
                self.cat_2_img_path = get_path(r"assets\right_cat.png")
                self.cat_1 = PhotoImage(file=self.cat_1_img_path)
                self.cat_2 = PhotoImage(file=self.cat_2_img_path)
                self.left_cat = Label(self, image=self.cat_1)
                self.right_cat = Label(self, image=self.cat_2)

                # creating the average daily lost frame and putting the average daily lost value and label inside
                self.avg_day_lost_frame = Frame(self)
                self.avg_daily_lost = Label(
                    self.avg_day_lost_frame,
                    textvariable=self.average_daily_lost_var,
                    font="roboto 15 bold",
                )
                self.avg_daily_lost_label = Label(
                    self.avg_day_lost_frame, text="Avg daily lost", font="roboto 12"
                )

                # creating body fat percentage time frame and putting the body fat percentage value and label inside
                self.body_fat_frame = Frame(self)
                self.body_fat_percent = Label(
                    self.body_fat_frame,
                    textvariable=self.body_fat_var,
                    font="roboto 15 bold",
                )
                self.body_fat_label = Label(
                    self.body_fat_frame, text="Body fat", font="roboto 12"
                )

                # creating the average weekly lost frame and putting the average weekly lost value and label inside
                self.avg_week_lost_frame = Frame(self)
                self.avg_weekly_lost = Label(
                    self.avg_week_lost_frame,
                    textvariable=self.average_weekly_lost_var,
                    font="roboto 15 bold",
                )
                self.avg_weekly_lost_label = Label(
                    self.avg_week_lost_frame, text="Avg weekly lost", font="roboto 12"
                )
                # loading the enter button image and creating it
                self.user_img_path = get_path(r"assets\enter_butt.png")
                self.enter_butt_img = PhotoImage(file=self.user_img_path)
                self.enter_button = Button(
                    self,
                    image=self.enter_butt_img,
                    style="link.TButton",
                    command=self.open_weight_entry,
                )

            def create_layout(self):
                # placing widgets
                self.left_cat.grid(column=1, row=2, sticky=NSEW)
                self.right_cat.grid(column=3, row=2, sticky=E)

                self.avg_daily_lost.pack(side=TOP)
                self.avg_daily_lost_label.pack(side=TOP)

                self.body_fat_percent.pack(side=TOP)
                self.body_fat_label.pack(side=TOP)

                self.avg_weekly_lost.pack(side=TOP)
                self.avg_weekly_lost_label.pack(side=TOP)

                self.avg_day_lost_frame.grid(column=1, row=1, pady=20)
                self.body_fat_frame.grid(column=2, row=1, pady=20)
                self.avg_week_lost_frame.grid(column=3, row=1, pady=20)
                self.enter_button.grid(column=1, row=2, columnspan=3)

        class TableFrame(Frame):
            def __init__(self, parent):
                super().__init__(parent)
                # setup
                self.create_widgets()
                self.load_update_data()
                self.create_layout()
                # placing the frame inside of the main frame
                self.grid(column=3, row=2, sticky=NSEW)

            def load_update_data(self):
                self.table_data = App.main_data.copy()
                # load/update data
                self.table_data["weight_diff"] = self.table_data["weights"].diff()
                self.table_data = self.table_data[["weights", "weight_diff", "dates"]]

                # set the data
                self.table.build_table_data(
                    coldata=self.table_data.columns.to_list(),
                    rowdata=self.table_data.values.tolist(),
                )

                # making it beautiful
                self.table.align_column_center(cid=0)
                self.table.align_column_center(cid=1)
                self.table.align_column_center(cid=2)
                self.table.align_heading_center(cid=0)
                self.table.align_heading_center(cid=1)
                self.table.align_heading_center(cid=2)
                self.table.autofit_columns()

            def create_widgets(self):
                # determining the font size for the table
                default_font = nametofont("TkDefaultFont")
                default_font.configure(size=14, weight="bold")

                # creating the table
                self.table = Tableview(
                    self,
                    pagesize=500,
                    paginated=True,
                    searchable=True,
                    bootstyle=PRIMARY,
                    stripecolor=("#B7FFFB", None),
                )

            def create_layout(self):
                # placing the table
                self.table.pack(fill=BOTH, expand=YES, padx=10, pady=10)

        class PlotFrame(Frame):
            def __init__(self, parent):
                super().__init__(parent)
                # setup
                self.create_widgets()
                self.load_update_data()
                self.create_layout()
                # placing the frame inside of the main frame
                self.grid(column=1, row=2, sticky=NSEW)

            def load_update_data(self):
                self.ax.cla()
                # make the x axis(dates) more elegant and human readable
                self.fig.autofmt_xdate()
                # plotting the user inputted data
                self.x = App.main_data["dates"]
                self.y = App.main_data["weights"]
                self.ax.plot(self.x, self.y, label="user input", marker="o")
                self.ax.legend()
                self.canvas.draw()

                # plotting the estimated data

            def create_widgets(self):
                plt.style.use("seaborn-v0_8-whitegrid")
                # crating plot
                self.fig = Figure(figsize=(10, 10), layout="constrained")
                self.ax = self.fig.add_subplot()
                # cant use this part because when the plot is updated all the labels will be cleared !!!!!!
                """
                self.ax.set_xlabel(
                    "Date",
                    labelpad=5,
                    fontdict={
                        "family": "serif",
                        "color": "#4582EC",
                        "weight": "normal",
                        "size": 16,
                    },
                )
                self.ax.set_ylabel(
                    "Weight",
                    labelpad=5,
                    fontdict={
                        "family": "roboto",
                        "color": "#4582EC",
                        "weight": "normal",
                        "size": 16,
                    },
                )
                """

                # creating the canvas and putting the plot in it and drawing the canvas
                self.canvas = FigureCanvasTkAgg(master=self, figure=self.fig)
                self.canvas.draw()

                self.toolbar = NavigationToolbar2Tk(
                    self.canvas, self, pack_toolbar=False
                )

            def create_layout(self):
                # placing the canvas
                self.toolbar.pack(side=BOTTOM, fill=X)
                self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)


if __name__ == "__main__":
    main()
