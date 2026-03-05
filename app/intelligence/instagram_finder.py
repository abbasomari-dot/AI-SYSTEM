import requests
from bs4 import BeautifulSoup


class InstagramFinder:

    def find(self, restaurant_name):

        query = f"{restaurant_name} instagram"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        url = "https://www.google.com/search"

        params = {
            "q": query
        }

        try:

            response = requests.get(url, headers=headers, params=params)

            soup = BeautifulSoup(response.text, "html.parser")

            links = soup.find_all("a")

            for link in links:

                href = link.get("href")

                if not href:
                    continue

                if "instagram.com" in href:

                    href = href.replace("/url?q=", "")

                    if "&" in href:
                        href = href.split("&")[0]

                    if "instagram.com/p/" in href:
                        continue

                    if "instagram.com/reel/" in href:
                        continue

                    return href

        except:
            pass

        return None