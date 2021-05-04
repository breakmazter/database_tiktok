from TikTokApi import TikTokApi

api = TikTokApi()

results = 10

trending = api.get_user(username="kom_sportswear")

for tiktok in trending:
    print(tiktok)




