import time
import random
import logging
import functools
from googleapiclient.errors import HttpError

logger = logging.getLogger("OMEGA.Backoff")

def google_api_backoff(max_retries=5, initial_delay=1):
    """
    Implements Exponential Backoff for Google API calls.
    Handles 429 (Rate Limit) and 5xx (Server) errors.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            delay = initial_delay
            while retries <= max_retries:
                try:
                    return func(*args, **kwargs)
                except HttpError as e:
                    if e.resp.status in [429, 500, 502, 503, 504]:
                        if retries == max_retries:
                            logger.error(f"Max retries reached for {func.__name__}. Error: {e}")
                            raise

                        wait_time = delay + random.uniform(0, 1) # Jitter
                        logger.warning(f"Google API Error {e.resp.status}. Retrying in {wait_time:.2f}s... (Attempt {retries+1}/{max_retries})")
                        time.sleep(wait_time)
                        retries += 1
                        delay *= 2 # Exponential
                    else:
                        raise # Rethrow 400, 401, 403, 404 etc.
                except Exception as e:
                    logger.error(f"Unexpected error in {func.__name__}: {e}")
                    raise
            return None
        return wrapper
    return decorator
