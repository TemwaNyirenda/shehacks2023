import requests
import json

def retrieve_countries_dict():

    total_items = json.loads(requests.get('https://api-uct.mukuru.com/taurus/v1/resources/countries').text)['totalItems']
    # print(total_items)

    response_API = requests.get('https://api-uct.mukuru.com/taurus/v1/resources/countries?page_size=' + str(total_items))
    data = response_API.text
    all_countries_data = json.loads(data)['items']

    dict_countries_continents = {
        "A, B, C": [],
        "D, E, F": [],
        "G, H, I": [],
        "J, K, L": [],
        "M, N, O": [],
        "P, Q, R": [],
        "S, T, U": [],
        "V, W, X": [],
        "Y, Z"   : []
    }

    for country_data in all_countries_data:
        country = country_data['name']
        country_first_letter = country[0].upper()
        for key in dict_countries_continents.keys():
            if country_first_letter in key:
                dict_countries_continents[key].append(country)




    #     if continent in dict_countries_continents.keys():
    #         dict_countries_continents[continent].append(country)
    #     else:
    #         dict_countries_continents[continent] = []
    #         dict_countries_continents[continent].append(country)

    # for key in dict_countries_continents.keys():
    #     dict_countries_continents[key].sort()

    # for key in dict_countries_continents.keys():
    #     print(key + ": " + ", ".join(dict_countries_continents[key]))
    #     print(len(dict_countries_continents[key]))
    #     print()

    return dict_countries_continents


def get_country_data(country):
    total_items = json.loads(requests.get('https://api-uct.mukuru.com/taurus/v1/resources/countries').text)['totalItems']
    # print(total_items)

    response_API = requests.get('https://api-uct.mukuru.com/taurus/v1/resources/countries?page_size=' + str(total_items))
    data = response_API.text
    all_countries_data = json.loads(data)['items']

    for country_data in all_countries_data:
        if (country_data['name'] == country):
            return country_data
        

def get_country_code(country):
    total_items = json.loads(requests.get('https://api-uct.mukuru.com/taurus/v1/resources/countries').text)['totalItems']
    # print(total_items)

    response_API = requests.get('https://api-uct.mukuru.com/taurus/v1/resources/countries?page_size=' + str(total_items))
    data = response_API.text
    all_countries_data = json.loads(data)['items']

    for country_data in all_countries_data:
        if (country_data['name'] == country):
            return country_data['code']
        
def get_list_available_products(in_country, out_country):
    in_country_code = get_country_code(in_country)
    # print(in_country_code)
    out_country_code = get_country_code(out_country)
    # print(out_country_code)

    total_items = json.loads(requests.get('https://api-uct.mukuru.com/taurus/v1/products/price-check').text)['totalItems']
    # print(total_items)

    response_API = requests.get('https://api-uct.mukuru.com/taurus/v1/products/price-check?page_size=' + str(total_items))
    data = response_API.text
    all_products_data = json.loads(data)['items']

    available_products = []

    for products_data in all_products_data:
        if products_data['payInCountryCode'] == in_country_code and \
            products_data['payOutCountryCode'] == out_country_code:
            available_products.append(products_data['description'])

    # print(available_products)



if __name__ == "__main__":
    get_list_available_products("South Africa", "Zambia")