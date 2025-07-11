"""
URL configuration for StockAnalysis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from analysis import views

from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


#django admin customization




urlpatterns = [
    path("admin/", admin.site.urls),
    path('footer',views.footer),
    path('nav',views.nav),
    path('forgot',views.forgot,name="forgot"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('about',views.about,name="about"),

    path('base',views.base),
    path('',views.index,name="index"),
    path('blogs',views.allblogs,name="blogs"),
    path('blogsdesc/<int:id>',views.blogsdesc,name="blogsdesc"),
    path('experts',views.allexperts,name="experts"),
    path('expertsdesc/<int:id>',views.expertsdesc,name="expertsdesc"),
    path('latest_news',views.alllatest_news,name="latest_news"),
    path('newsdesc/<int:id>',views.newsdesc,name="newsdesc"),
    path('tutorials',views.alltutorials,name="tutorials"),
    path('faq',views.allfaq,name="faq"),
    path('review',views.review,name="review"),
    path('contact',views.contact,name="contact"),
    path('sidebar',views.sidebar),
    path('changepass',views.changepass,name="changepass"),
    path('help',views.help,name="help"),
    path('userprofile',views.userprofile,name="userprofile"),
    path('editprofile',views.editprofile,name="editprofile"),
    path('logout',views.logout,name="logout"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('ques',views.ques,name="ques"),
    path('ques_2',views.ques_2,name="ques_2"),
    path('ques_3',views.ques_3,name="ques_3"),
    path('ques_candle',views.ques_candle,name="ques_candle"),
    path('allyears',views.allyears,name="allyears"),
    path('year',views.year,name="year"),
    path('month',views.month,name="month"),
    path('range',views.range,name="range"),
    path('candle',views.candle,name="candle"),
    path('candle_year',views.candle_year,name="candle_year"),
    path('comp_2',views.comp_2,name="comp_2"),
    path('compyear_2',views.compyear_2,name="compyear_2"),
    path('compmonth_2',views.compmonth_2,name="compmonth_2"),
    path('comprange_2',views.comprange_2,name="comprange_2"),
    path('comp_3',views.comp_3,name="comp_3"),
    path('compyear_3',views.compyear_3,name="compyear_3"),
    path('compmonth_3',views.compmonth_3,name="compmonth_3"),
    path('comprange_3',views.comprange_3,name="comprange_3"),
    path('candle',views.candle,name="candle"),
    path('candle_year',views.candle_year,name="candle_year"),


    path('live',views.live,name="live"),
    path('sentiment',views.sentiment,name="sentiment"),
    path('stock_csv',views.stock_csv,name='stock_csv'),
    path('stnews',views.stnews,name="stnews"),
    path('reliance',views.reliance,name="reliance"),
    path('bajaj',views.bajaj,name="bajaj"),
    path('tata',views.tata,name="tata"),
    path('tcs',views.tcs,name="tcs"),
    path('itc',views.itc,name="itc"),
    path('sun',views.sun,name="sun"),
    path('icici',views.icici,name="icici"),
    path('sbi',views.sbi,name="sbi"),
    path('hdfc',views.hdfc,name="hdfc"),
    path('infy',views.infy,name="infy"),
    path('otp',views.otp,name="otp"),

    path('newstock',views.newstock,name="newstock"),

    
    




]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)