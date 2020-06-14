from forex_python.converter import CurrencyCodes, CurrencyRates
from tkinter import *
from tkinter import ttk
import datetime


def text_currency_name(curr_code):
    display_currency_name = currency_code.get_currency_name(curr_code) + \
                            "  (" + currency_code.get_symbol(curr_code) + ")"
    return display_currency_name


def text_rate(base, quote):
    rate = currency_rate.get_rate(base_currency_combobox.get(), quote_currency_combobox.get())
    currency_rate_label.configure(text=rate)


def show_base_currency_name(event):
    curr_code = text_currency_name(base_currency_combobox.get())
    base_currency_name_label.configure(text=curr_code)
    text_rate(base_currency_combobox.get(), quote_currency_combobox.get())


def show_quote_currency_name(event):
    curr_code = text_currency_name(quote_currency_combobox.get())
    quote_currency_name_label.configure(text=curr_code)
    text_rate(base_currency_combobox.get(), quote_currency_combobox.get())


currency_code = CurrencyCodes()
currency_rate = CurrencyRates()
currency = []
for curr in currency_rate.get_rates("USD"):
    currency.append(curr)
currency.sort()

main_window = Tk()
main_window.geometry("300x200")
base_currency_label = Label(main_window, text="Base Currency")
base_currency_label.grid(row=0, column=0)
quote_currency_label = Label(main_window, text="Quote Currency")
quote_currency_label.grid(row=0, column=1)
base_currency_combobox = ttk.Combobox(main_window, values=currency)
base_currency_combobox.grid(row=1, column=0)
quote_currency_combobox = ttk.Combobox(main_window, values=currency)
quote_currency_combobox.grid(row=1, column=1)
base_currency_name_label = Label(main_window)
base_currency_name_label.grid(row=2, column=0)
quote_currency_name_label = Label(main_window)
quote_currency_name_label.grid(row=2, column=1)
base_currency_combobox.current(31)
base_currency_name_label.configure(text=text_currency_name(base_currency_combobox.get()))
quote_currency_combobox.current(31)
quote_currency_name_label.configure(text=text_currency_name(quote_currency_combobox.get()))
base_currency_combobox.bind("<<ComboboxSelected>>", show_base_currency_name)
quote_currency_combobox.bind("<<ComboboxSelected>>", show_quote_currency_name)
currency_rate_label = Label(main_window, width=40, font=10)
currency_rate_label.place(x=0, y=100)
text_rate(base_currency_combobox.get(), quote_currency_combobox.get())

main_window.mainloop()

