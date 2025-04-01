import tkinter as tk
from tkinter import ttk, scrolledtext
import main


def create_gui():
    root = tk.Tk()
    root.title("Genetic Algorithm Optimizer")
    root.geometry("1200x800")
    root.configure(padx=20, pady=20, bg="#f2d7ce")

    #default variables, as in the example from the assignment
    population_size_var = tk.IntVar(value=20)
    domain_start_var = tk.IntVar(value=-1)
    domain_end_var = tk.IntVar(value=2)
    a_var = tk.IntVar(value=-1)
    b_var = tk.IntVar(value=1)
    c_var = tk.IntVar(value=2)
    precision_var = tk.IntVar(value=6)
    crossover_probability_var = tk.IntVar(value=25)
    mutation_probability_var = tk.IntVar(value=1)
    generation_number_var = tk.IntVar(value=50)

    result_var = tk.StringVar(value="Results will appear here")

    def submit():
        #input the values
        population_size = population_size_var.get()
        domain_start = domain_start_var.get()
        domain_end = domain_end_var.get()
        a = a_var.get()
        b = b_var.get()
        c = c_var.get()
        precision = precision_var.get()
        crossover_probability = crossover_probability_var.get()
        mutation_probability = mutation_probability_var.get()
        generation_number = generation_number_var.get()

        #run the algorithm
        result, real_value2 = main.start(population_size, domain_start, domain_end, a, b, c,
                            precision, crossover_probability, mutation_probability,
                            generation_number)
        result_var.set(f"Maximum Value: {result}")

        import numpy as np
        from matplotlib import pyplot as plt

        def PolyCoefficients(x, coeffs):
            o = len(coeffs)
            print(f'# This is a polynomial of order {o}.')
            y = 0
            for i in range(o):
                y += coeffs[i] * x ** i
            return y

        x = np.linspace(domain_start, domain_end, 100)
        coeffs = [c, b, a]
        plt.plot(x, PolyCoefficients(x, coeffs))
        plt.plot(float(real_value2), PolyCoefficients(float(real_value2), coeffs), marker="x")
        plt.show()
        #extract from the folder the log
        with open('Evolutie.txt', 'r') as file:
            data = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, data)


    # some styles I found online
    input_frame = ttk.LabelFrame(root, text="Algorithm Parameters", padding=10)
    input_frame.pack(fill="x", expand=False, padx=5, pady=5)

    button_frame = ttk.Frame(root, padding=10)
    button_frame.pack(fill="x", expand=False, padx=5, pady=5)

    result_frame = ttk.LabelFrame(root, text="Results", padding=10)
    result_frame.pack(fill="both", expand=True, padx=5, pady=5)


    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 10))
    style.configure("TButton", font=("Arial", 10, "bold"))
    style.configure("TEntry", font=("Arial", 10))
    style.configure("TLabelframe", font=("Arial", 11, "bold"))

    param_labels = ["Population Size:", "Domain Start:", "Domain End:",
                    "Coefficient A:", "Coefficient B:", "Coefficient C:",
                    "Precision:", "Crossover Probability (%):",
                    "Mutation Probability (%):", "Number of Generations:"]

    param_vars = [population_size_var, domain_start_var, domain_end_var,
                  a_var, b_var, c_var, precision_var,
                  crossover_probability_var, mutation_probability_var,
                  generation_number_var]

    #split the inputs in 2 columns
    for i, (label, var) in enumerate(zip(param_labels, param_vars)):
        row = i % 5
        col = i // 5 * 2

        ttk.Label(input_frame, text=label).grid(row=row, column=col, sticky="w", padx=5, pady=5)
        ttk.Entry(input_frame, textvariable=var, width=10).grid(row=row, column=col + 1, padx=5, pady=5, sticky="w")


    ttk.Button(button_frame, text="Run Algorithm", command=submit, style="TButton").pack(side="left", padx=10)

    #logs
    ttk.Label(result_frame, textvariable=result_var, font=("Arial", 11, "bold")).pack(fill="x", pady=5)
    text_area = scrolledtext.ScrolledText(result_frame, wrap=tk.WORD, height=20, font=("Consolas", 10))
    text_area.pack(fill="both", expand=True, padx=5, pady=5)

    return root



app = create_gui()
app.mainloop()