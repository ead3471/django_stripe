# Django + Stripe API testing project 

The goal of the project is to demonstrate how to integrate Django-based server with the Stripe web service.
## Installation
1. install python 3.8
2. run "git clone git@github.com:ead3471/django_stripe.git"
3. cd django_stripe
4. run "python3.8 -m venv venv
5. for windows run
        source venv/Scripts/activate
   for Linux and macOS:
        source venv/bin/activate
6. run pip install -m requirements.txt
7.cd stripe_server 
8. python3 manage.py migrate
9. python3 manage.py runserver
10. navigate to http://127.0.0.1:8000/

## Server urls:
- "/"  - the index page. Shows all registered items
- "/item/<item_id>" - detailed item info page with "buy" button
- "/buy/<item_id>" - endpoint create Stripe buy selected item session and return json: {'id': <stripe session id>}
- "/orders/<order_id>": shows all registered orders
- "/orders/<order_id>": shows order info
- "/orders/<order_id>/buy": endpoint creates Stripe buy selected order session and return json: {'id': <stripe session id>}
