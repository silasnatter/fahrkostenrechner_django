from user.forms import NewPostForm, UserRegisterForm
from django.contrib.auth import views as auth_views
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post
from django.views.generic import ListView
# from .forms import NewCommentForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created')
            return redirect('login')
    
    else:
        form = UserRegisterForm()
    
    return render(request, 'user/register.html', { 'form': form })


class PostListView(ListView):
	model = Post
	template_name = 'feed/user_posts.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super(PostListView, self).get_context_data(**kwargs)
		return context


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user 


    # check if attributes exists
    
    

    # return HttpResponse("<img src='{}' alt='Alternative'".format(name))

    return render(request, 'feed/post_detail.html', { 'post':post })


def image_view(request, pk):
    post = get_object_or_404(Post, pk=pk)


     # check if attributes exists
    class Media:
        def __init__(self, img_1, img_2, img_3, vid_1):
            img_1 = self.img_1
            img_2 = self.img_2
            img_3 = self.img_3
            vid_1 = self.vid_1
    
    try:
        media_obj = Media()
        media_obj.img_1 = post.img_1
        media_obj.img_2 = post.img_2
        media_obj.img_3 = post.img_3
        media_obj.vid_1 = post.vid_1
    except:
        pass


    print(post.img_1)

    # return render(request, 'feed/image_view.html', { 'post':post, 'media': media_obj })
    return render(request, 'feed/image_view.html', { 'post':post })

@login_required
def create_post(request):
    user = request.user
    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_name = user
            data.save()
            messages.success(request, f'Posted Successfully')
            return redirect('create_post')
    
    else:
        form = NewPostForm()

    return render(request, 'feed/create_post.html', { 'form':form })

# @login_required
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     user = request.user
#     if request.method == 'POST':
#         form = NewCommentForm(request.POST)
#         if form.is_valid():
#             data = form.save(commit=False)
#             data.post = post
#             data.username = user
#             data.save()
#             return redirect('post-detail', pk=pk)
#     else:
#         form = NewCommentForm()
    
#     return render(request, 'feed/post_detail.html', { 'post':post, 'form':form })
    
