from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
# from moon_stone.main import views as MainViews
from main import views as NewViews

urlpatterns = [
    path('', NewViews.index, name='index'),
    # path('predict_set/<str:model>', NewViews.predict_set, name='predict_set'),
]
