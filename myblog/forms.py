from django import forms
from .models import Post,Category,Comment

#choices = [('coding','coding'),('sports','sports'),('entertainment','entertainment'),('history','history')]
choices=Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
	choice_list.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','title_tag','author','category','body','snippet','header_image')

		widgets = {
        	'title': forms.TextInput(attrs={'class':'form-control','placeholder': 'Write any title here......'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder': 'Write any tag here......'}),
            #'author': forms.TextInput(attrs={'class':'form-control','value': '','id': 'elder', 'type':'hidden'}),
            'author': forms.Select(attrs={'class':'form-control','placeholder': 'Write your here......'}),
            'category': forms.Select(choices=choice_list , attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder': 'Write your content here......'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),
		}

class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','title_tag','body','snippet')

		widgets = {
        	'title': forms.TextInput(attrs={'class':'form-control','placeholder': 'Write any title here......'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder': 'Write any tag here......'}),
            #'author': forms.Select(attrs={'class':'form-control','placeholder': 'Write your here......'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder': 'Write your content here......'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),
		}		

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder': 'Write your comment here......'}),
            }               
