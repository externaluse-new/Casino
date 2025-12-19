
import tkinter as tk
import random
import pygame

# ---------- INIT SOUND ----------
pygame.mixer.init()
win_sound = pygame.mixer.Sound("win.wav")
spin_sound = pygame.mixer.Sound("spin.wav")

# ---------- CONFIG ----------
EMOJIS = ["🍒", "🍋", "🔔", "⭐", "💎", "7️⃣"]
WIN_PROBABILITY = 0.1  # 1 win in 10 spins

credits = 0
spin_count = 0

# ---------- FUNCTIONS ----------
def start_game():
    global credits
    val = credit_entry.get()
    if not val.isdigit() or int(val) <= 0:
        status.config(text="❌ Enter valid credits", fg="red")
        return
    credits = int(val)
    update_credits()
    status.config(text="🎮 Game Started", fg="lime")

def spin():
    global credits, spin_count
    if credits <= 0:
        status.config(text="❌ No credits left", fg="red")
        return

    credits -= 1
    spin_count += 1
    update_credits()

    spin_sound.play()
    flash_lights()

    # Decide win or lose
    is_win = random.random() < WIN_PROBABILITY

    if is_win:
        symbol = random.choice(EMOJIS)
        reels = [symbol, symbol, symbol]
        credits += 5
        status.config(text="🎉 WIN! +5 Credits", fg="gold")
        win_sound.play()
    else:
        reels = random.choices(EMOJIS[:-1], k=3)  # avoid 777 emoji on loss
        status.config(text="😢 Try Again", fg="white")

    r1.config(text=reels[0])
    r2.config(text=reels[1])
    r3.config(text=reels[2])
    update_credits()

def update_credits():
    credit_label.config(text=f"Credits: {credits}")

def flash_lights():
    for i in range(6):
        window.after(i*100, lambda c=i: light.config(bg="gold" if c % 2 == 0 else "#1c1c1c"))

# ---------- UI ----------
window = tk.Tk()
window.title("🎰 777 Emoji Arcade")
window.geometry("450x480")
window.configure(bg="#1c1c1c")
window.resizable(False, False)

title = tk.Label(window, text="🎰 777 EMOJI ARCADE", font=("Helvetica", 20, "bold"), fg="gold", bg="#1c1c1c")
title.pack(pady=10)

light = tk.Label(window, text=" ", bg="#1c1c1c", width=40, height=1)
light.pack()

credit_entry = tk.Entry(window, font=("Arial", 12), justify="center")
credit_entry.pack()
credit_entry.insert(0, "Enter credits")

tk.Button(window, text="START", command=start_game, bg="green", fg="white", width=20).pack(pady=6)

credit_label = tk.Label(window, text="Credits: 0", font=("Arial", 14), fg="white", bg="#1c1c1c")
credit_label.pack(pady=5)

frame = tk.Frame(window, bg="#1c1c1c")
frame.pack(pady=20)

style = {"font": ("Arial", 40), "bg": "black", "fg": "white", "width": 3}
r1 = tk.Label(frame, text="❔", **style)
r2 = tk.Label(frame, text="❔", **style)
r3 = tk.Label(frame, text="❔", **style)

r1.grid(row=0, column=0, padx=8)
r2.grid(row=0, column=1, padx=8)
r3.grid(row=0, column=2, padx=8)

tk.Button(window, text="🎲 SPIN 🎲", command=spin, bg="orange", fg="black", width=25, height=2).pack(pady=10)

status = tk.Label(window, text="Welcome to the Arcade!", font=("Arial", 12), fg="white", bg="#1c1c1c")
status.pack(pady=10)

window.mainloop()
