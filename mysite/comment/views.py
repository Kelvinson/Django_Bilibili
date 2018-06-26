from django.shortcuts import redirect,reverse,render
from django.contrib.contenttypes.models import ContentType

from .models import Comment
# Create your views here.
def update_comment(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))

    # 数据检查
    if not request.user.is_authenticated:
        return render(request, 'error.html', {'message': '请先登录再评论','redirect_to':referer})

    comment_content = request.POST.get('comment_content').strip()
    if comment_content == '':
        return render(request,'error.html',{'message':'评论为空！！！','redirect_to':referer})

    try:
        object_id = int(request.POST.get('object_id'))
        content_type = request.POST.get('content_type')
        model_class = ContentType.objects.get(model=content_type).model_class()
        model_obj = model_class.objects.get(pk=object_id)
    except Exception as error:
        return render(request, 'error.html', {'message': '评论对象不存在！！！','redirect_to':referer})

    comment = Comment()
    comment.comment_user = request.user
    comment.comment_content = comment_content
    comment.content_object = model_obj
    comment.save()
    # 返回原来的网页

    return redirect(referer)

def get_comment_list(request):
    pass