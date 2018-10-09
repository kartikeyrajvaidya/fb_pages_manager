from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from requests import request as call
import json
from . import forms
# Create your views here.


def home(request):
    context = {
        "title":"FB Page Manager"
    }
    # my_template = loader.get_template("fbapp/home.html")  # old-way
    # return HttpResponse(my_template.render(context,request))
    return render(request, "fbapp/home.html", context)


def dashboard(request):
    if(request.method=="POST"):
        token=request.POST.get("token",'')
        header="OAuth "+ token
        details=call('GET', 'https://graph.facebook.com/me/accounts', headers={"Authorization": header})
        d2=call('GET','https://graph.facebook.com/me', headers={"Authorization":header})

        # ------------ new stuff ----------------- #

        page_ids_list = details.json()["data"]
        page_attributes='name,phone,overall_star_rating,is_published,location,verification_status'

        dict_details = details.json()

        page_list = []
        for index in range(len(page_ids_list)):
            page_id = page_ids_list[index]["id"]
            page_token = page_ids_list[index]["access_token"]
            api_url="https://graph.facebook.com/"+ page_id + "?fields="+page_attributes
            header='OAuth ' + page_token
            page_obj = call('GET', api_url, headers={"Authorization": header})

            page_obj_json = page_obj.json()
            page_obj_json["is_published"] = str(page_obj_json["is_published"])
            page_ids_list[index]["page_info"] = page_obj_json

            page_list.append(json.dumps(page_obj.json()))


        # ------------ new stuff ends----------------- #

        typo = str(type(details.json()))
        details=json.dumps(details.json())

        d2=json.dumps(d2.json())
        return render(request, "fbapp/dashboard.html",{"title":"Dashboard",'pages': page_ids_list, 'personal':d2 , 'page_list' : page_list  }) #, 'mega_details': mega_details})
    else:
        # here use sessions to save user-id and pageids/tokens
        details = {}
        d2 = {}
        return render(request, "fbapp/dashboard.html",{"title":"Dashboard",'pages': details, 'personal':d2}) #, 'mega_details': mega_details})

    #return render(request, "fbapp/dashboard.html")

@csrf_exempt
def get_page_details(request):
    if request.method=="POST":
        print("HELLO")
        fields='name,about,phone,emails,website,description,fan_count,link,overall_star_rating,location,displayed_message_response_time'
        pageToken=request.POST.get("pageToken",'')
        pageId=request.POST.get("pageId",'')
        header='OAuth ' + pageToken
        url="https://graph.facebook.com/"+pageId + "?fields="+fields
        details=call('GET', url, headers={"Authorization": header})

        details=json.dumps(details.json())
        return HttpResponse(details)
    return HttpResponse(400)

#not used
def get_form(request):

    id = request.GET.get("id",'')
    form = forms.SimpleForm()

    return render(request, 'fbapp/pageform.html', {'form_obj': form})


