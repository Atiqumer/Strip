from flask import Blueprint, render_template, request, redirect, url_for 
import stripe 
from .config import Config  # type: ignore

main = Blueprint('main', __name__)

stripe.api_key = Config.STRIPE_SECRET_KEY

@main.route('/') 
def index(): 
    return render_template('index.html', stripe_public_key=Config.STRIPE_PUBLIC_KEY)

@main.route('/create-checkout-session', methods=['POST']) 
def create_checkout_session(): 
    try: 
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Flask Stripe Payment Example',
                    },
                    'unit_amount': 5000,  # Correct for $50.00
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=url_for('main.success', _external=True),
            cancel_url=url_for('main.cancel', _external=True),
        )

        # Debugging URLs
        print(f"Success URL: {url_for('main.success', _external=True)}")
        print(f"Cancel URL: {url_for('main.cancel', _external=True)}")

        return redirect(checkout_session.url, code=303) 
    except Exception as e:
        return str(e)
    
@main.route('/success') 
def success(): 
    return 'Payment was successful!' 

@main.route('/cancel') 
def cancel(): 
    return 'Payment was cancelled.'
