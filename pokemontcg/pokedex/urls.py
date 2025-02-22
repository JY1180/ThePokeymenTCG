from django.urls import path

from . import views

app_name = "pokedex"

urlpatterns = [
    path("searchInput", views.searchInputView, name="searchInput"),
    path("pokemon_list", views.PokemonListView.as_view(), name="pokemon_list"),
    path("trainer_list", views.TrainerListView.as_view(), name="trainer_list"),
    path("energy_list", views.EnergyListView.as_view(), name="energy_list"),
    path("test", views.testView, name="test"),
    path("loadInitialData", views.loadInitialData, name="loadInitialData"),
    path("create/<str:card_id>", views.createPokemonCard, name="create"),
    path("search/<str:card_name>", views.searchView, name="search"),
    path("", views.homeView, name='home'),
    path("bis/<int:pk>", views.PokemonDetailbisView.as_view(), name="pokemon_detail_bis",),
    path( "js/<int:pk>", views.PokemonDetailJsView.as_view(), name="pokemon_detail_js", ),
    path("bisT/<int:pk>", views.TrainerDetailbisView.as_view(), name="trainer_detail_bisT",),
    path( "js/<int:pk>", views.TrainerDetailJsView.as_view(), name="trainer_detail_js", ),
    path("bisE/<int:pk>", views.EnergyDetailbisView.as_view(), name="energy_detail_bisE",),
    path( "js/<int:pk>", views.EnergyDetailJsView.as_view(), name="energy_detail_js", ),
    path("delete/<int:pk>", views.PokemonDeleteView.as_view(),
         name="pokemon_delete"),
    path("energy_delete/<int:pk>", views.EnergyDeleteView.as_view(),
         name="energy_delete"),
    path("trainer_delete/<int:pk>", views.TrainerDeleteView.as_view(),
         name="trainer_delete"),
]