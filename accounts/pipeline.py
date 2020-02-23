import os
import urllib.request, urllib.error
from django.core.files.base import ContentFile

import sys

def save_profile_picture(backend, strategy, details, response ,user=None, *args, **kwargs):
    url = None
    if backend.name == 'google-oauth2':
        # 画像のurlを保存
        url = response['image'].get('url')
        # 拡張子を用意
        ext = url.split('.')[-1].split('?')[0]
    if url:
        user.profile_picture_url = url
        picture = os.path.join(sys.MEDIA_ROOT, 'profiles', '%s.%s' % (user.username, ext))
        # 既にプロフィール画像がある場合、削除
        if os.path.exists(picture):
            os.remove(picture)
        user.profile_picture.save('%s.%s' % (user.username, ext), ContentFile(urllib.request.urlopen(url).read()))
        user.save()