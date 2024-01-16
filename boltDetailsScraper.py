from playwright.sync_api import Page

def getRestaurantData(page: Page, id: str, rating: str):
    MAX_RETRIES = 3  # Maximum number of retries
    TIMEOUT = 60000  # Timeout for page.goto (in milliseconds)

    for attempt in range(MAX_RETRIES):
        try:
            # Navigate to the target webpage
            url = f"https://food.bolt.eu/en-US/581-split/p/{id}"
            page.goto(url, timeout=TIMEOUT)

            # Wait for the contact_info_modal to be clickable and click it
            contact_info_modal = page.wait_for_selector('div[role="presentation"]:last-child')
            contact_info_modal.click()

            # Wait for the restaurantNameEl to appear
            restaurantNameEl = page.wait_for_selector('#provider-info-modal span')
            restaurantAddressEl = page.query_selector('div.flex-1:nth-child(2) > span:nth-child(1)')
            restaurantContactNumberEl = page.query_selector('div.flex-1:nth-child(2) > a:nth-child(3)')

            restaurantData = {
                "name": restaurantNameEl.text_content(),
                "address": restaurantAddressEl.text_content(),
                "phone": restaurantContactNumberEl.text_content(),
                "rating": rating,
                "reviews": None
            }
            print(f'🤖 Extracted information from {restaurantData["name"]}')
            return restaurantData

        except Exception as e:
            if attempt < MAX_RETRIES - 1:  # i.e. not the last attempt
                print(f"Error processing restaurant ID {id}: {e}. Retrying...")
                continue
            else:
                print(f"Error processing restaurant ID {id}: {e}. No more retries.")
                raise  # Re-raise the last exception

        finally:
            pass