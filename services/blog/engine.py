import json
from loguru import logger

class BlogEngine:
    """The SEO-optimized Blog Engine for Project FIRE (Luxury Edition)."""
    def __init__(self):
        self.target_url = "https://villiers.ai/?id=11089"
        logger.info("Blog Engine: Ready to dominate search results.")

    def create_ceo_article(self, topic):
        """Generates an article specifically for CEOs and high-level entrepreneurs."""
        hero_img = "https://images.unsplash.com/photo-1540962351504-03099e0a754b?auto=format&fit=crop&w=1200&q=80"
        
        article = {
            "title": f"The CEO's Guide to Aviation Efficiency: {topic}",
            "seo_keywords": "business jet charter, corporate efficiency, private aviation ROI, Villiers AI for CEOs",
            "html_content": f"""
            <article class="ceo-post" style="font-family: 'Helvetica', sans-serif; color: #333;">
                <img src="{hero_img}" alt="Business Aviation" style="width:100%; border-radius:0;">
                <h1 style="font-size: 2.5rem; border-bottom: 2px solid #000; padding-bottom: 10px;">The Strategic Advantage of Private Aviation</h1>
                <p class="lead" style="font-size: 1.4rem; font-style: italic;">For the modern executive, travel is not a cost—it is an investment in time.</p>
                
                <section style="margin: 40px 0;">
                    <h3>Maximizing Your Hourly Rate</h3>
                    <p>When your presence is required across continents in a single day, commercial hubs become bottlenecks. Villiers AI allows you to regain control of your schedule, offering non-stop flights to over 40,000 locations.</p>
                </section>

                <div style="background: #f4f4f4; padding: 40px; border-radius: 10px;">
                    <h4>Why Industry Leaders Choose Villiers:</h4>
                    <p>Real-time availability, absolute privacy, and the ability to conduct board meetings at 40,000 feet. The Villiers network is the ultimate tool for corporate scaling.</p>
                    <a href="{self.target_url}" style="display:inline-block; background: #000; color: #fff; padding: 20px 40px; text-decoration: none; font-weight: bold;">Access the Villiers Network</a>
                </div>
            </article>
            """
        }
        return article

    def save_article(self, article):
        """Saves the article for deployment to the dashboard/cPanel."""
        filename = f"dashboard/blog_{article['title'].replace(' ', '_').lower()}.json"
        with open(filename, "w") as f:
            json.dump(article, f, indent=4)
        logger.info(f"Article saved to {filename}")