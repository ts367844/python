import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import pygame
import time
import os
import json
from datetime import date, datetime
import pytz
import swisseph as swe
from geopy.geocoders import Nominatim

# --------------------------------------------------
# CONFIG
# --------------------------------------------------

CONFIG_FILE = "user_config.json"
TRACK_FILE = "last_played.txt"
START_DELAY = 60  # 1 minutes

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

RASHI_URLS = {
    "mesh": "https://www.divyabhaskar.co.in/rashifal/13/today",
    "vrushabh": "https://www.divyabhaskar.co.in/rashifal/14/today",
    "mithun": "https://www.divyabhaskar.co.in/rashifal/15/today",
    "kark": "https://www.divyabhaskar.co.in/rashifal/16/today",
    "sinh": "https://www.divyabhaskar.co.in/rashifal/17/today",
    "kanya": "https://www.divyabhaskar.co.in/rashifal/18/today",
    "tula": "https://www.divyabhaskar.co.in/rashifal/19/today",
    "vrushchik": "https://www.divyabhaskar.co.in/rashifal/20/today",
    "dhanu": "https://www.divyabhaskar.co.in/rashifal/21/today",
    "makar": "https://www.divyabhaskar.co.in/rashifal/22/today",
    "kumbh": "https://www.divyabhaskar.co.in/rashifal/23/today",
    "meen": "https://www.divyabhaskar.co.in/rashifal/24/today",
}

RASHIS = [
    "mesh", "vrushabh", "mithun", "kark", "sinh", "kanya",
    "tula", "vrushchik", "dhanu", "makar", "kumbh", "meen"
]

# --------------------------------------------------
# DAILY CHECK
# --------------------------------------------------

def already_played_today():
    if not os.path.exists(TRACK_FILE):
        return False
    with open(TRACK_FILE, "r") as f:
        return f.read().strip() == str(date.today())

def mark_played_today():
    with open(TRACK_FILE, "w") as f:
        f.write(str(date.today()))

# --------------------------------------------------
# USER CONFIG (SAVE ONCE)
# --------------------------------------------------

def load_or_create_user_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)

    # First run only
    print("First time setup – enter birth details")

    dob = input("Birth Date (YYYY-MM-DD): ").strip()
    tob = input("Birth Time (HH:MM, 24h): ").strip()
    place = input("Birth Place (Village/Town, District, State): ").strip()

    config = {
        "dob": dob,
        "tob": tob,
        "place": place
    }

    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

    print("Details saved successfully.")
    return config

# --------------------------------------------------
# ASTROLOGY
# --------------------------------------------------

def get_lat_lon(place):
    geolocator = Nominatim(user_agent="rashi_app")
    location = geolocator.geocode(place)
    if not location:
        raise ValueError("Could not determine location")
    return location.latitude, location.longitude

def get_chandra_rashi(dob, tob, place):
    lat, lon = get_lat_lon(place)

    local_tz = pytz.timezone("Asia/Kolkata")
    dt_local = datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
    dt_local = local_tz.localize(dt_local)
    dt_utc = dt_local.astimezone(pytz.utc)

    jd = swe.julday(
        dt_utc.year,
        dt_utc.month,
        dt_utc.day,
        dt_utc.hour + dt_utc.minute / 60
    )

    swe.set_topo(lon, lat, 0)
    moon_pos, _ = swe.calc_ut(jd, swe.MOON)
    moon_longitude = moon_pos[0]

    return RASHIS[int(moon_longitude // 30)]

# --------------------------------------------------
# MAIN LOGIC
# --------------------------------------------------

def play_rashi_bhavishya():
    if already_played_today():
        return  # silent exit

    config = load_or_create_user_config()

    rashi = get_chandra_rashi(
        config["dob"],
        config["tob"],
        config["place"]
    )

    url = RASHI_URLS[rashi]
    response = requests.get(url, headers=HEADERS, timeout=10)

    if response.status_code != 200:
        return

    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.find("div", class_="a6b3d8fe")
    if not content:
        return

    text = content.text.strip()[:3000]

    gTTS(text=text, lang="gu").save("rashi.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("rashi.mp3")
    mark_played_today()          # 👈 mark FIRST

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
      time.sleep(1)


# --------------------------------------------------
# ENTRY POINT
# --------------------------------------------------

if __name__ == "__main__":
    time.sleep(60)
    play_rashi_bhavishya()