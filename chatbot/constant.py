import os

_my_env = "production" if "BOT_ENV" in os.environ and os.environ["BOT_ENV"]=="production" else "development"

if _my_env == "production":
    _access_token=os.environ["PAGE_ACCESS_TOKEN"]
    _verify_token=os.environ["VERIFY_TOKEN"]
    _db_link=os.environ.get("REDIS_URL")
else:
    _access_token=None
    _verify_token=None
    _db_link="localhost:6379"

_fb_url="https://graph.facebook.com/v2.6/me/messages"
_fb_userinfo_url="https://graph.facebook.com/v2.6/"
_response_content_type="application/json"