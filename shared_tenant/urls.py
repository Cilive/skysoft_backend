from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import   BranchMangerViewSet, BranchesViewSet, CompanyRegistration, CompanyTokenObtainPairView, EmployeeRegistration
from rest_framework import routers



router = routers.DefaultRouter()

router.register("company", CompanyRegistration, basename="company")
router.register("employee", EmployeeRegistration, basename="employee")
router.register("branches", BranchesViewSet, basename="branches")
router.register("branchmanager", BranchMangerViewSet, basename="branch_manager")



urlpatterns = [

    
    path('login/',CompanyTokenObtainPairView.as_view(),name='login'),
    path('', include(router.urls)),

    # path('company/',CompanyRegistration.as_view(),name='company'),
    # path('company/<int:pk>',CompanyRegistration.as_view(),name='company'),
    # path('employee/',EmployeeRegistration.as_view(),name='employee'),
    # path('employee/<int:pk>/',EmployeeRegistration.as_view(),name='employee'),

]

# urlpatterns = format_suffix_patterns(urlpatterns)
