import json
import os
from loguru import logger
from core.maintenance.git_sync import GitSync

class KnowledgeManager:
    """Manages persistent wisdom and knowledge synchronization."""
    def __init__(self, storage_path="data/brain/wisdom.json", root="/home/q/TravelKing.Live"):
        self.storage_path = storage_path
        self.root = root
        self.git = GitSync(root=self.root)
        self._ensure_storage()

    def _ensure_storage(self):
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        if not os.path.exists(self.storage_path):
            with open(self.storage_path, 'w') as f:
                json.dump({"wisdom": [], "last_update": 0}, f)

    def record_finding(self, topic, data, push=True):
        """Records a new finding and optionally pushes to Git immediately."""
        import time
        try:
            with open(self.storage_path, 'r') as f:
                kb = json.load(f)
            
            entry = {
                "timestamp": time.time(),
                "topic": topic,
                "data": data
            }
            kb["wisdom"].append(entry)
            kb["last_update"] = time.time()
            
            with open(self.storage_path, 'w') as f:
                json.dump(kb, f, indent=4)
            
            logger.info(f"🧠 Knowledge Recorded: {topic}")
            
            if push:
                self.git.sync(f"📝 Knowledge Update: {topic}")
            return True
        except Exception as e:
            logger.error(f"Failed to record knowledge: {e}")
            return False

    def get_all_wisdom(self):
        """Returns all recorded knowledge."""
        try:
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        except Exception:
            return {"wisdom": []}
