# Experiences Docs

Contains data about my work experiences such as internships and jobs.

## Methods

#### `GET` /experiences

Gets all experiences.

#### `POST` /experiences

Creates a new experience.

#### `GET` /experiences/{id}

Gets an experience by id.

#### `PUT` /experiences/{id}

Updates an experience. Gets an experience by id.

#### `DELETE` /experiences/{id}

Deletes an experience by id.

## Sample API Response

```json
{
    "_id": {
        "$oid": "61bfaf49999a6c076f383df8"
    },
    "company": "Meta Platforms Inc.",
    "position": "Software Engineer Intern",
    "dateStarted": "June 2021",
    "dateEnded": "August 2021",
    "image": "<link_to_image>"
}
```

## Parameters

### Path Params

Parameter | Required/Optional | Description | Type
------ | -------- | -------- | -------- 
`id` | required | The value for the `Experience` object you want to look up. | `ObjectId`

### Query Params

Parameter | Required/Optional | Description | Type
------ | -------- | -------- | -------- 
`id` | required | The value for the `Experience` object you want to look up. | `ObjectId`
`company` | optional | The company that I either interned or worked full-time. | `string`
`position` | optional | The type of role I'll be doing at the company (i.e Software Engineer Intern) | `string`
`dateStarted` | optional | Month and year that I started the experience. | `string`
`dateEnded` | optional | Month and year that the experience ended. | `string`
`image` | optional | File location of the company image. | `string`



