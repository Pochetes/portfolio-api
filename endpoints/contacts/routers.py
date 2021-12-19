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
def getContacts(request: Request):
    contacts = list(request.app.db['contacts'].find({}))
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(contacts, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
       raise HTTPException(400, "No contacts found!")

# CREATE a new contact
@router.post('', response_model=Contact)
def createContact(contact: Contact, request: Request):
    newContact = contact.dict()
    request.app.db['contacts'].insert_one(newContact)
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(newContact, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
        raise HTTPException(400, "Bad request")

# GET a contact by title
@router.get('/{title}', response_model=Contact)
def getContact(title: str, request: Request):
    contact = request.app.db['contacts'].find_one({"title": title})

    response = json.loads(json.dumps(contact, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
        raise HTTPException(404, f"Contact from {title} not found")

# UPDATE a contact by title
@router.put('/{title}', response_model=UpdateContact)
def updateContact(title: str, contact: Contact, request: Request):
    updatedContact = contact.dict()
    request.app.db['contacts'].update_one({"title": title}, { "$set": updatedContact})
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(updatedContact, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
        raise HTTPException(400, "Person does not exist!")

# DELETE a contact by title
@router.delete('/{title}', response_model=Contact)
def deleteContact(title: str, request: Request):
    deletedContact = request.app.db["contacts"].delete_one({"title": title})

    if deletedContact.deleted_count == 1:
        return JSONResponse(status_code=204, content=f"Deleted {title} contact")

    raise HTTPException(status_code=404, detail=f"Contact from {title} not found")
# ================== END /contacts endpoint ==================
