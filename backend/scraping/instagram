import instaloader
import csv
import time

L = instaloader.Instaloader()
L.load_session_from_file('stefany.022')

from instaloader import Profile
profile = Profile.from_username(L.context, 'stefany.022')

followers = profile.get_followers()

with open('seguidores.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['username'])

    for follower in followers:
        writer.writerow([follower.username])
        print(f"Guardado: {follower.username}")
        time.sleep(5)  # Espera 5 segundos entre cada petición

