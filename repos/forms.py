from datetime import datetime

from django import forms
from django.utils.text import slugify

from tinymce.widgets import TinyMCE

from .models import Repository
from tags.models import Tag


class RepositoryModelForm(forms.ModelForm):
	class Meta:
		model = Repository
		fields = ['name', 'description', 'image', 'tags']

		widgets = {
			"name": forms.TextInput(attrs={"placeholder": "Repository name"}),
			"description": forms.Textarea(
				attrs={"placeholder": "Repository description"}
			),
			"tags": forms.CheckboxSelectMultiple(),
		}

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request')
		super(RepositoryModelForm, self).__init__(*args, **kwargs)

	def clean_name(self):
		# name = self.cleaned_data.get('name')
		name = self.cleaned_data['name']
		query_set = Repository.objects.filter(
			name=name,
			owner=self.request.user
		)

		if query_set.exists():
			raise forms.ValidationError(
				"Repository named '{}' already exists".format(name)
			)

		slugified = slugify(name)
		if Repository.objects.filter(
			slug=slugified, owner=self.request.user).exists():
			raise forms.ValidationError(
				"Slugified repo named '{}' already exists".format(slugified)
			)

		return name


class RepositoryUpdateModelForm(forms.ModelForm):
	request = None
	old_name = None

	class Meta:
		model = Repository
		fields = ['name', 'description', 'image', 'tags']

		widgets = {
			"name": forms.TextInput(attrs={"placeholder": "Repository name"}),
			"description": forms.Textarea(
				attrs={"placeholder": "Repository description"}
			),
			"tags": forms.CheckboxSelectMultiple(),
		}

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request')
		self.old_name = kwargs.pop('old_name')
		super(RepositoryUpdateModelForm, self).__init__(*args, **kwargs)
		self.fields['image'].label = 'Image (400x300px)'

	def clean_name(self):
		name = self.cleaned_data['name']
		if not name == self.old_name:
			query_set = Repository.objects.filter(
				name=name,
				owner=self.request.user
			)

			if query_set.exists():
				raise forms.ValidationError(
					"Repository named '{}' already exists".format(name)
				)

			slugified = slugify(name)
			if Repository.objects.filter(
				slug=slugified, owner=self.request.user).exists():
				raise forms.ValidationError(
					"Slugified repo named '{}' already exists".format(slugified)
				)


		return name


class TinyMCEFileEditForm(forms.Form):
	content = forms.CharField(widget=TinyMCE(mce_attrs={'width': '100%'}))
	commit_message = forms.CharField(
		required=False,
		empty_value="edited on {}".format(
			datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
		)
	)


class FileCreateForm(forms.Form):
	filename = forms.CharField(label='File name', required=True)
	content = forms.CharField(widget=TinyMCE(mce_attrs={'width': '100%'}))
	commit_message = forms.CharField(
		required=False,
		empty_value="Created on {}".format(
			datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
		)
	)

	def clean_filename(self):
		filename = self.cleaned_data['filename']
		if filename == ('.html'.strip()):
			raise forms.ValidationError(
				'Please enter file name, i.e. "example.html"'
			)

		return filename


class FileRenameForm(forms.Form):
	# old_filename = forms.CharField(label='File name', required=True)
	new_filename = forms.CharField(label='New file name', required=True)
	commit_message = forms.CharField(
		required=False,
		empty_value="Created on {}".format(
			datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
		)
	)
	def clean_filename(self):
		new_filename = self.cleaned_data['new_filename']
		if new_filename == ('.html'.strip()):
			raise forms.ValidationError(
				'Please enter file name, i.e. "example.html"'
			)

		return new_filename

class RepoForkRenameForm(forms.Form):
	new_reponame = forms.CharField(label='New fork name', required=True)

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		super(RepoForkRenameForm, self).__init__(*args, **kwargs)

	def clean_new_reponame(self):
		new_reponame = self.cleaned_data['new_reponame']
		# if not new_reponame == self.old_filename:
		query_set = Repository.objects.filter(
			name=new_reponame,
			owner=self.request.user
		)

		if query_set.exists():
			raise forms.ValidationError(
				"Repository named '{}' already exists".format(new_reponame)
			)

		slugified = slugify(new_reponame)
		if Repository.objects.filter(
			slug=slugified, owner=self.request.user).exists():
			raise forms.ValidationError(
				"Slugified repo named '{}' already exists".format(slugified)
			)


		return new_reponame
