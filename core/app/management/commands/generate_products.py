from typing import Any, Optional, List
from django.core.management.base import BaseCommand
from app.models import Category, Product

class Command(BaseCommand):
    help = '''generates categories and products,
    takes 2 positional arguments,
    the first is the number of categories,
    the second is the number of products in the category'''

    def add_arguments(self, parser):
        
        parser.add_argument(nargs = '+', type = int, dest = 'args')
    
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        
        categories_num = 0
        products_num = 0
        
        if len(args):
            
            categories_num = args[0]
            
            if len(args) > 1:
            
                products_num = args[1]

        if not categories_num: 
            
            msg = 'the number of categories is not set'
            
            return self.stdout.write(self.style.SUCCESS(msg))
        
        if not products_num:
            
            msg = 'the number of products is not set'
            
            return self.stdout.write(self.style.SUCCESS(msg))
        
        category_objects = self.create_categories(categories_num)

        self.create_products(products_num, category_objects)      
        
        return self.stdout.write(self.style.SUCCESS('OK'))


    def create_categories(self, categories_num:int) -> List[Category]:
        '''creates category list'''
        category_list = [Category(name=f'cagetory_{c}',pk = c) 
                            for c in range(categories_num)]

        return Category.objects.bulk_create(category_list)
    

    def create_products(
            self,products_num:int,category_objects:List[Product]) -> None:
        '''creates products by category'''
        pk = 0
        product_list = []
        default_choice = Product._meta.get_field('status').choices[1][0]
        
        for category in category_objects:
            for _ in range(products_num):
                product = Product(
                    name = f'product_{pk}',
                    category = category,
                    status = default_choice,
                    pk = pk)
                    
                product_list.append(product)
                pk += 1
        
        _ = Product.objects.bulk_create(product_list)
