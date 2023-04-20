from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DictionaryViewSet, DictionaryAllViewSet
####### from . import views viewsをまるごとインポートしてる

# URLパターンを逆引きできるように名前を付ける
app_name = 'myapp'

router = DefaultRouter()
# viewsets使うならrouterから
router.register('dictionaryAll', DictionaryAllViewSet )

# URLパターンを登録するための変数
urlpatterns = [
    # リクエストされたURLが''(無し)の場合
    # viewsモジュールのIndexVieを実行
    # path('', views.IndexView.as_view(), name='index'),
    #####  as_view() は全部のビュークラスのスーパークラスで定義されてるクラスメソッド
    #####  クラスメソッドはクラスのインスタンス化が不要で上みたいにダイレクト実行できる
    #####  as_view()でＨＴＴＰレスポンス返される
    ####   name='index' はＵＲＬパターンを認識するための名前
    path('', include(router.urls)),
    # APIViewからなら直接
    path('dictionary/', DictionaryViewSet.as_view(), name='dictionary'),
]
