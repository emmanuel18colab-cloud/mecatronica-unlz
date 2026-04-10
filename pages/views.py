from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def post_list(request):
    posts = Post.objects.all()
    query = request.GET.get('q')
    tipo = request.GET.get('tipo')
    anio = request.GET.get('anio')

    if query:
        posts = posts.filter(titulo__icontains=query)
    if tipo:
        posts = posts.filter(tipo=tipo)
    if anio:
        posts = posts.filter(anio=anio)

    return render(request, 'pages/post_list.html', {'posts': posts})

class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'pages/post_form.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'pages/post_form.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'pages/post_confirm_delete.html', {'post': post})