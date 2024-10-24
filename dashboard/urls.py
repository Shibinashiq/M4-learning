"""
This module defines the URL patterns for the dashboard application in a Django web application.

The URL patterns cover various functionalities, including authentication, route management, salesman management, brand management, product management, customer management, warehouse management, vehicle management, user management, coupon booklet type management, coupon booklet management, order management, cashier log management, and reporting.

Each URL pattern is associated with a view function that handles the corresponding functionality. The view functions are defined in various submodules, such as `authentication`, `route`, `salesman`, `brand`, `product`, `customer`, `warehouse_manager`, `vehicle`, `user`, `coupon_booklet_type`, `coupon_booklet`, `order`, `cashier_log`, `report`, and `credit`.

The URL patterns provide a structured and organized way to access the different features of the dashboard application, making it easier to maintain and extend the application as needed.
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from dashboard.views import(
    home,
    authentication,
)

urlpatterns = [


    # ==================================== Home ============================================= #

    path("", home.home, name="dashboard-home-manager"),
    # ==================================== Authentication ============================================= #

    path("login/", authentication.login, name="dashboard-login"),
    # path("logout/", auth_views.LogoutView.as_view(), name="dashboard-logout"),


   



]
