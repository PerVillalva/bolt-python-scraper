from playwright.sync_api import sync_playwright
from boltDetailsScraper import getRestaurantData
from boltRestaurants import getRestaurantIds
import json

url = "https://deliveryuser.live.boltsvc.net/eaterWeb/providersIdentifiers/byCityId?city_id=581&version=FW.0.17.10&deviceId=e2ca5c08-61f3-4b8e-8a23-3796ac70c3be&deviceType=web&device_name=UNKNOWN&device_os_version=Google+Inc.&language=en-US"

restaurantIdsList = getRestaurantIds(url)

restaurantsData = []

with sync_playwright() as p:
    browser = p.firefox.launch(headless=True)  # Launch a headless browser
    page = browser.new_page()  # Open a new page

    for id, rating in zip(restaurantIdsList[0], restaurantIdsList[1]):
        try:
            restaurantsData.append(getRestaurantData(page, id, rating))
        except Exception as e:
            print(f"Error processing restaurant ID {id}: {e}")

    # Close the browser
    browser.close()

print(f'Obtained data from {len(restaurantsData)} restaurants')


def write_data_to_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)
        
write_data_to_json("bolt_restaurants_data", restaurantsData)