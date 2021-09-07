# REST API Design

## API Basics
- `API`: A set of clearly defined methods of communication among various components
- `Web API`: An API exposed by a web component, allowing other components to interact with it.
  - Platform agnostic
  - Use standard protocols over HTTP
  - Usually Request/Response based
  - `SOAP`: XML based, RPC style
  - `REST`: 
    - Representational State Transfer, URL + JSON based, message style protocol
    - REST API enables transfer of representation of a resource's state.
  - `GraphQL`: Enables very flexible querying, updating and subscribing to data changes, JSON input & output
  - `gRPC`: Uses HTTP/2, Protobuf, supports bi-directional & streaming messaging
## HTTP Verbs
- Set the action to be performed
  - Retrieve a resource
  - Add a resource
  - Update a resource
  - Delete a resource

| Verb | Role | Body? | Params In |
| --- | --- | --- | --- |
| GET | Retrieve resource(s) | No | URL |
| POST | Add resource(s) | Yes | Body |
| PUT | Modify resource(s) | Yes | Body |
| DELETE | Delete resource(s) | No | URL |
### GET
- Used to retrieve resources
- Never use it to add/update/delete resources
- GET is the default verb of the browser's address bar
- Usually combined with parameters
- GET request should not include body
### POST
- Used to add resource
- Should contain a message body that specifies the resource to be added
- Should not contain query string parameters
### PUT
- Used to modify the resource
- Should contain a message body that specifies the resource to be modified
- Should not contain query string parameters
- What happens if the resource to modify does not exist
  - The spec states a new resource should be created
  - use your own discretion
  - PUT is idempotent
### DELETE
- Used to delete the resource
- Never use it to add/update/retrieve resources
- Almost always combined with parameters
- Should not include body
### Additional Verbs
- `PATCH`: Similar to PUT, but with partial updates
- `HEAD`: Same as GET, but without the body in the response, can be used as a pre-check to check if an entity exists
- `OPTIONS`: Describes the available verbs for the URL
## URL Structure
- defines the structure of the api's url
- Should be self explanatory, consistent across the API, predictable
### Domain name
- Protocol should be HTTPS
- For FQDN(fully qualified domain name) - should have `api` in its name
- https://api.myapp.com
### The API word
- If the domain does not include `api`, it comes now
- https://www.myapp.com/api
- emphasizes that this URL is for the API, not the website
### Version
- If the version strategy is URL, it comes now
- only natural number - positive, no decimals
- could be prefixed with `v`
### Entity
- REST deals with resources, or entities
- The next part is the entity we're dealing with
- Should be one word, no more
- NEVER a verb, only nouns
  - HTTP verb provides the verb/action
### ID Parameter
- when dealing with a specific entity, next is the entity id
- The ID is part of the URL
- /api/v1/order/17
- Relevant for GET, PUT, DELETE
### Sub entity
- Used for accessing entities that are dependant on other entities
- Example: Get all the items of order no. 17
- Sub entity should come after the ID parameter
- /api/v1/order/17/items
### Query parameters
- Used to query the entities in GET method
- Come at the end of the URL, after `?`
- Concatenated with `&`
  - /api/v1/orders?fromDate=12/12/2018&toDate=2/2/2019

| | Query parameters | ID parameter |
| --- | --- | --- |
| Location | At the end of the URL | End or middle of the URL |
| Param count | 0..N parameters | 1 parameter |
| Example| /api/v1/orders/?user=john | /api/v1/order/17 |
| Return value | may return 0..N entities | must return exactly 1 entity |
| If not found | That's fine | Error |
### Singular Vs Plural
- Best practice: always prefer readability and ease of use
  - When the API returns a single entity, use singular
  - When the API returns multiple entities, use plural
## Response Codes
- Notify clients about the status of the request
  - Did it succeed?
  - Did it fail? why?
  - What kind of error?
- Return the appropriate status code
- Use the most common codes:
  - 200 OK, 201 Created, 204 No content, 400 Bad request, 404 Not Found, 500 Internal Server Error
### Response Code Groups
- Five groups
- Each group represent specific response type
- Each group consists of 3 digits status code
- Groups
  - 1xx - Informational response
  - 2xx - Success
  - 3xx - redirection
  - 4xx - Client errors
  - 5xx - Server errors
### 200 - OK
- The default status code
- The request was successful
- With GET: returns the entities requested
- With POST: returns the entities created
### 201 - Created
- The request has been fulfilled, a new entity has been created
- Response might contain `Location` header pointing to the entity
- This is the expected status code of POST request
### 202 - Accepted
- The request has been accepted and is pending processing
- Processing might not be complete
- No notification is given when processing completes
- Usually used for POST, PUT requests
### 204 - No content
- Request was fulfilled but no content was sent back
- Should NOT include body
- used mainly when updating large entity
- The 204 no content Vs 200 OK dilemma
  - what should be returned when a GET returns no entity?
  - 200 with no body, or 204?
  - No agreed upon answer, better to avoid 204 and stick to 200
### 400 - Bad request
- The client sent a bad request
  - Parameters can't be validated (ie negative age)
  - JSON can't be parsed
- Used with all verbs
- Consider using RFC 7807 - Problem details
  - Standard for returning machine-readable data about the problem
### 401 - Unauthorized
- The client is not authorized to access the entity
- Authorization is required
- Not to be confused with 403 - Forbidden
### 403 - Forbidden
- The client is not authorized to access the entity
- Authorization failed
- 401 - I don't know who you are
- 403 - I know who you are and this action is forbidden for you
### 404 - Not Found
- The entity specified in the request was not found
- used when a specific entity was looked for (with id parameter), not with query parameter
- Used with all verbs
### 500 - Internal Server Error
- Something bad happened while processing the request
- Client can do nothing about it
- Used with all verbs
### Additional codes
- 207 - Multi-status:
  - Used for cases where multiple entities are handled, each has its own status
## Response Codes Cheat Sheet

| Verb | Relevant Codes | Description |
| --- | --- | --- |
| GET | 200 OK | Content was found and returned |
| | 400 Bad Request | There was an error validating the parameters sent |
| | 401 / 403 | Authorization required / Not authorized |
| | 404 Not Found | Entity not found |
| POST | 200 OK | The request was completed successfully |
| | 201 Created | The entity was added successfully |
| | 202 Accepted | The request was received and is pending processing |
| | 204 No Content | The request was completed successfully, but the server has nothing to send back |
| | 400 Bad Request | There was an error validating the parameters sent |
| | 401 / 403 | Authorization required / Not authorized |
| | 404 Not Found | Entity not found. Relevant when adding sub-entity to a specific entity, using the ID Parameter |
| PUT | 200 OK | The request was completed successfully |
| | 202 Accepted | The request was received and is pending processing |
| | 204 No Content | The request was completed successfully, but the server has nothing to send back |
| | 400 Bad Request | There was an error validating the parameters sent |
| | 401 / 403 | Authorization required / Not authorized |
| | 404 Not Found | Entity to update not found. Relevant also when updating subentity of a specific entity, using the ID Parameter |
| DELETE | 200 OK | Content was found and deleted |
| | 400 Bad Request | There was an error validating the parameters sent |
| | 401 / 403 | Authorization required / Not authorized |
| | 404 Not Found | Entity to delete not found |
## API Definition File
- File that describes all the things you can do with an API
- Lists every request you can make
- Tells you how to make that request
- Tells you what the response will look like
### What's in an API Definition File?
- Server location
- How security is handled (authorization)
- All the available requests in that API
- All the different data you can send in a request
- what data is returned
- What HTTP status codes can be returned
#### Response body
- The response body is included in a response object
- The response object has a achema to describe the structured data.
- You can have a separate response object for each HTTP status code returned.
#### Security
- Authentication and authorization
- can be:
  - None
  - Basic Auth: username and password
  - API key: using a valid API key to gain access
  - OAuth
## API Versioning
- Set version support policy
- Include versioning in the API
- Version can be in the URL, in the header or in a query parameter
- Keeping the version in the header is the most correct form
  - adheres to the REST principles
- URL is the most common and easiest to implement
## Authentication and Authorization
- Authentication: who is the user
- Authorization: what is the user allowed to do

## Open API Specification
- The Open API Specification uses structured data for its API definition files.
- `YAML`:
  - `|` means preserve lines and spaces
  - `>` means fold lines
### Open API Specification File
```yml
swagger: "2.0"

# document metadata
info:
  version: "0.0.1"
  title: Example Service

host: api.example.com
basePath: /photo
schemes:
  - https

# Endpoints
paths:
  # example with query parameters
  /album:
    get:
      parameters:
        - name: start
          in: query
          required: false
          type: string
        - name: end
          in: query
          required: false
          type: string
  # example with path parameter
  /album/{id}:
    get:
      parameters:
        - name: id
          in: path
          required: true
          type: integer
```
### Data Types
- boolean
- integer
- number
- string
- array
### Custom headers
- Custom headers are treated as parameters
- Standard headers(authorization, content format) are handled elsewhere
```yml
- name: Access-level
  in: header
  required: false
  type: string
```

## Swagger Tools
- Swagger Editor: 
  - Helps you write OAS files
  - https://editor.swagger.io/
- Swagger CodeGen: Generates code in popular languages for using your API
- Swagger UI: Generates documentation from OAS files
- SwaggerHub: Hosted platform for designing and documenting APIs