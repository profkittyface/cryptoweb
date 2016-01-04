from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'encrypt/$', views.encrypt_index, name='encrypt_index'),
    url(r'encrypt/post/$', views.encrypt_post, name='encrypt_post'),
    url(r'encrypt/(?P<fingerprint>.{40})/$', views.encrypt_index, name='encrypt_index'),

    url(r'decrypt/$', views.decrypt_index, name='decrypt_index'),
    url(r'decrypt/post/$', views.decrypt_post, name='decrypt_post'),

    url(r'address/$', views.address_list_index, name='address_list_index'),
    url(r'address/add/$', views.address_list_add, name='address_list_add'),
    url(r'address/delete/$', views.address_list_delete, name='address_list_delete'),
    url(r'address/delete/(?P<fingerprint>.{40})/$', views.address_list_delete, name='address_list_delete'),
    url(r'address/encrypt/$', views.address_list_encrypt, name='address_list_encrypt'),

    url(r'generate_key/$', views.generate_key_index, name='generate_key_index'),
    url(r'generate_key/post/$', views.generate_key_post, name='generate_key_post'),
]