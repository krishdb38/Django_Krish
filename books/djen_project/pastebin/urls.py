from django.urls import path
from .views import PasteCreate , PasteDetail #, PasteList


urlpatterns = [
                path('', PasteCreate.as_view(), name='pastebin_paste_list'),
                path('<int:pk>', PasteDetail.as_view(), name = 'pastebin_paste_detail')
]