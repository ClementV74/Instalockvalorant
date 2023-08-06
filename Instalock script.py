import subprocess
import sys

def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyautogui", "keyboard", "tk"])
    except subprocess.CalledProcessError:
        print("Erreur lors de l'installation des requirements.")
        sys.exit(1)

# Vérifier si les requirements sont déjà installés
try:
    import pyautogui
    import keyboard
    import tkinter as tk
except ImportError:
    print("Les requirements ne sont pas installés. Installation en cours...")
    install_requirements()

import pyautogui as pg
import keyboard
import tkinter as tk

window = tk.Tk()
window.geometry("830x605")
window.title("Valorant Instalocker")
window.resizable(False, False)

agent_coordinates = {
    "Astra": (544, 927),
    "Breach": (625, 925),
    "Brimstone": (717, 925),
    "Chamber": (791, 925),
    "Cypher": (872, 925),
    "Deadlock": (960, 920),
    "Fade": (1043, 925),
    "Gekko": (1131, 925),
    "Harbor": (1214, 925),
    "Jett": (1300, 925),
    "Kay/O": (1385, 918),
    "Killjoy": (540, 1007),
    "Neon": (622, 993),
    "Omen": (703, 993),
    "Phoenix": (790, 993),
    "Raze": (876, 999),
    "Reyna": (963, 996),
    "Sage": (1046, 1000),
    "Skye": (1130, 996),
    "Sova": (1210, 994),
    "Viper": (1306, 997),
    "Yoru": (1378, 998)
}

def pick_agent(agent):
    text_output.config(text="OK! Now go play and carry your team!")
    while True:
        pg.moveTo(agent_coordinates[agent])
        pg.doubleClick()
        pg.PAUSE = 0.015
        pg.moveTo(954, 812)
        pg.doubleClick()

        try:
            if keyboard.is_pressed('p'):
                break
        except:
            break

text_output = tk.Label(window, text="", fg='black', font=("Helvetica", 12))
text_output.grid(row=3, column=0, columnspan=5, pady=10)

agents = [
    "Astra", "Breach", "Brimstone", "Chamber", "Cypher", "Deadlock", "Fade", "Gekko",
    "Harbor", "Jett", "Kay/O", "Killjoy", "Neon", "Omen", "Phoenix", "Raze", "Reyna",
    "Sage", "Skye", "Sova", "Viper", "Yoru"
]

buttons = []
for idx, agent in enumerate(agents):
    button = tk.Button(
        text=f"Pick {agent}",
        command=lambda a=agent: pick_agent(a),
        fg='white',
        bg='black',
        font=("Helvetica", 12),
        width=15,
        height=2,
        relief="ridge"
    )
    button.grid(row=4 + idx // 5, column=idx % 5, padx=10, pady=10)
    buttons.append(button)

stop_label = tk.Label(window, text="To stop the program, hold 'P'", fg="black", font=('Helvetica', 12))
stop_label.grid(row=5 + (len(agents) - 1) // 5, column=0, columnspan=5, pady=10)

# Style pour le pseudo "Fee Gaffe"
fee_gaffe_label = tk.Label(window, text="Fee Gaffe", fg='purple', font=("Arial", 30, "bold"))
fee_gaffe_label.grid(row=0, column=0, columnspan=5, pady=20)

title_label = tk.Label(window, text='Valorant agent picker', fg='black', font=("Helvetica", 16, "bold"))
title_label.grid(row=1, column=0, columnspan=5, pady=10)

if __name__ == "__main__":
    window.mainloop()
