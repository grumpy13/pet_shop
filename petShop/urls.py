from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('pets/list/',views.pet_list ,name='pets-list'),
    path('pet/detail/<int:pet_id>/',views.pet_detail ,name='pet-details'),

    path('pet/create/',views.pet_create ,name='create-pet'),
    path('pet/update/<int:pet_id>/',views.pet_update ,name='update-pet'),
    path('pet/delete/<int:pet_id>/',views.pet_delete ,name='delete-pet'),

]
