import json
import os
from loguru import logger
from core.google.gemini import GeminiClient

class BlogEngine:
    """
    The SEO-optimized Blog Engine for Project FIRE (Luxury Edition).
    Updated for 2026 Blogging Standards (E-E-A-T, AIEO).
    """
    def __init__(self, gemini: GeminiClient):
        self.gemini = gemini
        self.target_url = "https://villiers.ai/?id=11089"
        logger.info("Blog Engine: Ready to dominate search results.")

    def _get_2026_standards(self):
        """Loads the codifed blogging standards."""
        try:
            with open("knowledge/BLOGGING_2026.md", "r") as f:
                return f.read()
        except FileNotFoundError:
            logger.warning("BLOGGING_2026.md not found, using default fallback.")
            return "Standards: High quality, E-E-A-T, AI-friendly structure."

    def create_2026_blog_post(self, topic):
        """Generates an article specifically for CEOs and high-level entrepreneurs."""
        standards = self._get_2026_standards()

        prompt = f"""
        You are an elite travel journalist writing for a high-net-worth audience.
        Generate a comprehensive, SEO-optimized blog post about: "{topic}".

        CRITICAL 2026 STANDARDS TO FOLLOW:
        {standards}

        OUTPUT FORMAT (JSON ONLY):
        {{
            "title": "Engaging Headline (under 60 chars)",
            "seo_keywords": "comma, separated, keywords",
            "html_content": "<article>...</article>" (Use semantic HTML, H2/H3, bullet points, and placehoder images)
        }}
        
        Specific Content Requirements:
        - Include a 'Key Takeaways' box at the start.
        - Include a personal anecdote relevant to the topic.
        - Include at least one data point or expert citation.
        - Use short paragraphs (max 3 sentences).
        - End with a strong CTA to book via Villiers Jets ({self.target_url}).
        """

        logger.info(f"Generating CEO article for topic: {topic}...")

        # In degraded mode or testing, gemini might be None
        if not self.gemini:
             logger.warning("Gemini client not initialized. Returning fallback content.")
             return {
                 "title": f"Fallback Article: {topic}",
                 "html_content": "<p>AI Generation Unavailable.</p>",
                 "seo_keywords": "fallback"
             }

        response = self.gemini.generate_content(prompt)

        try:
            # Clean up potential markdown code blocks from Gemini response
            if response:
                cleaned_response = response.replace("```json", "").replace("```", "").strip()
                article_data = json.loads(cleaned_response)
                return article_data
            return {"error": "Empty response from Gemini"}
        except json.JSONDecodeError:
            logger.error("Failed to parse Gemini response as JSON. Returning raw text fallback.")
            return {
                "title": f"The CEO's Guide to {topic}",
                "seo_keywords": "aviation, luxury, travel",
                "html_content": f"<p>{response}</p>"
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
