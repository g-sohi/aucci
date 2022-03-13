# REST API endpoints for listings

from email.mime import image
from pymongo import MongoClient
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from bson import ObjectId
import pyuploadcare as PuC
from pyuploadcare import Uploadcare
import json

connection_string = "mongodb+srv://auccibids:Seng401!@aucci.eqyli.mongodb.net/aucciDB"

def db_collection(collection):
    client = MongoClient(connection_string)
    db = client.aucciDB

    return db[collection]

# Prepares for jsonResponse
# Only works for lists of items
def itemList_jsonify(data):
    json_data = []
    for datum in data:
        json_data.append({"_id" : str(datum['_id']), "useruniqid" : str(datum['useruniqid']), "item" : datum['item']})

    return json_data

# Prepares for jsonResponse
# Only works for lists of items
def categories_jsonify(data):
    json_data = []
    for datum in data:
        json_data.append({"_id" : str(datum['_id']), "name" : str(datum['name'])})

    return json_data

# GET listings by name or GET all listings
def listing(request, name = ""):
    if request.method == "GET":
        cursor = db_collection("listings")

        if name != "":
            listings = cursor.find({"item" : name})
        else:
            listings = cursor.find({})

        json_content = itemList_jsonify(listings)

        return JsonResponse(json_content, safe=False)
    else:
        return HttpResponse("Unrecognized request. This URL only accepts GET methods.")

# DELETE listing by object id
@csrf_exempt 
def delete_listing(request, oid = ""):
    if request.method != "DELETE":
        return HttpResponse("Unrecognized request. This URL only accepts DELETE methods.")
    if oid == "":
        return HttpResponse("Specify one object to delete")
    
    cursor = db_collection("listings")

    query = { "_id": ObjectId(oid) }

    try: 
        cursor.delete_one(query)
    except:
        return HttpResponse("Something went wrong")
    else:
        return HttpResponse("Success")

# POST new listing
@api_view(['POST'])
def create_listing(request):
    if request.method != "POST":
        return HttpResponse("Unrecognized request. This URL only accepts POST methods.")

    id = db_collection("listings").insert_one(request.data).inserted_id

    return JsonResponse({"id" : str(id)})

# UPDATE listing by id
@api_view(['POST'])
def update_listing(request, oid = ""):
    if request.method != "POST":
        return HttpResponse("Unrecognized request. This URL only accepts POST methods.")
    if oid == "":
        return HttpResponse("Specify one object to update")
    
    cursor = db_collection("listings")

    try:
        cursor.update_one({'_id':ObjectId(oid)}, {"$set": request.data}, upsert=False)
    except:
        print("Something went wrong")
        return HttpResponse("Something went wrong")
    else:
        return HttpResponse("Success")

# GET catagories
def categories(request):
    if request.method == "GET":
        cursor = db_collection("categories")

        listings = cursor.find({})

        json_content = categories_jsonify(listings)

        return JsonResponse(json_content, safe=False)
    else:
        return HttpResponse("Unrecognized request. This URL only accepts GET methods.")

@api_view(['POST'])
def up(request):
    # if imagepath == "":
    #     return HttpResponse("Specify an image path")

    if request.method == "POST":
        urls = []
        Uploadcare = PuC.Uploadcare(public_key =  '20a0df730e28f42bb662', secret_key = '8ad164c8ada8aaf4034f')
        for image in request.data['imagepath']:
            print(image)
            try:
                with open(image, 'rb') as f:
                    url = Uploadcare.upload(f)
                    urls.append(str(url))
            except Exception as e: 
                return HttpResponse(e)

            
        if(len(urls) == 0):
            return HttpResponse("Upload error: it appears nothing was uploaded")
        for thing in urls:
            print (thing)
        urls_json = json.dumps(urls)
        # print (urls_json)

        return JsonResponse(urls_json, safe=False)