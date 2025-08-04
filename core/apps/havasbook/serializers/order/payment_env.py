from config.env import env
from payme import Payme
from click_up import ClickUp

PAYME_ID = env.str("PAYME_ID")
PAYME_KEY = env.str("PAYME_KEY")
BOT_TOKEN = env.str("BOT_TOKEN")


payme = Payme(
    payme_id=PAYME_ID,
    payme_key=PAYME_KEY
)

click_up = ClickUp(service_id=env("CLICK_SERVICE_ID"), merchant_id=env("CLICK_MERCHANT_ID"))

