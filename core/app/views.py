import time
from datetime import datetime
from typing import Any, Dict
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Category, Product
from .redis_service import get_redis_value

class ProductsListView(ListView):
    
    model = Product
    paginate_by = 50
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        context['selected_category'] = self.category

        if not cache.get('page_obj', None) or self.cache_is_not_valid(context):
            
            seconds = 300
            
            cache.set('page_obj', context['page_obj'], seconds)
            
            time.sleep(2)
            
            session = self.request.session
            
            session['page_readed_at'] = str(datetime.now())

        return context
    
    
    def get_queryset(self):
        
        pk = self.kwargs.get('pk',0)
        
        self.category = get_object_or_404(Category, pk = pk)        
        
        return Product.objects.filter(category = self.category)
    
    def cache_is_not_valid(self, context:Dict[str,Any]) -> bool:
        '''
        
        '''
        session = self.request.session

        products_updated_at_str = get_redis_value('products_updated_at')
        
        page_readed_at_str = session.get('page_readed_at', str(datetime.now()))

        if products_updated_at_str:
            
            products_updated_at = datetime.fromisoformat(products_updated_at_str)
            
            page_readed_at = datetime.fromisoformat(page_readed_at_str)

            return products_updated_at > page_readed_at
        
        return False


class CategoryListView(ListView):

    model = Category
    paginate_by = 50
