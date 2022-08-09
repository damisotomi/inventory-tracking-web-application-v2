from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/add',views.ProductCreateView.as_view(), name='product_form'),
    path('products/<uuid:pk>',views.ProductDetailView.as_view(), name='product_detail'),
    path('products/<uuid:pk>/edit',views.ProductUpdateView.as_view(), name='product_update_form'),
    path('products/<uuid:pk>/delete',views.ProductDeleteView.as_view(), name='product_delete_form'),
    path('warehouses/', views.WarehouseListView.as_view(), name='warehouses'),
    path('warehouses/add',views.WarehouseCreateView.as_view(), name='warehouse_form'),
    path('warehouse/<int:pk>/edit',views.WarehouseUpdateView.as_view(), name='warehouse_update_form'),
    path('warehouse/<int:pk>/delete',views.WarehouseDeleteView.as_view(), name='warehouse_delete_form'),
    path('warehouses/<int:pk>',views.WarehouseDetailView.as_view(), name='warehouse_detail'),
    path('productinstance/', views.ProductInstanceListView.as_view(), name='product_instances'),
    path('productinstance/add',views.ProductInstanceCreateView.as_view(), name='product_instance_form'),
    path('productinstance/<int:pk>/edit',views.ProductInstanceUpdateView.as_view(), name='product_instance_update_form'),
    path('productinstance/<int:pk>/delete',views.ProductInstanceDeleteView.as_view(), name='product_instance_delete_form'),
    path('productinstance/<int:pk>',views.ProductInstanceDetailView.as_view(), name='product_instance_detail'),
    path('group/add',views.GroupCreateView.as_view(), name='group_form'),
    path('groups/', views.GroupListView.as_view(), name='groups'),
    path('groups/<int:pk>', views.GroupDetailView.as_view(), name='group_detail'),
    path('groups/<int:pk>/edit', views.GroupUpdateView.as_view(), name='group_update_form'),
    path('groups/<int:pk>/delete', views.GroupDeleteView.as_view(), name='group_delete_form'),
    path('overviewmanual/', views.overview_manual, name='overview_manual'),
    path('productmanual/', views.product_manual, name='product_manual'),
    path('transactionmanual/', views.transaction_manual, name='transaction_manual'),
    path('warehousemanual/', views.warehouse_manual, name='warehouse_manual'),
    path('groupmanual/', views.group_manual, name='group_manual'),
    path('profile/', views.profile, name='profile'),
       
    ]

urlpatterns+=staticfiles_urlpatterns()
