from .import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('editteacher/<int:user_id>',views.editteacher,name='editteacher'),
    path('teacheredit/<int:user_id>',views.teacheredit,name='teacheredit'),
    path('cardteacher/<int:user_id>',views.cardteacher,name='cardteacher')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)