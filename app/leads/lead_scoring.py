class LeadScoring:

    def score(self, restaurant):

        score = 0

        if restaurant["rating"] < 4.6:
            score += 2

        if restaurant["reviews"] < 2000:
            score += 2

        if restaurant["reviews"] < 500:
            score += 1

        return score