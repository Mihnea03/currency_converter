import tkinter as tk
from tkinter import ttk, messagebox
from data import get_currency_names, get_data

def main():
    currencies = get_currency_names()
    conversion_rates = get_data()
    values = [f"{key} ({value})" for (key, value) in currencies.items()]

    window = tk.Tk()
    window.title("Currency Converter")
    window.config(width=300, height=200, padx=15, pady=15, bg='white')
    
    input = tk.StringVar()
    input_box = tk.Entry(width=20, textvariable=input)
    input_box.grid(column=0, row=0, columnspan=1, padx=5)

    input_curr = tk.StringVar()
    input_curr_cb = ttk.Combobox(textvariable=input_curr, width=20, background='white')
    input_curr_cb['values'] = values
    input_curr_cb['state'] = 'readonly'
    input_curr_cb.grid(column=1, row=0, columnspan=1, padx=5)

    is_equal_label = tk.Label(text="is equal to:", width=10, bg='white')
    is_equal_label.grid(column=2, row=0, columnspan=1, padx=5)

    output = tk.StringVar()
    output_box = tk.Entry(width=20, textvariable=output)
    output_box.grid(column=0, row=1, columnspan=1, padx=5)

    output_curr = tk.StringVar()
    output_curr_cb = ttk.Combobox(textvariable=output_curr, width=20, background='white')
    output_curr_cb['values'] = values
    output_curr_cb['state'] = 'readonly'
    output_curr_cb.grid(column=1, row=1, columnspan=1, padx=5)

    def calc_conversion():
        try:
            original_value = round(float(input.get()), 7)
        except ValueError:
            messagebox.showerror(title="Invalid value format!", message="Given value should contain only digits and '.'!")
            return
        
        try:
            inputcurr = currencies[input_curr.get().split("(")[0].strip()]
            outputcurr = currencies[output_curr.get().split("(")[0].strip()]
        except KeyError:
            messagebox.showerror(title="No currency given!", message="The given currency and the desired currency should be selected!")
            return
        
        value = original_value / conversion_rates[inputcurr] * conversion_rates[outputcurr]
        output.set(round(value, 7))
        return

    calculate = tk.Button(width=10, height=1, bg='white', text='Calculate', command=calc_conversion)
    calculate.grid(column=2, row=1, padx=5)

    window.mainloop()

if __name__ == '__main__':
    main()