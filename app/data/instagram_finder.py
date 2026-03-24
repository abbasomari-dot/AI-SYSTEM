import requests
import re


class InstagramFinder:

    def __init__(self, api_key):
        self.api_key = api_key

    # ✅ اسم واضح وثابت
    def get_instagram_data(self, query):

        url = "https://serpapi.com/search.json"

        params = {
            "engine": "google",
            "q": f"{query} instagram",
            "api_key": self.api_key
        }

        response = requests.get(url, params=params)
        data = response.json()

        results = data.get("organic_results", [])

        for r in results:
            link = r.get("link", "")
            snippet = r.get("snippet", "")

            if "instagram.com" in link:

                followers = self._extract_followers(snippet)

                return {
                    "link": link,
                    "followers": followers,
                    "source": "serpapi"
                }

        return {
            "link": None,
            "followers": None,
            "source": None
        }

    # 🔒 private method
    def _extract_followers(self, text):

        if not text:
            return None

        match = re.search(r"([\d,.]+)\s*(K|M)?\s*followers", text, re.IGNORECASE)

        if match:
            number = match.group(1).replace(",", "")
            suffix = match.group(2)

            num = float(number)

            if suffix == "K":
                num *= 1000
            elif suffix == "M":
                num *= 1000000

            return int(num)

        return None