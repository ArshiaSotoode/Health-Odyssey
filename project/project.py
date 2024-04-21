import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import Meter, Button, Label, Frame ,Entry
from ttkbootstrap.tableview import Tableview
from ttkbootstrap import PhotoImage
import pathlib
import dummy_data
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
from tkinter.font import nametofont

def main():
    SignUp()

#getting the path and adding the wanted directory to the path
def get_path(join_path=""):
    # getting the path of current working directory
    path = pathlib.Path(__file__).parent.resolve()
    #joining the extra path
    return path.joinpath(join_path)

class SignUp(ttk.Window):
    def __init__(self):
        super().__init__("litera")
        # main-setup
        self.title("Weight tracker")
        self.geometry("700x900")
        self.resizable(width=False,height=False)
        
        self.create_widgets()
        self.create_layout() 

        
        
        self.mainloop()

    def create_widgets(self):
        
        #creating the Main Frame
        self.main_frame = Frame(self)
        
        #girding the main_frame
        self.main_frame.columnconfigure(index=1, weight=1, uniform="a")
        self.main_frame.columnconfigure(index=2, weight=1, uniform="a")
        self.main_frame.rowconfigure(index=1, weight=1, uniform="a")
        self.main_frame.rowconfigure(index=2, weight=1, uniform="a")
        self.main_frame.rowconfigure(index=3, weight=1, uniform="a")
        self.main_frame.rowconfigure(index=4, weight=2, uniform="a")
        self.main_frame.rowconfigure(index=5, weight=4, uniform="a")
        self.main_frame.rowconfigure(index=6, weight=1, uniform="a")
        #the welcome label
        self.welcome = Label(self.main_frame,text="Welcome😍",font="roboto 40 bold")

        #input name
        self.name_entry_stringvar = ttk.StringVar()
        self.name_entry_frame = Frame(self.main_frame)
        self.name_entry_label = Label(self.name_entry_frame,text="Name : ",font="roboto 15 bold")
        self.name_entry = Entry(self.name_entry_frame,textvariable=self.name_entry_stringvar,font="roboto 15")
        
        
        #input last_name
        self.last_name_entry_stringvar = ttk.StringVar()
        self.last_name_entry_frame = Frame(self.main_frame)
        self.last_name_entry_label = Label(self.last_name_entry_frame,text="Last Name : ",font="roboto 15 bold")
        self.last_name_entry = Entry(self.last_name_entry_frame,textvariable=self.last_name_entry_stringvar,font="roboto 15")
        
        
        #input Date of birth
        self.date_of_birth_frame = Frame(self.main_frame)
        self.date_of_birth_entry = ttk.DateEntry(self.date_of_birth_frame)
        self.date_of_birth_label = Label(self.date_of_birth_frame,text="Date of birth : ",font="roboto 15 bold")
        
        #input gender
        self.gender_frame = Frame(self.main_frame)
        self.gender_label = Label(self.gender_frame,text="Gender : ",font="roboto 15 bold")

        #making a list and inserting it to our combobox
        self.gender_combobox_list = ["Male","Female"]
        self.gender_combobox = ttk.Combobox(self.gender_frame,values=self.gender_combobox_list,font="roboto 15")
        #setting the default value for combobox
        self.gender_combobox.current(0)
        

        #height selector
        self.height_meter = Meter(self.main_frame,
                                  subtext="Height",
                                  subtextfont="roboto 20 bold",
                                  metertype=SEMI,
                                  stripethickness=5,
                                  interactive=True,
                                  metersize=250,
                                  meterthickness=15,
                                  amounttotal=250,
                                  amountused=160,
                                  textright="Cm")
        self.up_arrow_img_path = get_path(r"assets\up_arrow.png")
        self.up_arrow_img = PhotoImage(file=self.up_arrow_img_path)
        self.down_arrow_img_path = get_path(r"assets\down_arrow.png")
        self.down_arrow_img = PhotoImage(file=self.down_arrow_img_path)
        self.increase_height_butt = Button(self.main_frame,image=self.up_arrow_img, style="link.TButton")
        self.decrees_height_butt = Button(self.main_frame,image=self.down_arrow_img, style="link.TButton")
        
        
        #start weight/date
        self.start_wight_meter = Meter(self.main_frame,
                                  subtext="Start Weight",
                                  subtextfont="roboto 20 bold",
                                  metertype=SEMI,
                                  stripethickness=5,
                                  interactive=True,
                                  metersize=300,
                                  meterthickness=15,
                                  amounttotal=160,
                                  amountused=80,
                                  textright="KG")
        
        
        self.start_date = ttk.DateEntry(self.main_frame)
        
        
        #target weight/date
        self.target_wight_meter = Meter(self.main_frame,
                                  subtext="Target Weight",
                                  subtextfont="roboto 20 bold",
                                  metertype=SEMI,
                                  stripethickness=5,
                                  interactive=True,
                                  metersize=300,
                                  meterthickness=15,
                                  amounttotal=160,
                                  amountused=80,
                                  textright="KG")

        self.target_date = ttk.DateEntry(self.main_frame)
        
        #styling the sign up butt
        self.sign_up_style = ttk.Style()
        self.sign_up_style.configure('sign_up.TButton', font=("roboto", 25))
        #sign up button
        
        self.sign_up_butt = Button(self.main_frame,text="Sign up",style='sign_up.TButton',width=8)


    
    
    
    def create_layout(self):
        self.welcome.grid(column=1,columnspan=2,row=1)
        #packing the name_entry
        self.name_entry_label.pack(side=LEFT)
        self.name_entry.pack(side=LEFT)
        self.name_entry_frame.grid(column=1,row=2,padx=10,pady=10)
        #packing the last_name_entry
        self.last_name_entry_label.pack(side=LEFT)
        self.last_name_entry.pack(side=LEFT)
        self.last_name_entry_frame.grid(column=2,row=2,padx=10,pady=10)        
        
        #packing date of birth
        self.date_of_birth_label.pack(side=LEFT)
        self.date_of_birth_entry.pack(side=RIGHT,padx=10)
        self.date_of_birth_frame.grid(column=1,row=3)
        
        #packing gender combobox
        self.gender_label.pack(side=LEFT)
        self.gender_combobox.pack(side=RIGHT)
        self.gender_frame.grid(column=2,row=3)
        
        #packing height input
        self.height_meter.grid(column=1,row=4,columnspan=2)
        self.increase_height_butt.grid(column=2,row=4)
        self.decrees_height_butt.grid(column=1,row=4)
        
        
        #pack start weight and start date
        self.start_wight_meter.grid(column=1,row=5)
        self.start_date.grid(column=1,row=5,sticky=S)
        
        #pack target weight and start date
        self.target_wight_meter.grid(column=2,row=5)
        self.target_date.grid(column=2,row=5,sticky=S)
        
        #pack sign up butt
        self.sign_up_butt.grid(column=1,row=6,columnspan=2)
        
        #packing the main_frame
        self.main_frame.pack()

# creating the main app
class App(ttk.Window):
    def __init__(self):
        super().__init__("litera")
        # main-setup
        self.title("Weight tracker")
        self.geometry("1600x900")

        # layout\widgets
        self.topbar = TopBar(self)
        self.mainframe = MainFrame(self)
        # run
        self.mainloop()


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
        #getting the path for user butt img
        self.user_img_path = get_path(r"assets\user.png")
        self.user_img = PhotoImage(file=self.user_img_path)
        self.user_button = Button(self, image=self.user_img, style="link.TButton")

        # user name text
        self.name = ttk.StringVar(value="Arshia Sotoode")
        self.user_name = Label(
            self, textvariable=self.name, font="roboto 25 underline bold"
        )

        # user height text
        self.height = ttk.StringVar(value="189cm")
        self.user_height = Label(
            self, textvariable=self.height, font="roboto 12 underline"
        )

        # editing user info button
        #getting the path for user butt img
        self.edit_img_path = get_path(r"assets\edit.png")
        self.edit_img = PhotoImage(file=self.edit_img_path)
        self.edit_button = Button(self, image=self.edit_img, style="link.TButton")

        # user switch button
        #getting the path for user butt img
        self.switch_user_img_path = get_path(r"assets\switch_user.png")
        self.switch_user_img = PhotoImage(file=self.switch_user_img_path)
        self.switch_user_button = Button(
            self, image=self.switch_user_img, style="link.TButton"
        )

        # setting button
        #getting the path for user butt img
        self.setting_img_path = get_path(r"assets\setting.png")
        self.setting_img = PhotoImage(file=self.setting_img_path)
        self.setting_button = Button(self, image=self.setting_img, style="link.TButton")

    def create_layout(self):
        # placing the widgets
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

    class TimePercentFrame(Frame):
        def __init__(self, parent):
            super().__init__(parent)
            # setup
            self.grid(column=1, row=1, sticky=NSEW)
            self.create_grid()
            self.create_widgets()
            self.create_layout()

        def create_grid(self):
            # creating the grid tables
            self.columnconfigure(1, weight=1, uniform="a")
            self.columnconfigure(2, weight=1, uniform="a")
            self.rowconfigure(1, weight=10)
            self.rowconfigure(2, weight=1)

        def create_widgets(self):
            # creating the time percent meter
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
                metersize=350,
                meterthickness=30,
            )
            # creating the total time frame and putting the time value and label inside
            self.total_time_frame = Frame(self)
            self.tot_time = ttk.StringVar(value="37 days")
            self.total_time = Label(
                self.total_time_frame, textvariable=self.tot_time, font="roboto 15 bold"
            )
            self.total_time_lable = Label(
                self.total_time_frame, text="total time", font="roboto 12"
            )

            # creating the days past frame and putting the days past value and label inside
            self.days_past_frame = Frame(self)
            self.past = ttk.IntVar(value=81)
            self.days_past = Label(
                self.days_past_frame, textvariable=self.past, font="roboto 15 bold"
            )
            self.days_past_lable = Label(
                self.days_past_frame, text="Days past", font="roboto 12"
            )

            # creating the days remaining frame and putting the days remaining value and label inside
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
            # placing the widgets inside of frames and then placing frames
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
            super().__init__(parent)
            # setup
            # placing the frame inside of the main frame
            self.grid(column=2, row=1, sticky=NSEW)
            self.create_grid()
            self.create_widgets()
            self.create_layout()

        def create_grid(self):
            # creating the grid tables
            self.columnconfigure(1, weight=1, uniform="a")
            self.columnconfigure(2, weight=1, uniform="a")
            self.rowconfigure(1, weight=10)
            self.rowconfigure(2, weight=1)

        def create_widgets(self):
            # creating the BMI meter
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
            # creating the current weight frame and putting the current weight value and label inside
            self.cw_frame = Frame(self)
            self.cw = ttk.IntVar(value=87)
            self.current_weight = Label(
                self.cw_frame, textvariable=self.cw, font="roboto 15 bold"
            )
            self.cw_lable = Label(
                self.cw_frame, text="Current weight", font="roboto 12"
            )
            # creating the goal weight frame and putting the goal weight value and label inside
            self.gw_frame = Frame(self)
            self.gw = ttk.IntVar(value=81)
            self.goal_weight = Label(
                self.gw_frame, textvariable=self.gw, font="roboto 15 bold"
            )
            self.gw_lable = Label(self.gw_frame, text="Goal weight", font="roboto 12")

        def create_layout(self):
            # placing the widgets
            self.BMI_meter.grid(column=1, row=1, columnspan=2)

            self.current_weight.pack(side=TOP)
            self.cw_lable.pack(side=TOP)

            self.goal_weight.pack(side=TOP)
            self.gw_lable.pack(side=TOP)

            self.cw_frame.grid(column=1, row=2)
            self.gw_frame.grid(column=2, row=2)

    class ProgressFrame(Frame):
        def __init__(self, parent):
            super().__init__(parent)
            # setup
            # placing the frame inside of the main frame
            self.grid(column=3, row=1, sticky=NSEW)
            self.create_grid()
            self.create_widgets()
            self.create_layout()

        def create_grid(self):
            # creating the grid tables
            self.columnconfigure(1, weight=1, uniform="a")
            self.columnconfigure(2, weight=1, uniform="a")
            self.rowconfigure(1, weight=10)
            self.rowconfigure(2, weight=1)

        def create_widgets(self):
            # creating the progress percent meter
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
                metersize=350,
                meterthickness=30,
            )
            # creating the lost weight frame and putting the lost wight value and label inside
            self.lost_frame = Frame(self)
            self._lost = ttk.StringVar(value="16KG")
            self.lost = Label(
                self.lost_frame, textvariable=self._lost, font="roboto 15 bold"
            )
            self.lost_lable = Label(self.lost_frame, text="Lost", font="roboto 12")

            # creating the remaining weight frame and putting the remaining wight value and label inside
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
            # placing the widgets
            self.lost.pack(side=TOP)
            self.lost_lable.pack(side=TOP)
            self.remaining.pack(side=TOP)
            self.remaining_lable.pack(side=TOP)
            self.progress_percent.grid(column=1, row=1, columnspan=2)
            self.lost_frame.grid(column=1, row=2)
            self.remaining_frame.grid(column=2, row=2)

    class InfoEnterFrame(Frame):
        def __init__(self, parent):
            super().__init__(parent)
            # setup
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
            self.avg_day_lost = ttk.StringVar(value="0.25KG")
            self.avg_daily_lost = Label(
                self.avg_day_lost_frame,
                textvariable=self.avg_day_lost,
                font="roboto 15 bold",
            )
            self.avg_daily_lost_label = Label(
                self.avg_day_lost_frame, text="Avg daily lost", font="roboto 12"
            )

            # creating body fat percentage time frame and putting the body fat percentage value and label inside
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

            # creating the average weekly lost frame and putting the average weekly lost value and label inside
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

            # loading the enter button image and creating it
            self.user_img_path = get_path(r"assets\enter_butt.png")
            self.enter_butt_img = PhotoImage(file=self.user_img_path)
            self.enter_button = Button(
                self, image=self.enter_butt_img, style="link.TButton"
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
            self.create_layout()
            # placing the frame inside of the main frame
            self.grid(column=3, row=2, sticky=NSEW)

        def create_widgets(self):
            #determining the font size for the table
            default_font = nametofont("TkDefaultFont")
            default_font.configure(size=14,weight='bold')
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

            # creating the table
            self.table = Tableview(
                self,
                coldata=self.coldata,
                rowdata=self.rowdata,
                paginated=True,
                searchable=True,
                bootstyle=PRIMARY,
            )

        def create_layout(self):
            # placing the table
            self.table.pack(fill=BOTH, expand=YES, padx=10, pady=10)

    class PlotFrame(Frame):
        def __init__(self, parent):
            super().__init__(parent)
            # setup
            self.create_widgets()
            self.create_layout()
            # placing the frame inside of the main frame
            self.grid(column=1, row=2, sticky=NSEW)

        def create_widgets(self):
            # loading data
            self.revenue_data = pd.DataFrame(dummy_data.revenue)
            self.revenue_data["date"] = pd.to_datetime(self.revenue_data["date"])

            # crating plot
            self.fig_1 = Figure(figsize=(10, 10), layout="constrained")
            self.plot = self.fig_1.add_subplot()
            sns.lineplot(
                y=self.revenue_data["amount"], x=self.revenue_data["date"], ax=self.plot
            )
            # make the x axis(dates) more elegant and human readable
            self.fig_1.autofmt_xdate()
            # creating the canvas and putting the plot in it and drawing the canvas
            self.canvas = FigureCanvasTkAgg(master=self, figure=self.fig_1)
            self.canvas.draw()

        def create_layout(self):
            # placing the canvas
            self.canvas.get_tk_widget().pack()


if __name__ == "__main__":
    main()

