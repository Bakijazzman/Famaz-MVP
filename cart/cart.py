class Cart():
    def __init__(self,request):
        self.session = request.session
        # Get previous session key
        cart = self.session.get('session_key')
        if "session_key" not in request.session:
            cart = self.session['session_key'] = {}
        
    # Make sure cart is available on all pages on the site
        self.cart = cart
    