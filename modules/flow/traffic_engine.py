import os
from loguru import logger
from ai.logic.brain import Brain
from core.security.validator import Validator
from services.content.video_maker import VideoMaker

class TrafficEngine:
    """
    Automated Content-to-Traffic Pipeline.
    Generates viral assets (Video/Text/Image) from a single product link.
    """

    def __init__(self):
        self.brain = Brain()
        self.video_maker = VideoMaker()
        self.output_dir = "data/assets/generated"
        os.makedirs(self.output_dir, exist_ok=True)

    def ignite(self, product_url, affiliate_link):
        """Starts the full production cycle."""
        logger.info(f"🔥 Igniting Traffic Engine for: {product_url}")

        # 1. BRAIN: Analyze & Script
        strategy = self._strategize(product_url)
        if not strategy:
            return
        
        # 2. FACTORY: Create Assets
        logger.info("🏭 Starting Asset Factory...")
        
        # Generate Video
        if strategy and 'video_script' in strategy:
            # Note: generate_google_flow_video is used for Google Flow (Nano Banana)
            video_path = self.video_maker.generate_google_flow_video(strategy['video_script'])
            strategy['generated_video'] = video_path
        
        # 3. REPORT
        logger.success(f"✅ Traffic Assets Ready in {self.output_dir}")
        return strategy

    def _strategize(self, url):
        """Uses Gemini to create the viral angle."""
        prompt = f"""
        Analyze this product: {url}
        Create a viral marketing strategy for YouTube Shorts and Google Discover.
        OUTPUT JSON:
        {{
          "hook": "Shocking first sentence",
          "video_script": "Full 15s script",
          "blog_title": "Clickbait title for Discover",
          "pain_point": "Core problem solved"
        }}
        """
        
        raw_plan = self.brain.think(prompt)
        valid, plan = Validator.validate_json_output(raw_plan)
        
        if valid:
            logger.info(f"🧠 Strategy Generated: {plan.get('hook')}")
            return plan
        else:
            logger.error("❌ Brain failed to generate strategy.")
            return None

if __name__ == "__main__":
    engine = TrafficEngine()
    # Test run (simulated)
    engine.ignite("https://example.com/smart-watch", "https://affiliate.com/ref123")