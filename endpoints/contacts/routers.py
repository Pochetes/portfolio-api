import json
from fastapi import APIRouter, Request
from fastapi.exceptions import HTTPException
from starlette.responses import JSONResponse
from .models import Contact, UpdateContact
from typing import List
from bson import json_util

router = APIRouter(prefix='/contacts')

# ================== START /contacts endpoint ==================

# GET all contacts (i.e. LinkedIn, Twitter, Github)
@router.get('', response_model=List[Contact])
def get_all_contacts(request: Request):
    contacts = list(request.app.db['contacts'].find({}))
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(contacts, default=json_util.default))
    if response is not None:
        return JSONResponse(response, 200)
    
    raise HTTPException(404, "No contacts found!")

# CREATE a new contact
@router.post('', response_model=Contact)
def create_a_new_contact(contact: Contact, request: Request):
    newContact = contact.dict()
    request.app.db['contacts'].insert_one(newContact)
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(newContact, default=json_util.default))
    if response is not None:
        return JSONResponse(response, 201)
    
    raise HTTPException(400, "Bad request")

# GET a contact by title
@router.get('/{title}', response_model=Contact)
def get_a_contact_by_title(title: str, request: Request):
    # checks if title exists in MongoDB db
    if request.app.db['contacts'].find({"title": title}, {"$exists": False}):
        raise HTTPException(404, f"Contact from {title} does not exist!")

    contact = request.app.db['contacts'].find_one({"title": title})

    response = json.loads(json.dumps(contact, default=json_util.default))
    if response is not None:
        return JSONResponse(response, 200)

    raise HTTPException(404, f"Contact from {title} not found")

# UPDATE a contact by title
@router.put('/{title}', response_model=UpdateContact)
def update_a_contact_by_title(title: str, contact: Contact, request: Request):
    # checks if title exists in MongoDB db
    if request.app.db['contacts'].find({"title": title}, {"$exists": False}):
        raise HTTPException(404, f"Contact from {title} does not exist!")

    updatedContact = contact.dict()
    request.app.db['contacts'].update_one({"title": title}, { "$set": updatedContact})
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(updatedContact, default=json_util.default))
    if response is not None:
        return JSONResponse(response, 200)
        
    raise HTTPException(404, f"Contact from {title} does not exist!")

# DELETE a contact by title
@router.delete('/{title}', response_model=Contact)
def delete_a_contact_by_title(title: str, request: Request):
    # checks if title exists in MongoDB db
    if request.app.db['contacts'].find({"title": title}, {"$exists": False}):
        raise HTTPException(404, f"Contact from {title} does not exist!")    
    
    deletedContact = request.app.db["contacts"].delete_one({"title": title})

    if deletedContact.deleted_count == 1:
        return JSONResponse(status_code=204, content=f"Deleted {title} contact")

    raise HTTPException(status_code=404, detail=f"Contact from {title} not found")
# ================== END /contacts endpoint ==================
