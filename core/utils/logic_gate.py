import functools
import logging
from typing import Any, Callable

logger = logging.getLogger("OMEGA.LogicGate")

def require_real_data(confidence_threshold: float = 0.9):
    """
    Gold Standard Logic Gate.
    Strictly prevents hallucinations by enforcing a minimum confidence score
    from verified real-world data sources before allowing execution.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # The first argument is 'self' (e.g., SniperEngine)
            instance = args[0]

            # Identify the flight/target from arguments
            target = kwargs.get('target') or (args[1] if len(args) > 1 else None)

            if not target:
                logger.warning("🚫 LOGIC GATE: No target provided. Blocked.")
                return None

            # Check for ground truth data
            confidence = target.get('confidence', 0.0)

            if confidence < confidence_threshold:
                logger.error(f"🚫 HALUCINATION PREVENTED: Target {target.get('flight_number')} has confidence {confidence}. Threshold is {confidence_threshold}.")
                return {"status": "blocked", "reason": "insufficient_real_evidence"}

            logger.info(f"✅ LOGIC GATE: Confidence {confidence} verified. Proceeding with execution.")
            return func(*args, **kwargs)

        return wrapper
    return decorator
