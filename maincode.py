from tkinter.messagebox import showerror

from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.popup import Popup

from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.label import MDLabel

import sqlite3


Window.size = (400, 588)
con = sqlite3.Connection('passenger_details.db')
cur = con.cursor()
table = """CREATE TABLE IF NOT EXISTS passenger(
        username varchar(20) NOT NULL, 
        password varchar(20) NOT NULL, 
        email varchar(20) NOT NULL, 
        phone int NOT NULL,
        origin varchar(20),
        destination varchar(20),
        depart_date date, 
        departure_time varchar(20), 
        arrival_time varchar(20), 
        coach char, 
        seat int,
        pax int, 
        amount varchar(20),
        payment_method varchar(20),
        status varchar(20)
        );"""
cur.execute(table)
con.commit()


class Screen1(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def select_origin(self):
        return self.ids.origin_list.text

    def select_destination(self):
        return self.ids.destination_list.text

    def on_save1(self, instance, value, date_range):
        self.ids.departure_date.text = str(value)

    def on_cancel(self, instance, value):
        pass

    def departure_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save1, on_cancel=self.on_cancel)
        date_dialog.open()

    def on_save2(self, instance, value, date_range):
        self.ids.return_date.text = str(value)

    def on_cancel2(self, instance, value):
        pass

    def return_date_picker(self):
        date_dialog = MDDatePicker()  # sizing calendar fit the app
        date_dialog.bind(on_save=self.on_save2, on_cancel=self.on_cancel2)
        date_dialog.open()


class Screen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Screen3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def coach_check(self, coach_name):
        self.ids.selected_coach_3.text = coach_name
        self.ids.cap_id_coach.text = coach_name

    def seat_check(self, seat_name):
        self.ids.selected_seat_3.text = seat_name


class Screen4(Screen):
    pass


class Screen5(Screen):
    pass


class Screen6(Screen):
    def checkbox(self, value, pay_method):
        if value == True:
            self.ids.payment_method.text = pay_method
            #print(pay_method)
        else:
            pass


class Screen7(Screen):
    pass


class Screen8(Screen):

    def show_popup(self):
        show = MDLabel(text="Signed Up Successful", halign='center')

        popupWindow = Popup(title = "Signed Up Successful", content=show, size_hint=(None,None),size=(250,100))
        popupWindow.open()

class Screen9(Screen):
    pass

class Screen10(Screen):
    pass

class CancellingTicket(Screen):
    def cancel_successful(self):
        txt = MDLabel(text="Your booking has been cancelled successfully. Refund will be credited in your HogwartsWallet within 3-4 days.", halign='center')

        popupWindow = Popup(title = "Cancel Ticket", content=txt, size_hint=(None,None),size=(300,200))
        popupWindow.open()

class TrainApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = Builder.load_file("train.kv")

        list_places = ["Johor", "Kuala Lumpur", "Melaka", "Pulau Pinang", "Kedah", "Pahang", "Negeri Sembilan", "Selangor",
                       "Kelantan", "Terengganu", "Perak", "Perlis"]

        places_items1 = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{item}",
                "on_release": lambda x=f"{item}": self.set_item1(x),
            } for item in list_places[:]]

        self.places1 = MDDropdownMenu(
            caller=self.sm.get_screen('screen_one').ids.origin,
            items=places_items1,
            position="center",
            width_mult=3,
            border_margin='10dp'
        )

        places_items2 = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{item}",
                "on_release": lambda x=f"{item}": self.set_item2(x),
            } for item in list_places[:]]

        self.places2 = MDDropdownMenu(
            caller=self.sm.get_screen('screen_one').ids.destination,
            items=places_items2,
            position="center",
            width_mult=3,
            border_margin='10dp'
        )

    def set_item1(self, text__item):
        self.sm.get_screen('screen_one').ids.origin.text = text__item
        self.places1.dismiss()

    def set_item2(self, text__item):
        self.sm.get_screen('screen_one').ids.destination.text = text__item
        self.places2.dismiss()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"

        return self.sm

    def pages_places(self):
        self.sm.get_screen('screen_four').ids.origin_4.text = self.sm.get_screen('screen_one').ids.origin.text
        self.sm.get_screen('screen_four').ids.destination_4.text = self.sm.get_screen('screen_one').ids.destination.text
        self.sm.get_screen('screen_five').ids.origin_5.text = self.sm.get_screen('screen_one').ids.origin.text
        self.sm.get_screen('screen_five').ids.destination_5.text = self.sm.get_screen('screen_one').ids.destination.text
        self.sm.get_screen('screen_seven').ids.origin_7.text = self.sm.get_screen('screen_one').ids.origin.text
        self.sm.get_screen('screen_seven').ids.destination_7.text = self.sm.get_screen(
            'screen_one').ids.destination.text

    def pages_date(self):
        self.sm.get_screen('screen_two').ids.depart_date_2.text = self.sm.get_screen(
            'screen_one').ids.departure_date.text
        self.sm.get_screen('screen_four').ids.depart_date_4.text = self.sm.get_screen(
            'screen_one').ids.departure_date.text
        self.sm.get_screen('screen_five').ids.depart_date_5.text = self.sm.get_screen(
            'screen_one').ids.departure_date.text
        self.sm.get_screen('screen_seven').ids.depart_date_7.text = self.sm.get_screen(
            'screen_one').ids.departure_date.text

    def pages_coach_seat(self):
        self.sm.get_screen('screen_four').ids.coach_no_4.text = self.sm.get_screen(
            'screen_three').ids.selected_coach_3.text
        self.sm.get_screen('screen_five').ids.coach_no_5.text = self.sm.get_screen(
            'screen_three').ids.selected_coach_3.text
        self.sm.get_screen('screen_seven').ids.coach_no_7.text = self.sm.get_screen(
            'screen_three').ids.selected_coach_3.text
        self.sm.get_screen('screen_four').ids.seat_no_4.text = self.sm.get_screen(
            'screen_three').ids.selected_seat_3.text
        self.sm.get_screen('screen_five').ids.seat_no_5.text = self.sm.get_screen(
            'screen_three').ids.selected_seat_3.text
        self.sm.get_screen('screen_seven').ids.seat_no_7.text = self.sm.get_screen(
            'screen_three').ids.selected_seat_3.text

    def details_check(self, departure_time, arrival_time, price):
        details_list = [departure_time, arrival_time, price]
        s = str(details_list)
        s = s.replace(', ', ' ').replace('[', '').replace(']', '')
        self.sm.get_screen('screen_four').ids.time_4.text = s[1:8] + "    -    " + s[11:18]
        self.sm.get_screen('screen_five').ids.time_5.text = s[1:8] + "    -    " + s[11:18]
        self.sm.get_screen('screen_five').ids.prices_5.text = s[21:28]
        self.sm.get_screen('screen_seven').ids.departure_time_7.text = s[1:8]
        self.sm.get_screen('screen_seven').ids.arrival_time_7.text = s[11:18]

    def signup(self,user_name, password, email, phone):
        newdata = [user_name,password,email,phone]
        cur.execute("INSERT INTO passenger (username, password, email, phone) VALUES (?,?,?,?)", newdata)
        con.commit()

    def signin(self,user_name, password):
        cur.execute("SELECT * FROM passenger WHERE username =(?) AND password=(?)",(user_name,password))
        a = cur.fetchall()
        if a == []:
            showerror('Sign In Failed', 'Invalid Username or Password')
            self.sm.current = 'screen_nine'
        elif a == [('','','','')]:
            showerror('Sign In Failed', 'Please Sign In')
            self.sm.current = 'screen_nine'
        else:
            self.sm.get_screen('screen_seven').ids.name_7.text = user_name
            self.sm.current = 'screen_five'

    def add_data(self):
        username = self.sm.get_screen('screen_nine').ids.login_username.text
        password = self.sm.get_screen('screen_nine').ids.login_password.text
        origin_newdata = self.sm.get_screen('screen_one').ids.origin.text
        destination_newdata = self.sm.get_screen('screen_one').ids.destination.text
        date_depart_newdata = self.sm.get_screen('screen_one').ids.departure_date.text
        time_depart_newdata = self.sm.get_screen('screen_seven').ids.departure_time_7.text
        time_arrive_newdata = self.sm.get_screen('screen_seven').ids.arrival_time_7.text
        no_coach_newdata = self.sm.get_screen('screen_three').ids.selected_coach_3.text
        no_seat_newdata = self.sm.get_screen('screen_three').ids.selected_seat_3.text
        no_pax_newdata = self.sm.get_screen('screen_one').ids.pax.text
        total_amount_newdata = self.sm.get_screen('screen_five').ids.prices_5.text
        payment_method_newdata = self.sm.get_screen('screen_six').ids.payment_method.text
        status = 'Upcoming'
        cur.execute("UPDATE passenger SET origin = (?), destination = (?), depart_date = (?), departure_time = (?), arrival_time = (?), coach = (?), seat = (?), pax = (?), amount= (?), payment_method= (?), status=(?) WHERE username =(?) AND password=(?)",
                    (origin_newdata,destination_newdata,date_depart_newdata,time_depart_newdata,time_arrive_newdata,
                     no_coach_newdata,no_seat_newdata,no_pax_newdata,total_amount_newdata, payment_method_newdata, status, username, password))
        con.commit()

    def signin_bookings(self, user_name, password):
        cur.execute("SELECT * FROM passenger WHERE username =(?) AND password=(?)", (user_name, password))
        a = cur.fetchall()
        if a == []:
            showerror('Sign In Failed', 'Invalid Username or Password')
            self.sm.current = 'screen_ten'
        elif a == [('', '', '', '')]:
            showerror('Sign In Failed', 'Please Sign In')
            self.sm.current = 'screen_ten'
        else:
            self.sm.current = 'screen_one'
            #self.sm.current = self.sm.get_screen('screen_one').ids.bottom_nav('booking_screen')

    def bookings(self):
        username9 = self.sm.get_screen('screen_nine').ids.login_username.text
        password9 = self.sm.get_screen('screen_nine').ids.login_password.text
        username10 = self.sm.get_screen('screen_ten').ids.login_username10.text
        password10 = self.sm.get_screen('screen_ten').ids.login_password10.text
        if username9 != '' or username10 != '':
            self.extract(username10 or username9, password10 or password9)
        else:
            txt = MDLabel(text='Please Sign In')
            window_bookings = Popup(title = 'Sign In Required', content=txt, size_hint=(None,None),size=(250,100))
            window_bookings.open()
            self.sm.current = 'screen_ten'

    def extract(self, username, password):
        ex = cur.execute("SELECT * FROM passenger WHERE username =(?) AND password =(?)",(username, password)).fetchall()
        date = str(ex[0][6])
        time = str(ex[0][7])
        coach = str(ex[0][9])
        seat = str(ex[0][10])
        price = str(ex[0][12])
        #payment = str(ex[0][13])
        status = str(ex[0][14])
        origin = str(ex[0][4])
        destination = str(ex[0][5])
        self.sm.get_screen('screen_one').ids.book_date.text  = date
        self.sm.get_screen('screen_one').ids.book_dtime.text = time
        self.sm.get_screen('screen_one').ids.book_username.text = username
        self.sm.get_screen('screen_one').ids.book_coach.text = coach
        self.sm.get_screen('screen_one').ids.book_seat.text = seat
        self.sm.get_screen('screen_one').ids.book_price.text = price
        self.sm.get_screen('screen_one').ids.status.text = status
        self.sm.get_screen('screen_one').ids.book_origin.text = origin
        self.sm.get_screen('screen_one').ids.book_destination.text = destination

    def change(self):
        username = self.sm.get_screen('screen_ten').ids.login_username10.text
        password = self.sm.get_screen('screen_ten').ids.login_password10.text
        self.sm.get_screen('screen_one').ids.status.text = 'Cancelled'
        cur.execute("UPDATE passenger SET status = 'Cancelled' WHERE username =(?) AND password=(?)",(username, password))
        con.commit()

    def refund(self):
        self.sm.get_screen('cancelling_ticket').ids.cancel_origin.text = self.sm.get_screen('screen_one').ids.book_origin.text
        self.sm.get_screen('cancelling_ticket').ids.cancel_destination.text = self.sm.get_screen('screen_one').ids.book_destination.text
        self.sm.get_screen('cancelling_ticket').ids.cancel_date.text = self.sm.get_screen('screen_one').ids.book_date.text
        self.sm.get_screen('cancelling_ticket').ids.cancel_dtime.text = self.sm.get_screen('screen_one').ids.book_dtime.text
        self.sm.get_screen('cancelling_ticket').ids.cancel_coach.text = self.sm.get_screen('screen_one').ids.book_coach.text
        self.sm.get_screen('cancelling_ticket').ids.cancel_seat.text = self.sm.get_screen('screen_one').ids.book_seat.text
        self.sm.get_screen('cancelling_ticket').ids.cancel_refund.text = self.sm.get_screen('screen_one').ids.book_price.text





#cur.execute("DELETE FROM passenger")
#con.commit()

TrainApp().run()
