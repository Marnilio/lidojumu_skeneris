# Lidojumu Skeneris: Rīga → Milāna (ar e-pasta paziņojumiem)

Šī ir **Python skripta** aplikācija, kas meklē **vienvirziena lidojumus no Rīgas (RIX) uz Milānu** (MXP, BGY, LIN) **norādītajā datumā**, izmantojot **FlightAPI.io**. Ja atrastie lidojumi atbilst maksimālajai cenai (piemēram, zem €200), Tu saņemsi automātisku **e-pasta paziņojumu ar lidojumu tabulu**.

---

## Funkcionalitāte

- Meklē vienvirziena lidojumus no Rīgas uz Milānas 3 lidostām:
  - Malpensa (MXP)
  - Bergamo (BGY)
  - Linate (LIN)
- Filtrē rezultātus pēc cenas (piemēram, zem €200)
- Sūta automātisku e-pastu ar lidojumu sarakstu
- Balstīts uz publisku API: [FlightAPI.io](https://flightapi.io)

---

## Kas nepieciešams

- Python 3.7+
- Gmail konts ar **App Password** (drošības nolūkos)
- FlightAPI.io konts ar API atslēgu

---

## Soli pa solim: kā uzstādīt

### 1. Instalē nepieciešamās Python bibliotēkas

pip install requests pandas

### 2. Iegūsti API atslēgu

Reģistrējies: https://flightapi.io

Nokopē API atslēgu

Ievieto kodā: 
- API_KEY = 'tava_api_atslēga'

### 3. Konfigurē e-pastu

Izmanto Gmail App Password: https://myaccount.google.com/apppasswords

Nodrošini, ka 2FA (divpakāpju autentifikācija) ir ieslēgta

Ievieto savus datus kodā:
- EMAIL = 'tavs_sūtāmais_epasts@gmail.com'
- EMAIL_USER = 'tavs_gmail_epasts@gmail.com'
- EMAIL_PASS = 'tavs_app_password_bez_atstarpēm'

### 4. Definē meklēšanas parametrus

- ORIGIN = 'RIX'
- DESTINATIONS = ['MXP', 'BGY', 'LIN']
- DEPART_DATE = '2025-07-15'
- MAX_PRICE = 200

#### Kā palaist skriptu?

python flight_scanner.py

#### Kā izskatās rezultāts?

| Destination Airport | Airline | Flight Number | Departure Time      | Arrival Time        | Price (EUR) |
| ------------------- | ------- | ------------- | ------------------- | ------------------- | ----------- |
| MXP                 | Ryanair | FR123         | 2025-07-15T10:30:00 | 2025-07-15T12:30:00 | 89          |
