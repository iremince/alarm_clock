import tkinter as tk
import datetime
import time
import pygame # type: ignore

def show_custom_alarm():
    custom_window = tk.Toplevel(root)
    custom_window.title("🌟 Zaman Doldu 🌟")
    custom_window.geometry("300x150")
    custom_window.configure(bg="#CEEDCE")

    custom_window.attributes("-topmost", True)  # Pencereyi en üstte göster
    custom_window.lift()                        # Diğer pencerelerin üstüne getir
    custom_window.focus_force()                 # O pencereye odaklan

    label = tk.Label(custom_window, text="Ders bitti, dinlenme zamanı 💖", font=("Verdana", 10 , " italic"), bg="#CEEDCE", fg="#756AA4")
    label.pack(expand=True)

    btn_ok = tk.Button(custom_window, text="Tamam" , fg="#FFFFFF", command=custom_window.destroy, bg="#756AA4")
    btn_ok.pack(pady=10)

def start_alarm():
    try:
        h = int(entry_hours.get())
        m = int(entry_minutes.get())
        s = int(entry_seconds.get())
    except ValueError:
        tk.messagebox.showerror("Hata", "Lütfen geçerli sayılar girin!")
        return

    total_seconds = h * 3600 + m * 60 + s
    if total_seconds <= 0:
        tk.messagebox.showerror("Hata", "Lütfen 0'dan büyük bir süre girin!")
        return

    target_time = datetime.datetime.now() + datetime.timedelta(seconds=total_seconds)
    print(f"Alarm {h} saat, {m} dakika, {s} saniye sonra çalacak!")
    root.withdraw()

    # Bekleme süreci ana döngüyü dondurmasın diye burada root.after kullanıyoruz
    def check_alarm():
        if datetime.datetime.now() >= target_time:
            pygame.mixer.init()
            pygame.mixer.music.load(r"") # alarm.wav dosyasını masaüstüne veya bu dosyayla aynı klasöre koymanız gerekir.
            pygame.mixer.music.play()
            show_custom_alarm()
        else:
            root.after(1000, check_alarm)

    root.after(1000, check_alarm)

# Arayüz
root = tk.Tk()
root.title("Alarm")
root.geometry("300x200")
root.configure(bg="#CEE6ED")  # Mavi tonlarında arka plan


tk.Label(root, text="Saat:" , fg="#E99BB0" , bg="#CEE6ED" , font=("Verdana", 10 , " bold")).grid(row=0, column=0, padx=10, pady=10)
entry_hours = tk.Entry(root, width=5)
entry_hours.grid(row=0, column=1)

tk.Label(root, text="Dakika:", fg="#E99BB0" , bg="#CEE6ED" , font=("Verdana", 10 , " bold")).grid(row=1, column=0, padx=10, pady=10)
entry_minutes = tk.Entry(root, width=5)
entry_minutes.grid(row=1, column=1)

tk.Label(root, text="Saniye:", fg="#E99BB0" , bg="#CEE6ED" , font=("Verdana", 10 , " bold")).grid(row=2, column=0, padx=10, pady=10)
entry_seconds = tk.Entry(root, width=5)
entry_seconds.grid(row=2, column=1)

btn_start = tk.Button(root, text="Alarmı Kur", fg="#E99BB0" , font=("Verdana", 10 , " bold") , command=start_alarm)
btn_start.grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()
