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
    "Astra": (639, 848),
    "Breach": (710, 832),
    "Brimstone": (790, 840),
    "Chamber": (876, 835),
    "Cypher": (872, 925),
    "Deadlock": (1055, 823),
    "Fade": (1111, 838),
    "Gekko": (1210, 828),
    "Harbor": (1306, 837),
    "Jett": (698, 927),
    "Kay/O": (794, 925),
    "Killjoy": (855, 931),
    "Neon": (950, 918),
    "Omen": (1047, 925),
    "Phoenix": (1120, 940),
    "Raze": (1217, 924),
    "Reyna": (1297, 931),
    "Sage": (606, 977),
    "Skye": (718, 1002),
    "Sova": (802, 992),
    "Viper": (802, 992),
    "Yoru": (942, 989),
    "Iso":(609, 922),
}

def pick_agent(agent):
    text_output.config(text="OK! Now go play and carry your team!")
    while True:
        pg.moveTo(agent_coordinates[agent])
        pg.doubleClick()
        pg.PAUSE = 0.015
        pg.moveTo(892, 739)
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
    "Sage", "Skye", "Sova", "Viper", "Yoru", "Iso"
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
