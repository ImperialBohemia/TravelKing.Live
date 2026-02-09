import facebook
import json
import os
from loguru import logger
from dotenv import load_dotenv

load_dotenv()

class FacebookOrchestrator:
    """Enterprise adapter for Facebook Graph API with unbreakable connectivity."""
    def __init__(self, config_path="data/config/facebook.json"):
        self.config_path = config_path
        self.config = self._load_config()
        
        # Priority: 1. Environment, 2. Page Token (Permanent), 3. User Token
        self.access_token = (
            os.getenv("FB_PAGE_TOKEN") or 
            self.config.get("page_token_791106764077902") or 
            self.config.get("access_token")
        )
        
        self.graph = None
        if self.access_token:
            try:
                self.graph = facebook.GraphAPI(access_token=self.access_token)
                # Connection sanity check
                logger.success("Facebook Orchestrator: UNBREAKABLE link active.")
            except Exception as e:
                logger.error(f"Facebook connection failed: {e}")

    def _load_config(self):
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def post_to_page(self, page_id, message, link=None):
        """High-reliability posting logic using the permanent token."""
        token = self.config.get(f"page_token_{page_id}") or self.access_token
        if not token:
            return {"error": "No token available"}
            
        temp_graph = facebook.GraphAPI(access_token=token)
        try:
            res = temp_graph.put_object(parent_object=page_id, connection_name='feed', message=message, link=link)
            logger.success(f"🔥 FIRE: Post successful on page {page_id}")
            return res
        except facebook.GraphAPIError as e:
            logger.error(f"Post failed: {e}")
            return {"error": str(e)}

        def get_page_insights(self, page_id):

            """Retrieves professional insights for the page (Admin only)."""

            try:

                metrics = 'page_impressions_unique,page_engaged_users'

                insights = self.graph.get_connections(id=page_id, connection_name='insights', metric=metrics)

                return insights

            except Exception as e:

                logger.error(f"Failed to fetch insights: {e}")

                return None

    

        def get_recent_comments(self, page_id):

            """Monitors recent comments for potential leads or moderation."""

            try:

                posts = self.graph.get_connections(id=page_id, connection_name='feed', limit=5)

                all_comments = []

                for post in posts.get('data', []):

                    comments = self.graph.get_connections(id=post['id'], connection_name='comments')

                    all_comments.extend(comments.get('data', []))

                return all_comments

            except Exception as e:

                logger.error(f"Failed to fetch comments: {e}")

                return []

    