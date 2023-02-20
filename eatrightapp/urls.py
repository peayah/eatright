# cohorts URL Configuration

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
# Use static() to add URL mapping to serve static
# files during development (only)
from django.conf import settings
from django.conf.urls.static import static


from django.urls import path
import catalog.views
from catalog import views
# from . import views
from django.urls import re_path as url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += [
#     path('catalog/', include('catalog.urls')),
# ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    # path('',
    #      views.index,
    #      name='index'),

    path('consumedfood/',
         views.ConsumedFoodListView.as_view(),
         name = 'all-consumed'),

    path('filtered_list/',
         views.food_list,
         name = 'filtered-list'),

    path('food/',
         views.FoodListView.as_view(),
         name = 'all-food'),

    path('notes/',
         views.NotesPageView.as_view(),
         name = 'notes'),

    path('food/create/',
         views.FoodCreate.as_view(),
         name = 'food-create'),

    path('foodinstance/create/',
         views.FoodInstanceCreate.as_view(),
         name = 'foodinstance-create'),

    path('foodinstance/<pk>/delete/',
         views.FoodInstanceDelete.as_view(),
         name='foodinstance-delete'),

    path('dailyintake/',
         views.DailyIntakeView.as_view(),
         name="user-settings"),

    path('dailyintake/<slug:pk>/',
         views.DailyIntakeUpdate.as_view(),
         name='settings_update'),

    url(r'^list$', views.food_list),
]
