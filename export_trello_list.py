import requests
import pandas as pd
api_key = 'ApiKey'
token = 'ApiToken'
board_id = 'board_id'
lists_url = f'https://api.trello.com/1/boards/{board_id}/lists'
lists_query = {
    'key': api_key,
    'token': token
}
try:
    lists_response = requests.get(lists_url, params=lists_query)
    lists_response.raise_for_status()
    lists = lists_response.json()
except requests.exceptions.RequestException as e:
    print(f"Error fetching lists from Trello: {e}")
    print(f"Response content: {lists_response.content}")
    exit(1)
except ValueError as e:
    print(f"Error parsing JSON response: {e}")
    print(f"Response content: {lists_response.content}")
    exit(1)
print("Listas disponíveis:")
for i, lst in enumerate(lists):
    print(f"{i + 1}. {lst['name']}")
list_choice = int(input("Digite o número da lista que deseja exportar: ")) - 1
if 0 <= list_choice < len(lists):
    list_id = lists[list_choice]['id']
    list_name = lists[list_choice]['name']
    url = f'https://api.trello.com/1/lists/{list_id}/cards'
    query = {
        'key': api_key,
        'token': token
    }
    try:
        response = requests.get(url, params=query)
        response.raise_for_status()
        cards = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching cards from Trello: {e}")
        print(f"Response content: {response.content}")
        exit(1)
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")
        print(f"Response content: {response.content}")
        exit(1)
    data = []
    for card in cards:
        card_data = {
            'Card Name': card['name'],
            'Description': card.get('desc', ''),
            'Due Date': card.get('due', ''),
            'Labels': ', '.join(label['name'] for label in card['labels'])
        }
        data.append(card_data)
    df = pd.DataFrame(data)
    df.to_excel(f'{list_name}_trello_list.xlsx', index=False)
    print(f"Dados exportados para {list_name}_trello_list.xlsx")
else:
    print("Escolha inválida. Por favor, tente novamente.")