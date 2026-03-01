class StrongTargetingStrategy:
    """
    Strong Market Targeting Strategy
    - Rating >= 4.2
    - Reviews between 100 and 1200
    - Closer to 100 = higher opportunity
    """

    def __init__(self):
        self.min_rating = 4.2
        self.min_reviews = 100
        self.max_reviews = 1200

    def calculate(self, rating: float, reviews: int) -> float:
        if rating is None or reviews is None:
            return 0

        if rating < self.min_rating:
            return 0

        if reviews < self.min_reviews or reviews > self.max_reviews:
            return 0

        range_size = self.max_reviews - self.min_reviews
        position = (reviews - self.min_reviews) / range_size
        visibility_factor = 1 - position

        rating_factor = (rating - self.min_rating) / (5 - self.min_rating)

        opportunity = ((visibility_factor * 0.7) + (rating_factor * 0.3)) * 100

        return round(opportunity, 2)