from core.models import Product, Profile

class Cart():
    def __init__(self, request):
        self.session = request.session
        # get request
        self.request = request
        # Get previous session key
        cart = self.session.get('session_key')
        if "session_key" not in request.session:
            cart = self.session['session_key'] = {}
        
    # Make sure cart is available on all pages on the site
        self.cart = cart
    
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)
            
        self.session.modified = True
        
        # Cart persistence Build
        if self.request.user.is_authenticated:
            # get the current user
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            # save to database
            current_user.update(old_cart=str(carty))
    
    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)
            
        self.session.modified = True
        
        # Cart persistence Build
        if self.request.user.is_authenticated:
            # get the current user
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            # save to database
            current_user.update(old_cart=str(carty))
     
    def __len__(self):
        return len(self.cart)
    
    def get_prod(self):
        product_id = self.cart.keys()
        products = Product.objects.filter(id__in=product_id)
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities    
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        ourcart = self.cart
        ourcart[product_id] = product_qty
        self.session.modified = True
        if self.request.user.is_authenticated:
            # get the current user
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            # save to database
            current_user.update(old_cart=str(carty)) 
        final = self.cart
        return final
    
    def delete(self, product):
        product_id = str(product)
        #delete frm cart
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True
        
        if self.request.user.is_authenticated:
            # get the current user
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            # save to database
            current_user.update(old_cart=str(carty))
        
    def cart_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quant = self.cart
        total = 0
        for key, value in quant.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total += (product.sale_price * value)
                    else:
                        total += (product.price * value)
        return total        
        