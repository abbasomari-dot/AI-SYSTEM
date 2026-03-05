import requests
from bs4 import BeautifulSoup
from app.intelligence.instagram_finder import InstagramFinder


class InstagramAnalyzer:

    def __init__(self):
        self.finder = InstagramFinder()

    def _extract_numbers(self, text):

        text = text.replace(",", "").lower()

        if "k" in text:
            return int(float(text.replace("k", "")) * 1000)

        if "m" in text:
            return int(float(text.replace("m", "")) * 1000000)

        try:
            return int(text)
        except:
            return 0

    def _scrape_instagram(self, url):

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        try:

            r = requests.get(url, headers=headers)

            soup = BeautifulSoup(r.text, "html.parser")

            spans = soup.find_all("span")

            followers = 0
            posts = 0

            for s in spans:

                text = s.text.lower()

                if "followers" in text:
                    number = text.split(" ")[0]
                    followers = self._extract_numbers(number)

                if "posts" in text:
                    number = text.split(" ")[0]
                    posts = self._extract_numbers(number)

            return followers, posts

        except:
            return 0, 0

    def _estimate_engagement(self, followers, posts):

        # تقدير بسيط للتفاعل

        if followers == 0:
            return 0

        estimated_likes = followers * 0.02
        estimated_comments = followers * 0.002

        engagement_rate = (estimated_likes + estimated_comments) / followers

        return round(engagement_rate * 100, 2)

    def analyze(self, restaurant_name):

        instagram_url = self.finder.find(restaurant_name)

        followers = 0
        posts = 0

        if instagram_url:
            followers, posts = self._scrape_instagram(instagram_url)

        engagement_rate = self._estimate_engagement(followers, posts)

        score = 0

        if followers < 2000:
            score += 2

        if posts < 100:
            score += 1

        if engagement_rate < 2:
            score += 2

        return {
            "instagram_url": instagram_url,
            "followers": followers,
            "posts": posts,
            "engagement_rate": engagement_rate,
            "instagram_score": score
        }