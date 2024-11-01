import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import requests
from datetime import datetime

def find_earthquakes():
    start_time = start_date.get()
    end_time = end_date.get()
    min_magnitude = min_mag.get()
    limit = results_limit.get()
    order_by = order.get()

    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson",
        "starttime": start_time,
        "endtime": end_time,
        "minmagnitude": min_magnitude,
        "limit": limit,
        "orderby": order_by
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        earthquakes = data.get("features", [])

        if earthquakes:
            results.delete(*results.get_children())

            for eq in earthquakes:
                lugar = eq["properties"]["place"]
                magnitud = eq["properties"]["mag"]
                tiempo = datetime.utcfromtimestamp(eq["properties"]["time"] / 1000).strftime('%Y-%m-%d %H:%M:%S')
                results.insert("", "end", values=(lugar, magnitud, tiempo))
        else:
            messagebox.showinfo("Resultado", "No se encontraron terremotos en ese rango.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error al consultar la API: {e}")


window = tk.Tk()
style = ttk.Style()
title = ttk.Label(window, text="Terremotos", font=("Arial", 16, "bold"), background="#fef2f2")
filters_frame = ttk.Frame(window, padding="20")
ttk.Label(filters_frame, text="Fecha de inicio:").grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
start_date = DateEntry(filters_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
ttk.Label(filters_frame, text="Fecha de fin:").grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
end_date = DateEntry(filters_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
ttk.Label(filters_frame, text="Magnitud mínima:").grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
min_mag = ttk.Entry(filters_frame)
ttk.Label(filters_frame, text="Límite de resultados:").grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
results_limit = ttk.Entry(filters_frame)
ttk.Label(filters_frame, text="Ordenar por:").grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
order = ttk.Combobox(filters_frame, values=["time", "time-asc", "magnitude", "magnitude-asc"])
find_results = ttk.Button(filters_frame, text="Buscar", command=find_earthquakes)
results = ttk.Treeview(window, columns=("Lugar", "Magnitud", "Tiempo"), show='headings')
scrollbar = ttk.Scrollbar(window, orient="vertical", command=results.yview)


def set_window_properties():
    window.title("Terremotos - API de USGS")
    window.geometry("700x600")
    window.configure(bg="#fef2f2")
    filters_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))
    title.grid(row=0, column=0, pady=10)
    results.heading("Lugar", text="Lugar")
    results.heading("Magnitud", text="Magnitud")
    results.heading("Tiempo", text="Tiempo")
    results.grid(row=2, column=0, sticky=(tk.W, tk.E), padx=20, pady=(10, 20))
    results.column("Lugar", width=300)
    results.column("Magnitud", width=100)
    results.column("Tiempo", width=150)
    results.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=2, column=1, sticky=(tk.N, tk.S))

def style_window():
    style.configure("TFrame", background="#fef2f2")
    style.configure("TLabel", background="#fef2f2", font=("Arial", 12))
    style.configure("TButton", background="#fca5a5", foreground="#7f1d1d", font=("Arial", 12))
    style.map("TButton", background=[('active', '#f87171')])
    style.configure("Treeview", font=("Arial", 10), rowheight=25)
    style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#fee2e2", foreground="#450a0a")

def set_filters_frame():
    start_date.grid(column=1, row=0, sticky=(tk.W, tk.E), padx=5, pady=5)
    end_date.grid(column=1, row=1, sticky=(tk.W, tk.E), padx=5, pady=5)
    min_mag.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=5, pady=5)
    results_limit.grid(column=1, row=3, sticky=(tk.W, tk.E), padx=5, pady=5)
    order.grid(column=1, row=4, sticky=(tk.W, tk.E), padx=5, pady=5)
    order.current(0)
    find_results.grid(column=0, row=5, columnspan=2, pady=10)

set_window_properties()
style_window()
set_filters_frame()
window.mainloop()