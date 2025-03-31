import tkinter as tk
import main

root = tk.Tk()

root.geometry("1024x1024")

population_size_var = tk.IntVar()
domain_start_var = tk.IntVar()
domain_end_var = tk.IntVar()
a_var = tk.IntVar()
b_var = tk.IntVar()
c_var = tk.IntVar()
precision_var = tk.IntVar()
crossover_probability_var = tk.IntVar()
mutation_probability_var = tk.IntVar()
generation_number_var = tk.IntVar()


def submit():
    population_size = population_size_var
    domain_start = domain_start_var
    domain_end = domain_end_var
    a = a_var
    b = b_var
    c = c_var
    precision = precision_var
    crossover_probability = crossover_probability_var
    mutation_probability = mutation_probability_var
    generation_number = generation_number_var

    max_value = tk.Label(root, text=main.start(population_size_var, domain_start, domain_end, a, b, c, precision,
                                               crossover_probability, mutation_probability, generation_number)
                         , font=('calibre', 10, 'bold'))

    max_value.grid(row=29, column=0)
    text_widget = tk.Text(root, height=40, width=150)
    with open('Evolutie.txt', 'r') as file:
        data = file.read()
        text_widget.insert(tk.END, data)

    text_widget.grid(row=30, column=0, columnspan=0)
    draw_text()

def default():
    max_value = tk.Label(root, text=main.start(20,-1,2,-1,1,2,6,25,1,50)
                         ,font=('calibre', 10, 'bold'))

    max_value.grid(row=29, column=0)
    text_widget = tk.Text(root, height=40, width=150)
    with open('Evolutie.txt', 'r') as file:
        data = file.read()
        text_widget.insert(tk.END, data)

    text_widget.grid(row=30, column=0, columnspan=2)
    draw_text()

def draw_text():
    population_size_label = tk.Label(root, text='Population size', font=('calibre', 10, 'bold'))
    domain_start_label = tk.Label(root, text='Domain start', font=('calibre', 10, 'bold'))
    domain_end_label = tk.Label(root, text='Domain end', font=('calibre', 10, 'bold'))
    a_label = tk.Label(root, text='A', font=('calibre', 10, 'bold'))
    b_label = tk.Label(root, text='B', font=('calibre', 10, 'bold'))
    c_label = tk.Label(root, text='C', font=('calibre', 10, 'bold'))
    precision_label = tk.Label(root, text='Precision', font=('calibre', 10, 'bold'))
    crossover_probability_label = tk.Label(root, text='Crossover', font=('calibre', 10, 'bold'))
    mutation_probability_label = tk.Label(root, text='Mutation', font=('calibre', 10, 'bold'))
    generation_number_label = tk.Label(root, text='Generation', font=('calibre', 10, 'bold'))


    population_size_entry = tk.Entry(root, textvariable=population_size_var)
    domain_start_entry = tk.Entry(root, textvariable=domain_start_var)
    domain_end_entry = tk.Entry(root, textvariable=domain_end_var)
    a_entry = tk.Entry(root, textvariable=a_var)
    b_entry = tk.Entry(root, textvariable=b_var)
    c_entry = tk.Entry(root, textvariable=c_var)
    precision_entry = tk.Entry(root, textvariable=precision_var)
    crossover_probability_entry = tk.Entry(root, textvariable=crossover_probability_var)
    mutation_probability_entry = tk.Entry(root, textvariable=mutation_probability_var)
    generation_number_entry = tk.Entry(root, textvariable=generation_number_var)


    sub_btn = tk.Button(root, text='Submit', command=submit)
    default_btn = tk.Button(root, text='Default', command=default)

    population_size_label.grid(row =0 , column=0, sticky=tk.W)
    population_size_entry.grid(row=0, column=1, sticky=tk.W)
    domain_start_label.grid(row=1, column=0, sticky=tk.W)
    domain_start_entry.grid(row=1, column=1, sticky=tk.W)
    domain_end_label.grid(row=2, column=0, sticky=tk.W)
    domain_end_entry.grid(row=2, column=1, sticky=tk.W)
    a_label.grid(row=3, column=0, sticky=tk.W)
    a_entry.grid(row=3, column=1, sticky=tk.W)
    b_label.grid(row=4, column=0, sticky=tk.W)
    b_entry.grid(row=4, column=1, sticky=tk.W)
    c_label.grid(row=5, column=0, sticky=tk.W)
    c_entry.grid(row=5, column=1, sticky=tk.W)
    precision_label.grid(row=6, column=0, sticky=tk.W)
    precision_entry.grid(row=6, column=1, sticky=tk.W)
    crossover_probability_label.grid(row=7, column=0, sticky=tk.W)
    crossover_probability_entry.grid(row=7, column=1, sticky=tk.W)
    mutation_probability_label.grid(row=8, column=0, sticky=tk.W)
    mutation_probability_entry.grid(row=8, column=1, sticky=tk.W)
    generation_number_label.grid(row=9, column=0, sticky=tk.W)
    generation_number_entry.grid(row=9, column=1, sticky=tk.W, rowspan=2)


    sub_btn.grid(row=20, column=4, sticky=tk.W, rowspan=2)
    default_btn.grid(row=20, column=5, sticky=tk.W, rowspan=2)

draw_text()
root.mainloop()
