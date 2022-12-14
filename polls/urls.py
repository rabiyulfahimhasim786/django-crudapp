from django.urls import path

from . import views
#from django.conf.urls import url

urlpatterns = [
    path('polls/', views.index, name='index'),
    path('',views.indexhtml,name='indexhtml'),
    path('create',views.create,name="create"),
    path('retrieve',views.retrieve,name="retrieve"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),
    #url(r'^delete_product/(?P<pk>[0-9]+)/$', views.delete,name="delete"),
]
