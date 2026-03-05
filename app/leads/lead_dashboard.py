import csv
import os


class LeadDashboard:

    def save(self, leads):

        os.makedirs("leads", exist_ok=True)

        path = "leads/leads_dashboard.csv"

        with open(path, "w", newline="", encoding="utf-8") as f:

            writer = csv.writer(f)

            writer.writerow([
                "Restaurant",
                "Rating",
                "Reviews",
                "Followers",
                "Posts",
                "EngagementRate",
                "LeadScore",
                "Instagram"
            ])

            for lead in leads:

                writer.writerow([
                    lead["name"],
                    lead["rating"],
                    lead["reviews"],
                    lead["followers"],
                    lead["posts"],
                    lead["engagement_rate"],
                    lead["lead_score"],
                    lead["instagram_url"]
                ])

        return path