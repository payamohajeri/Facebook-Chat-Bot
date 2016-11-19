import os

_my_env = "production" if "BOT_ENV" in os.environ and os.environ["BOT_ENV"]=="production" else "development"

if _my_env == "production":
    _access_token=os.environ["PAGE_ACCESS_TOKEN"]
    _verify_token=os.environ["VERIFY_TOKEN"]
else:
    _access_token=None
    _verify_token=None
