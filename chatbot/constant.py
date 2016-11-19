import os

_access_token=os.environ["PAGE_ACCESS_TOKEN"]
_verify_token=os.environ["VERIFY_TOKEN"]
_my_env = "production" if os.environ["BOT_ENV"]=="production" else "development"