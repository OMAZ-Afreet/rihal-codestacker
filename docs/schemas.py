SCHEMA = {
  "openapi": "3.1.0",
  "info": { 
    "title": "CodeStacker API", 
    "version": "1.0.0", 
    "summary": " APIs to upload, parse, and store PDF files", 
    "contact": {
        "name": "Alqasim Alzakwani",
        "email": "q.zak003@gmail.com"
} 
},
  "components": {
    "securitySchemes": {
      "Basic": { "type": "http", "scheme": "basic" }
    }
  },
  "security": [
    {"Basic": []}
  ],
  "servers": [
    { "url": "http://127.0.0.1:8000", "description": "Main server" }
  ],

  "tags": [
    {
      "name": "Account"
    },
    {
      "name": "PDF"
     
    },
    {
      "name": "Search"
     
    }
  ],

  "paths": {
    "/account/sign-up/": {
      "post": {
        "security": [],
        "operationId": "1",
        "tags": ["Account"],
        "summary": "Sign up new account",
        "description": "Use this endpoint to register new account for authenticating the other endpoints.\n\nNote: There is no requirements for valid username and password. Could be anything.",
        "requestBody": {
          "required": True,
          "content": {
            "multipart/form-data": {
              "schema":{
                "type": "object",
                "required": [
                  "username",
                  "password"
                ],
                "properties": {
                  "username": {
                  "type": "string"
                },
                "password": {
                  "type": "string"
                }
                }
              },
              "example": {
                "username": "alqasim",
                "password": "alzakwani"
              }
            },
            "application/json": {
              "schema":{
                "type": "object",
                "required": [
                  "username",
                  "password"
                ],
                "properties": {
                  "username": {
                  "type": "string"
                },
                "password": {
                  "type": "string"
                }
                }
              },
              "example": {
                "username": "alqasim",
                "password": "alzakwani"
              }
            }
            
          }
        },

        "responses": {
          "201": {
            "description": "Account created",
            "content": {
              "application/json": {
              "schema":{
                "type": "object",
                "properties": {
                  "username": {
                  "type": "string"
                }
                }
              },
              "example": {
                "username": "alqasim"
              }
            }
            }
          },

          "400":  {
            "description": "Account creation failed",
            "content": {
              "application/json": {
              "example": {
                "username": ["A user with that username already exists."],
                "password": ["This field is required."]
              }
            }
            }
          }
        }
      }
    },


    "/pdf/upload/": {
      "post": {
        "operationId": "2",
        "tags": ["PDF"],
        "summary": "Upload new PDFs",
        "description": "Use this endpoint to upload PDF files.\n\nNote that you can upload multiple files.",
        "requestBody": {
          "required": True,
          "content": {
            "multipart/form-data": {
              "schema":{
                "type": "object",
                "required": [
                  "file"
                ],
                "properties": {
                  "file": {
                  "type": "array",
                  "items": {
                    "type": "string",
                    "format": "binary"
                  }
                }
                }
              }
            }
            
          }
        },

        "responses": {
          "200": {
            "description": "File/s uploaded",
            "content": {
              "application/json": {
              "example": {
                "success": "file/s uploaded",
                "file/s": [
                  {
                    "file_name": "pfd.pdf",
                    "size": 64723,
                    "parsing_status": "IN PROCESS",
                    "time_of_upload": "SOME-TIME-DATE+TIMEZONE"
                  }
                ]
              }
            }
            }
          },

          "400":{
            "description": "Failed upload",
            "content": {
              "application/json": {
              "example": {
                "error": "file pdf.pdf already exists!",
                
              }
            }
            }
          }
        }
      }
    },

    "/pdf/list/": {
      "get": {
        "operationId": "3",
        "tags": ["PDF"],
        "summary": "List ALL files",
        "description": "Use this endpoint to all files at once.",
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
              "example": [
                    {
                  "id": 14,
                  "file_name": "m.pdf",
                  "size": 129117,
                  "number_of_pages": 8,
                  "time_of_upload": "2023-04-13T14:15:09.885872+04:00"
                  },
                  {
                    "id": 13,
                    "file_name": "H.pdf",
                    "size": 27465,
                    "number_of_pages": 1,
                    "time_of_upload": "2023-04-13T14:07:26.290963+04:00"
                }
              ]
            }
            }
          }
        }
      },

      "post": {
        "operationId": "4",
        "tags": ["PDF"],
        "summary": "Paginate the list",
        "description": "Use this endpoint to list the files with pagination.",
        "requestBody": {
          "content": {
            "application/json": {
              "schema":{
                "type": "object",
                "properties": {
                  "paginate": {
                  "type": "number"
                },
                "page": {
                  "type": "number"
                }
                }
              },
              "example": {
                "paginate": 20,
                "page": 1
              }
            },
            "multipart/form-data": {
              "schema":{
                "type": "object",
                "properties": {
                  "paginate": {
                  "type": "number"
                },
                "page": {
                  "type": "number"
                }
                }
              },
              "example": {
                "paginate": 20,
                "page": 1
              }
            }
          }
        },

        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
              "example": {
                "page": "1 of 10",
                "results": [
                    {
                  "id": 14,
                  "file_name": "m.pdf",
                  "size": 129117,
                  "number_of_pages": 8,
                  "time_of_upload": "2023-04-13T14:15:09.885872+04:00"
                  },
                  {
                    "id": 13,
                    "file_name": "H.pdf",
                    "size": 27465,
                    "number_of_pages": 1,
                    "time_of_upload": "2023-04-13T14:07:26.290963+04:00"
                }
                  ]
              }
            }
            }
          }
        }
      }
    }
  }
  
}
