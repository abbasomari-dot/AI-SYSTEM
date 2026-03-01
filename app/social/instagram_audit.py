from typing import Dict, Optional
import re
import requests


class InstagramAudit:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }

    def _extract_username(self, instagram_url: str) -> Optional[str]:
        if not instagram_url:
            return None

        pattern = r"instagram\.com/([A-Za-z0-9_.]+)"
        match = re.search(pattern, instagram_url)

        if match:
            return match.group(1)

        return None

    def _fetch_public_page(self, username: str) -> Optional[str]:
        try:
            url = f"https://www.instagram.com/{username}/"
            response = requests.get(url, headers=self.headers, timeout=5)

            if response.status_code == 200:
                return response.text

            return None

        except Exception:
            return None

    def _is_private(self, html: str) -> bool:
        return "This account is private" in html

    def _has_link_hint(self, html: str) -> bool:
        return "http://" in html or "https://" in html

    def analyze(self, instagram_url: str) -> Dict:
        username = self._extract_username(instagram_url)

        html = None
        is_private = None
        has_link = None
        presence_score = 0

        if username:
            html = self._fetch_public_page(username)

        if html:
            presence_score += 40
            is_private = self._is_private(html)
            has_link = self._has_link_hint(html)

            if not is_private:
                presence_score += 30

            if has_link:
                presence_score += 30

        return {
            "username": username,
            "account_exists": True if html else False,
            "is_private": is_private,
            "has_link_hint": has_link,
            "snapshot_score": presence_score,
        }