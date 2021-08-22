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
- 
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









