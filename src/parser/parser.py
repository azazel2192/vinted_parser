import requests
from src.parser import filemanager, constants


class Parser:
    def __init__(self):
        self.filters = {
            'positive_feedback': None,
            'negative_feedback': None,
            'neutral_feedback': None,
            'country': None,
            'items_count': None,
            'promoted': None,
            'first_page': None,
            'last_page': None
        }
        self.set_filters()
        self.url = \
            f"https://www.vinted.cz/api/v2/catalog/items?page={self.filters['first_page']}&catalog_ids=1904&per_page=" \
            f"{self.filters['last_page']}"

    def set_filters(self):
        print('Set the filters for parsing')
        for i in self.filters:
            if i == 'country':
                print('Hint: Czech Republic - 3, Poland - 15, Slovakia - 22')
            elif i == 'promoted':
                print('Hint: enter "True" or "False"')
            print(f'Set the {i} value: ')
            if i == 'promoted':
                self.filters[i] = bool(input())
            else:
                self.filters[i] = int(input())

    def parse_items(self):
        s = requests.session()
        null_items = []
        cookies_manage = filemanager.FileManager('cookie')
        sellers_manage = filemanager.FileManager('sellers')
        sellers_manage.load()

        s.cookies.set('_vinted_fr_session', domain='.www.vinted.cz', value=cookies_manage.load())
        s.headers.update(constants.headers)
        items_json_list = s.get(self.url).json()['items']

        for d in items_json_list:
            user_url = f"https://www.vinted.cz/api/v2/users/{d['user']['id']}/"
            profile_json_list = s.get(user_url).json()['user']

            if profile_json_list['positive_feedback_count'] <= self.filters['positive_feedback'] and \
                    profile_json_list['negative_feedback_count'] <= self.filters['negative_feedback'] \
                    and profile_json_list['neutral_feedback_count'] <= self.filters['negative_feedback'] and \
                    d['id'] not in sellers_manage.sellers and profile_json_list['country_id'] == self.filters['country']\
                    and profile_json_list['total_items_count'] <= self.filters['items_count'] and \
                    d['promoted'] is not self.filters['promoted']:
                print(d)
                null_items.append(d['url'])
                sellers_manage.sellers.append(profile_json_list['id'])

        cookies_manage.save(file_value=s.cookies.get('_vinted_fr_session'))
        sellers_manage.save()
        s.close()
        print(null_items)


x = Parser()
x.parse_items()
