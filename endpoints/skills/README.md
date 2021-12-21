# Skills Docs

Contains data about the technical skills I possess as a Software Engineer.

## Methods

### `GET` /skills

Gets all skills.

### `POST` /skills

Creates a new skill.

### `GET` /skills/{technology}

Gets an skill by technology.

### `PUT` /skills/{technology}

Updates an skill. Gets an skill by technology.

### `DELETE` /skills/{technology}

Deletes an skill by technology.

## Sample API Response

```json
{
    "_id": {
        "$oid": "61bf8e14d8948ee4f35e6c50"
    },
    "technology": "C",
    "image": "public/images/skills/<file_name>"
}
```

## Parameters

### Path Params

Parameter | Required/Optional | Description | Type
------ | -------- | -------- | -------- 
`technology` | required | The name of the programming language or software I know. | `string`

### Query Params

Parameter | Required/Optional | Description | Type
------ | -------- | -------- | -------- 
`technology` | required | The name of the programming language or software I know. | `string`
`image` | optional | File location that the image is stored in. | `string`

*Id is not included because MongoDB automatically generates that for us. Therefore, we can't and do not manipulate it.
