from django.forms import ModelForm
from .models import Post
from .models import Comment


class CreatePostModelForm(ModelForm):
    class Meta:
        model = Post
        #fields = ['question_text','pub_date']
        #include
        exclude = ['id', 'date_modified']

class CommentModelForm(ModelForm):
    class Meta:
        model = Comment
        #fields = ['question_text','pub_date']
        #include
        exclude = ['id']