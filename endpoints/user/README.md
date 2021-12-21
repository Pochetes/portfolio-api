# User Docs

Contains data about me such as my name, email and a brief description about me.

## Methods

#### `GET` /user

Gets all user, which should only be me.

#### `POST` /user

Creates a new user. THIS SHOULD ONLY BE DONE ONCE!

#### `PUT` /user/{technology}

Updates the user. Should only really be the description.

## Sample API Response

```json
{
    "_id": {
        "$oid": "61bea61cc60c6acf38e11766"
    },
    "firstName": "John",
    "lastName": "Doe",
    "email": "johndoe@email.com",
    "image": "public/images/<file_name>",
    "description": "A very nice guy indeed!"
}
```

## Parameters

### Path Params

There are no path parameters on this endpoint.

### Query Params

Parameter | Required/Optional | Description | Type
------ | -------- | -------- | -------- 
`firstName` | optional | The user's first name. | `string`
`lastName` | optional | The user's last name. | `string`
`email` | optional | The user's email. | `string`
`image` | optional | The user's profile image. | `string`
`description` | optional | A brief description about the user (i.e college grade, hobbies, etc.) | `string`
