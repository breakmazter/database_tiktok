from TikTokApi import TikTokApi
from pprint import pprint

print = pprint

api = TikTokApi()

user = api.get_user(username="kom_sportswear")

print(user)
