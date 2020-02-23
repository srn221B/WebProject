from django.shortcuts import redirect,render
from django.views import View
from .models import Contents,Reviews

from django.db import connection
from django.views.decorators.csrf import csrf_exempt

from .form import ReviewsAdd

#home
class Home(View):
    #一覧表示処理
    def get(self,request,*args,**kwargs):
        if self.request.user.is_authenticated:
            #SQLの実行
            with connection.cursor() as cursor:
                cursor.execute("select CL.contents_name, CL.picture, CL.contents_detail, RV.review, COALESCE(RR.rating,0) as rating"
                               " from \"Contents\" as CL"
                               " left outer join \"Reviews\" AS RV on CL.id = RV.contents_id and user_name_id = %s"
                               " left outer join review_rating AS RR on RR.user = %s and CL.id = RR.content"
                               " order by rating desc;",[request.user.id,request.user.id])
                reviews = cursor.fetchall()


                review_list = []

                for review in reviews:
                    inraw = []
                    #contents_name
                    inraw.append(review[0])
                    #picture
                    inraw.append(review[1])
                    #detail
                    inraw.append(review[2])
                    #review
                    inraw.append(review[3])
                    #rating list
                    if review[4] == 0:
                        inraw.append(0)
                    else:
                        inraw.append(1)
                    review_list.append(inraw)



            params = {
                'review_list' : review_list,
            }
            return render(request, 'recommend/home.html',params)
        else:
            return redirect('/')

#ReviewPost
class ReviewPost(View):
    @csrf_exempt
    def post(self,request,*args,**kwargs):
        template_name = 'recommend/review_post.html'
        select_contents = request.POST.get('contents')
        contents_id = Contents.objects.get(contents_name=select_contents)

        if Reviews.objects.filter(user_name=request.user.id,contents=contents_id).exists():
            #レビューが存在する場合
            reviewOBJ = Reviews.objects.get(user_name=request.user.id,contents=contents_id)
            review = reviewOBJ.review
            submit_text = "レビュー変更"
        else:
            #レビューが存在しない場合
            review = ""
            submit_text = "レビュー投稿"

        initial_dict = {
            'review' : review
        }
        form = ReviewsAdd(initial=initial_dict)

        params = {
            'contents' : select_contents,
            'submit_text' : submit_text,
            'form':form
        }
        response = render(request, template_name, params)
        return response


    def get(self,request,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('main:home')
        else:
            return redirect('/')

class ReviewPost_done(View):
    def get(self,request,*args,**kwargs):
        redirect('main:home')

    def post(self,request):
        template_name = 'recommend/review_post_done.html'
        select_contents = request.POST.get('contents')
        review = request.POST.get('review')
        contents_id = Contents.objects.get(contents_name=select_contents)

        if self.request.user.is_authenticated:
            if Reviews.objects.filter(user_name=request.user.id, contents=contents_id).exists():
                # レビューが存在する場合
                # Objectを取得しModelを更新
                reviewOBJ = Reviews.objects.get(user_name=request.user.id, contents=contents_id)
                reviewOBJ.review = review
                reviewOBJ.save()

                response = redirect('main:home')
                return response
            else:
                # レビューが存在しない場合
                # Objectを作成
                reviewOBJ = Reviews(user_name=request.user,contents=contents_id,review=review)
                reviewOBJ.save()

                response = redirect('main:home')
                return response

        else:
            redirect('main:home')