import requests
import pandas as pd
import smtplib
from email.message import EmailMessage

API_KEY = 'tava_api_atslēga'
EMAIL = 'tavs_sūtāmais_epasts@gmail.com'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465

EMAIL_USER = 'tavs_gmail_epasts@gmail.com'
EMAIL_PASS = 'tavs_app_password_bez_atstarpēm'

ORIGIN = 'RIX'
DESTINATIONS = ['MXP', 'BGY', 'LIN']
DEPART_DATE = '2025-07-15'
MAX_PRICE = 200

def search_flights(origin, destination, date):
    url = f"https://flightapi.io/api/v1/flights/search?key={API_KEY}&origin={origin}&destination={destination}&date={date}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"No flights for {destination}.")
        return []

    data = response.json().get('data', [])
    flights = []
    for f in data:
        try:
            price = float(f.get('price', 9999))
            if price <= MAX_PRICE:
                flights.append({
                    'Destination Airport': destination,
                    'Airline': f.get('airline', 'N/A'),
                    'Flight Number': f.get('flight_number', 'N/A'),
                    'Departure Time': f.get('departure_time', 'N/A'),
                    'Arrival Time': f.get('arrival_time', 'N/A'),
                    'Price (EUR)': price
                })
        except:
            continue

    return flights


def send_email(df):
    msg = EmailMessage()
    msg['Subject'] = 'Flight Deals: Riga → Milan (Filtered)'
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL
    msg.set_content('Flight deals found:\n' + df.to_string(index=False))
    msg.add_alternative(f"""\
    <!DOCTYPE html>
    <html>
        <body>
            <h2>Riga → Milan Flight Deals (Under €{MAX_PRICE})</h2>
            {df.to_html(index=False)}
        </body>
    </html>
    """, subtype='html')

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
         smtp.login(EMAIL_USER, EMAIL_PASS)
         smtp.send_message(msg)


def main():
    all_flights = []

    for destination in DESTINATIONS:
        print(f"Searching RIX → {destination}...")
        outbound = search_flights(ORIGIN, destination, DEPART_DATE)
        all_flights.extend(outbound)

    if not all_flights:
        print("No flights found under that price.")
        return

    df = pd.DataFrame(all_flights)
    send_email(df)
    print("Email sent with flights.")


if __name__ == "__main__":
    main()