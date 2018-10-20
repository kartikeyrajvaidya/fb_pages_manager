from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

# not used
class SimpleForm(forms.Form):
    name = forms.CharField(label="Page Name", required=False)
    about = forms.CharField(label="About Page", required=False)
    bio = forms.CharField(label="Bio", required=False)
    website = forms.CharField(label="Website", required=False)
    phone = forms.CharField(label="Phone", required=False)
    whatsapp_number = forms.CharField(label="Whatsapp Number", required=False)
    general_info = forms.CharField(label="General Info", required=False)

    impressum = forms.CharField(label="Impressum", required=False)
    description = forms.CharField(label="Description", required=False)
    company_overview = forms.CharField(label="Company Overview", required=False)
    hello = forms.CharField(required=False)

    #category = forms.CharField(label="Page Category", required=False)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.layout = Layout(
        Field("hello", type="hidden", hidden=True)
    )
class NewPostForm(forms.Form):
    pass