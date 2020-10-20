## Konfiguracja
  
- **emailMSTeams/passwordMSTeams/passwordPG/usernamePG:**  
Wpisz swoje dane logowanie do MS Teams i Moodla

- **run_at_time:**  
O której uruchomić skrypt? Aby się uruchomił natychmiast, pozostaw pole puste lub uzupełnij "07:00", aby od siódmej rano szukał spotkania do dołączenia. Upewnij się, że podałeś email/password/username.

- **organisation_num:**     
Numer organizacji w MS teams z listy wybierania (liczone od 1)

- **random_delay:**  
Dodaje losowe opóźnienie (10s-30s) żeby wszyscy w jednej sekundzie nie dołączyli XD Przyjmuje wartości true/false.

- **check_interval:**  
Czas (w sekundach), w któym ma sprawdzać, czy istnieje nowe spotkanie na MS Teams.

- **auto_leave_after_min:**  
Czas po jakim ma automatycznie wyjść ze spotkania (w minutach).

- **leave_if_last:**  
Czy ma wyjść jeśli jesteś ostatnią/jedyną osobą na spotkaniu? Przyjmuje wartości true/false.

- **headless:**     
Nie otwiera GUI Chrome/Chromium/Edge. Przyjmuje wartości true/false.

- **mute_audio:**     
Wyłącza audio w MS Teams, ale organizator chyba to widzi, kto ma wyłączone audio bezpośrednio w MS Teams z tego co wiem. Przyjmuje wartości true/false.

- **chrome_type:**     
Z jakiego chromopodobnego drivera ma korzystać: `google-chrome`, `chromium`, `msedge`. Domyślne używany jest Google Chrome, ale pod linuksy polecam ustawić Chromium.

- **blacklist:**  
Do jakich kanałów/zespołów bot ma nie dołączac i nie sprawdzać, czy jest nowe spotkanie do dołączenia.
Format:
```json
"blacklist": [  
  {  
    "team_name": "Test1",  
    "channel_names": [  
      "Ogólny"
    ]  
  }
]
```

## Uruchomienie
  
 1. Edytuj "config.json" i uzupełnij wedle potrzeb
 2. Zainstaluj Selenium, webdriver_manager i pozostałe rzeczy pod pythona
 3. Uruchom: `python a.py`  
 