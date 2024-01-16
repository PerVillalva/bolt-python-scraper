import httpx

def getRestaurantIds(apiUrl):
    response = httpx.get(apiUrl)

    data = response.json()

    # Get the list of providers (restaurants)
    providers = data['data']['providers']

    restaurantIds = [];
    restaurantRatings = []
    
    # Iterate over the list of restaurants and append the id of each one to the restaurantIds list
    for provider in providers:
        restaurantIds.append(provider['id'])
        rating = provider.get('rating')
        if rating is not None:
            restaurantRatings.append(rating.get('rating_value'))
        else:
            restaurantRatings.append(None)
    
    print(f'✅ Successfully obtained {len(restaurantIds)} restaurant Ids and ratings')
    return restaurantIds, restaurantRatings
