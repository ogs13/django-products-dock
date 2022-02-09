from datetime import datetime
from typing import Any, Optional
from datetime import datetime
from random import randint
from django.core.management.base import BaseCommand
from app.models import Product
from app.redis_service import set_redis_value

class Command(BaseCommand):
    help = '''set an arbitrary valid value of the price, 
    balance, status fields for the Product model'''

    def add_arguments(self, parser):
        pass        
    
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        
        min = 0
        max = 10000
        all_products = Product.objects.all()
        choices = self.get_product_choices()

        for product in all_products:
            
            stock_value = randint(0,len(choices)-1)
            
            product.price = randint(min, max)
            product.remains = randint(min, max)            
            product.status = choices[stock_value]
        
        _ = Product.objects.bulk_update(
                all_products, ['price','remains','status'], batch_size=999)
        
        set_redis_value('products_updated_at', str(datetime.now()))

        return self.stdout.write(self.style.SUCCESS('OK'))
    
    def get_product_choices(self) ->tuple():
        '''returns a tuple of the values 
        of the field model status Product'''
        
        choices = Product._meta.get_field('status').choices
        in_stok = choices[0][0]
        out_of_stok = choices[1][0]
        
        return (in_stok,out_of_stok)
