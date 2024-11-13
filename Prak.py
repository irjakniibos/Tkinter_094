import tkinter as tk
from tkinter import messagebox

def hasil_prediksi():
    try:
        for entry in entries:
            nilai = int(entry.get())
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0-100")
        hasil_label.config(text="Prediksi Prodi: teknologi informasi")
    except ValueError as ve:
        messagebox.showerror("Input Error","Pastikan semua input adalah angka antara 0 - 100")

# Create main window
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi")
root.geometry("500x800")
root.configure(bg="#f0f0f0")

# Label judul
judul_label = tk.Label(root,text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 18, "bold"),bg="#f0f0f0")
judul_label.pack(pady=20)

# Frame input nilai
frame_input = tk.Frame(root, bg="#f0f0f0")
frame_input.pack(pady=10)

# Create entries
entries=[]
for i in range(10):
    label = tk.Label(frame_input,text=f"Nilai Mata Pelajaran{i+1}:",font=("Arial",12),bg="#f0f0f0")
    label.grid(row=i,column=0,padx=10,pady=5,sticky="e")
    entry = tk.Entry(frame_input,width=10,font=("Arial",12))
    entry.grid(row=i,column=1,padx=10,pady=5)
    entries.append(entry)


# Prediction button
prediksi_button = tk.Button(root,text="Hasil Prediksi",command=hasil_prediksi,font=("Arial", 12, "bold"),bg="#4CAF50",fg="black",activebackground="#45a049",padx=20,pady=10)
prediksi_button.pack(pady=30)

# Result label
hasil_label = tk.Label(root,text="",font=("Arial", 14, "bold"),fg="blue",bg="#f0f0f0")
hasil_label.pack(pady=20)

# Start the application
root.mainloop()