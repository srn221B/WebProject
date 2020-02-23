from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

class Contents(models.Model):
    class Meta:
        #テーブル名を定義
        db_table = 'Contents'
    #テーブルのカラムに対応するフィールドを定義
    contents_name = models.CharField(verbose_name='作品名',max_length=255,null=False)
    picture = models.ImageField(verbose_name='作品画像',upload_to='images/')
    contents_detail = models.TextField(verbose_name='詳細',null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.contents_name


class Reviews(models.Model):
    user_name = models.ForeignKey(User,verbose_name='ユーザー名',on_delete=models.CASCADE,null=False)
    contents = models.ForeignKey(Contents,verbose_name='作品名',on_delete=models.CASCADE,null=False)
    review = models.IntegerField(verbose_name='評価',null=False,validators=[MinValueValidator(1),MaxValueValidator(5)])
    class Meta:
        #テーブル名
        db_table = 'Reviews'
        #ユニーク制約
        unique_together = (
            ('user_name','contents')
        )
    def publish(self):
        self.save()



class review_ratings(models.Model):
    user_name = models.ForeignKey(User,verbose_name='ユーザー名',on_delete=models.CASCADE,null=False)
    contents = models.ForeignKey(Contents,verbose_name='作品名',on_delete=models.CASCADE,null=False)
    rating = models.FloatField(verbose_name='rating',null=False)
    class Meta:
        db_table = 'review_rating'

    def publish(self):
        self.save()
