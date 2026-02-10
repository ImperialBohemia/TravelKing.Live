import json
import os
from loguru import logger
from core.google.gemini import GeminiClient

class BlogEngine:
    """
    The SEO-optimized Blog Engine for Project FIRE (Luxury Edition).
    Updated for 2026 'Billboard Pro' Standards (Data-First, Executive Briefings).
    """
    def __init__(self, gemini: GeminiClient):
        self.gemini = gemini
        self.target_url = "https://villiers.ai/?id=11089"
        logger.info("Blog Engine: Ready to dominate search results.")

    def _get_2026_standards(self):
        """Loads the codifed Billboard Pro standards."""
        try:
            with open("knowledge/BLOGGING_2026.md", "r") as f:
                return f.read()
        except FileNotFoundError:
            logger.warning("BLOGGING_2026.md not found, using default fallback.")
            return "Standards: High quality, Data-First, Billboard Pro style."

    def generate_content_prompt(self, topic):
        """Generates the prompt for the AI, exposed for testing/verification."""
        standards = self._get_2026_standards()

        prompt = f"""
        You are a senior analyst for 'TravelKing Pro' (modeled after Billboard Pro / Variety Intelligence).
        Your audience is HNWIs, CEOs, and Industry Insiders. They care about DATA, YIELD, and EFFICIENCY.

        Generate a data-driven intelligence report (blog post) about: "{topic}".

        CRITICAL 'BILLBOARD PRO' STANDARDS:
        {standards}

        OUTPUT FORMAT (JSON ONLY):
        {{
            "title": "Data-Driven Headline (e.g., 'Private Jet Rates Up 12% in Q3')",
            "seo_keywords": "comma, separated, keywords",
            "html_content": "<article>...</article>"
        }}

        STRUCTURAL REQUIREMENTS:
        1. **Executive Briefing:** Start with a `div` class='executive-brief' containing 3 bullet points summarizing the trend, the cause, and the opportunity.
        2. **Data Hook:** The first paragraph MUST start with a hard statistic (invent a plausible 2026 projection if needed, e.g., "78% of trans-Atlantic flights...").
        3. **Chart Placeholders:** Insert at least 2 visual directives like `[INSERT CHART: Bar graph showing 5-year trend of {topic}]`.
        4. **"Why It Matters":** Include a section explicitly titled "Why It Matters" explaining the financial/strategic impact.
        5. **Field Intelligence:** A section sharing a "real-world" observation or case study, written in a professional, analyst tone.
        6. **Verdict:** End with a "Strategic Verdict" linking to Villiers Jets ({self.target_url}) as the solution.
        """
        return prompt

    def create_2026_blog_post(self, topic):
        """Generates an article specifically for CEOs and high-level entrepreneurs."""
        prompt = self.generate_content_prompt(topic)

        logger.info(f"Generating Billboard Pro report for topic: {topic}...")

        if not self.gemini:
             logger.warning("Gemini client not initialized. Returning fallback content.")
             return {
                 "title": f"Fallback Report: {topic}",
                 "html_content": "<p>AI Generation Unavailable.</p>",
                 "seo_keywords": "fallback"
             }

        response = self.gemini.generate_content(prompt)

        try:
            if response:
                cleaned_response = response.replace("```json", "").replace("```", "").strip()
                article_data = json.loads(cleaned_response)
                return article_data
            return {"error": "Empty response from Gemini"}
        except json.JSONDecodeError:
            logger.error("Failed to parse Gemini response as JSON. Returning raw text fallback.")
            return {
                "title": f"Market Analysis: {topic}",
                "seo_keywords": "aviation, data, intelligence",
                "html_content": f"<div class='executive-brief'><ul><li>Analysis Failed</li></ul></div><p>{response}</p>"
            }

    def generate_chart_data(self, topic):
        """Mock method to generate chart configuration for the frontend."""
        # In the future, this would use Gemini to generate Chart.js/Recharts JSON config.
        return {
            "type": "bar",
            "data": {"labels": ["2024", "2025", "2026"], "datasets": [{"data": [10, 15, 25]}]},
            "title": f"Growth Trend: {topic}"
        }

    def save_article(self, article):
        """Saves the article for deployment to the dashboard/cPanel."""
        filename = f"dashboard/blog_{article.get('title', 'untitled').replace(' ', '_').lower()}.json"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            json.dump(article, f, indent=4)
        logger.info(f"Article saved to {filename}")

if __name__ == "__main__":
    # Test execution
    pass
