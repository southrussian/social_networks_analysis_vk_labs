import requests
import pandas as pd

access_token = 'vk1.a.HsuFagpssoZNlGtHR3lHV9ZKZ8z0M1qefv6SZ1fhBe3XJS83x6B8XpIxG7q-CwVcgu8iV0e2YlQpz3TVQfyolSiCrAaywcjRTtZKJ7Roqc6D5ZRouPPPILmvuFtdkAu0jOS81iM1ygB5VvubeyA1s8t3jJ0-wBGj0GlkiIvwSUvg2jTGx5NfbgRddv5lOir6Nrsmm-8ukqHZFK5Q1R7-AA'
user_id = '221066680'


def get_friends(user_id):
    url = 'https://api.vk.com/method/friends.get'
    params = {
        'user_id': user_id,
        'fields': 'bdate,city,education',
        'access_token': access_token,
        'v': '5.131'
    }
    response = requests.get(url, params=params)
    data = response.json()
    if 'response' in data:
        return data['response']['items']
    else:
        print('Error:', data)
        return []


friends_data = get_friends(user_id)

df_friends = pd.DataFrame(friends_data)

print(df_friends.head())
print(df_friends.columns)


if 'city' in df_friends.columns:
    df_friends['city_name'] = df_friends['city'].apply(lambda x: x['title'] if isinstance(x, dict) and 'title' in x else None)
    city_counts = df_friends['city_name'].dropna().value_counts()
    print("Распределение по городам:")
    print(city_counts)
else:
    print("Поле 'city' отсутствует в данных.")

if 'university_name' in df_friends.columns:
    university_counts = df_friends['university_name'].dropna().value_counts()
    print("Распределение по университетам:")
    print(university_counts)
else:
    print("Поле 'university_name' отсутствует в данных.")


if 'bdate' in df_friends.columns:
    df_friends['bdate'] = pd.to_datetime(df_friends['bdate'], errors='coerce', format='%d.%m.%Y')
    df_friends['birth_year'] = df_friends['bdate'].dt.year
    birth_year_counts = df_friends['birth_year'].dropna().astype(int).value_counts()
    print("Распределение по годам рождения:")
    print(birth_year_counts)
else:
    print("Поле 'bdate' отсутствует в данных.")
