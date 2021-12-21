# Contacts Docs

Contains data about my social media handles and their links to them.

## Methods

#### `GET` /contacts

Gets all contacts.

#### `POST` /contacts

Creates a new contact.

#### `GET` /contacts/{title}

Gets a contact by title.

#### `PUT` /contacts/{title}

Updates a contact. Gets a contact by title.

#### `DELETE` /contacts/{title}

Deletes a contact by title.

## Sample API Response

```json
{
    "_id": {
        "$oid": "61beaeaae241994e889ecb62"
    },
    "title": "LinkedIn",
    "link": "https://www.linkedin.com/in/RobertoMartinez21"
}
```

## Parameters

### Path Params

Parameter | Required/Optional | Description | Type
------ | -------- | -------- | -------- 
`title` | required | The value for the `Interest` object you want to look up. | `string`

### Query Params

Parameter | Required/Optional | Description | Type
------ | -------- | -------- | -------- 
`title` | required | The value for the `Interest` object you want to look up. | `string`
`link` | optional | The link to the social media page | `string`


