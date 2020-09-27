from django.conf.urls import url
from dappx import views
# SET THE NAMESPACE!
app_name = 'dappx'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^uploaded_posts/$',views.upload_posts_screen,name='uploaded_posts'),
    url(r'^upload_post/$',views.upload_post,name='upload_post'),
]