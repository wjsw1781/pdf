import anvil.stripe
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import stripe
import datetime
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def create_alipay_payment(amount_usd=10):
    intent = stripe.PaymentIntent.create(
        amount=amount_usd,
        currency="usd",
        payment_method_types=["alipay"],
        description=f"Order {datetime.datetime.utcnow().isoformat()}",
        confirm=True,
        return_url="https://YOUR-APP-ID.anvil.app/#paid"   # 支付完成后支付宝会回跳
    )

    qr_blob      = intent.next_action["alipay_display_qr_code"]["data"]
    qr_hosted    = intent.next_action["alipay_display_qr_code"]["hosted_voucher_url"]
    
    return {
        "qr_url": qr_hosted,
        "voucher_png_b64": f"data:image/png;base64,{qr_blob}",
        "intent_id": intent.id,
    }

