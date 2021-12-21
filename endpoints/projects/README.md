# Projects Docs

Contains data about my software-related projects that I have been working during my engineering career.

## Methods

### `GET` /projects

Gets all projects.

### `POST` /projects

Creates a new project.

### `GET` /projects/{id}

Gets an project by id.

### `PUT` /projects/{id}

Updates an project. Gets an project by id.

### `DELETE` /projects/{id}

Deletes an project by id.

## Sample API Response

```json
{
    "_id": {
        "$oid": "61bfd2c624af618a810eae2b"
    },
    "title": "Navi Web Companion",
    "description": "A Google Chrome extension",
    "image": "public/images/projects/<file_name>",
    "link": "https://www.github.com/..."
}
```

## Parameters

### Path Params

Parameter | Required/Optional | Description | Type
------ | -------- | -------- | -------- 
`id` | required | The value for the `Project` object you want to look up. | `ObjectId`

### Query Params

Parameter | Required/Optional | Description | Type
------ | -------- | -------- | -------- 
`id` | required | The value for the `Project` object you want to look up. | `ObjectId`
`title` | optional | The title of the project I am/was working on. | `string`
`description` | optional | A brief description of what the project does. | `string`
`image` | optional | An image of a certain feature in the project. | `string`
`link` | optional | A link to the project's Github repository. | `string`


