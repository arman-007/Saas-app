import stripe
from decouple import config

DJANGO_DEBUG=config("DJANGO_DEBUG", default=False, cast=bool)
STRIPE_SECRET_KEY=config("STRIPE_SECRET_KEY", default="", cast=str)

#check whether the stripe key is test key or production key
if "sk_test" in STRIPE_SECRET_KEY and not DJANGO_DEBUG:
    raise ValueError("Invalid STRIPE key for prod")



stripe.api_key = STRIPE_SECRET_KEY

def create_customer(name="", email="", raw=False):
    response = stripe.Customer.create(
        name=name,
        email=email,
    )
    if raw:
        return response
    stripe_id = response.id
    return stripe_id