from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm


def index(request):
    """The home page for the Blog."""
    return render(request, 'blogs/index.html')


def blogposts(request):
    """Show all blogposts."""
    blogposts = BlogPost.objects.order_by('date_added')
    context = {'blogposts': blogposts}
    return render(request, 'blogs/blogposts.html', context)


def blogpost(request, blogpost_id):
    """Show a single blogpost."""
    blogpost = BlogPost.objects.get(id=blogpost_id)
    context = {'blogpost': blogpost}
    return render(request, 'blogs/blogpost.html', context)


def new_blogpost(request):
    """Add a new blog post."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogposts')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_blogpost.html', context)
