from django.contrib.auth.models import User
from django.db.models.base import Model
from django.utils.translation import templatize
from django.views import generic

from .models import Post

class IndexView(generic.TemplateView):
    template_name = 'index.html'

# Create your views here.
class PostListView(generic.ListView):
    model = Post
    templat_name = 'post_list.html'

    def get_queryset(self):
        diaries = Post.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries