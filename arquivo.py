import os
import urllib.request
import json
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def get_own_ip_info():
    url = "http://ip-api.com/json/"
    response = urllib.request.urlopen(url)
    data = response.read()
    result = json.loads(data)
    return result

def get_ip_info(ip):
    api = "http://api.ipstack.com/"
    access_key = "fd0c1eae3c2d27ee676af0db2b864b0e"
    response = urllib.request.urlopen(api + ip + '?access_key=' + access_key)
    data = response.read()
    result = json.loads(data)
    return result

def track_ip():
    ip = ip_entry.get()
    if ip.lower() == "sair":
        root.quit()
    else:
        try:
            result = get_ip_info(ip)
            result1 = get_own_ip_info()
            if result1['status'] == 'success':
                lati = result['latitude']
                lon = result['longitude']
                languages = result['location'].get('languages', [])
                languages_str = ", ".join([lang['name'] for lang in languages])
                result_text = (
                    f"IP: {result['ip']}\n"
                    f"Tipo de IP: {result['type']}\n"
                    f"Nome do Continente: {result['continent_name']}\n"
                    f"Código do Continente: {result['continent_code']}\n"
                    f"País: {result['country_name']}\n"
                    f"Código do País: {result1['countryCode']}\n"
                    f"Nome da Região: {result['region_name']}\n"
                    f"Código da Região: {result['region_code']}\n"
                    f"Cidade: {result['city']}\n"
                    f"CEP: {result['zip']}\n"
                    f"Fuso Horário: {result1['timezone']}\n"
                    f"ISP: {result1['isp']}\n"
                    f"Latitude: {lati:.4f}\n"
                    f"Longitude: {lon:.4f}\n"
                    f"Línguas: {languages_str}\n"
                )
                result_label.config(text=result_text)
            else:
                result_label.config(text=f"Desculpe, por favor, digite o IP [{ip}] novamente")
        except Exception as e:
            result_label.config(text=f"Erro: {str(e)}")

def create_gui():
    global root, ip_entry, result_label
    root = tk.Tk()
    root.title("IP Tracker")
    root.geometry("360x640")
    root.config(bg='#0d0d0d')

    script_dir = os.path.dirname(__file__)

    icon_image = tk.PhotoImage(file=os.path.join(script_dir, 'logo.png'))
    root.iconphoto(True, icon_image)

    image_path = os.path.join(script_dir, 'QR.png')
    image = Image.open(image_path)
    image = image.resize((100, 100), Image.LANCZOS)
    qr_photo = ImageTk.PhotoImage(image)
    qr_label = tk.Label(root, image=qr_photo, bg='#0d0d0d')
    qr_label.photo = qr_photo
    qr_label.pack(side=tk.BOTTOM, pady=(0, 10))

    footer_label = tk.Label(root, text="Feito por Matheus 802 CMM", bg='#0d0d0d', fg='white', font=('Roboto', 12))
    footer_label.pack(side=tk.BOTTOM, pady=(0, 10))

    ip_label = tk.Label(root, text="Digite o IP:", bg='#0d0d0d', fg='white', font=('Roboto', 14))
    ip_label.pack(pady=10)

    ip_entry = tk.Entry(root, width=50, font=('Roboto', 12))
    ip_entry.pack(pady=10)

    track_button = tk.Button(root, text="Rastrear", command=track_ip, bg='#ff0000', fg='white', font=('Roboto', 12))
    track_button.pack(pady=10)

    result_label = tk.Label(root, text="", bg='#0d0d0d', fg='white', font=('Roboto', 12))
    result_label.pack(pady=10)

    root.mainloop()

create_gui()
