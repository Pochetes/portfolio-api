# Interests Docs

Contains data about my interests in the technology field and outside of it as well.

## Methods

### `GET` /interests

Gets all interests.

### `POST` /interests

Creates a new interest.

### `GET` /interests/{id}

Gets an interest by id.

### `PUT` /interests/{id}

Updates an interest. Gets an interest by id.

### `DELETE` /interests/{id}

Deletes an interest by id.

## Sample API Response

```json
{
    "_id": {
        "$oid": "61bfced4e9725b992a7e779f"
    },
    "topic": "Artificial Intelligence",
    "image": "public/images/interests/<file_name>"
}
```

## Parameters

### Path Params

Parameter | Required/Optional | Description | Type
------ | -------- | -------- | -------- 
`id` | required | The value for the `Interest` object you want to look up. | `ObjectId`

### Query Params

Parameter | Required/Optional | Description | Type
------ | -------- | -------- | -------- 
`id` | required | The value for the `Interest` object you want to look up. | `ObjectId`
`topic` | optional | The topic that I am interested and/or passionate about. | `string`
`image` | optional | File location of the interest image. | `string`



