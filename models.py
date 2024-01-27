# schema description
contact_schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "object",
            "properties": {
                "first name": {"type": "string"},
                "last name": {"type": "string"}
            },
            "required": ["first name", "last name"]
        },
        "email": {"type": "string"},
        "code": {"type": "string"},
        "number": {"type": "string"},
        "address": {
            "type": "object",
            "properties": {
                "country": {"type": "string"},
                "city": {"type": "string"},
                "address": {"type": "string"}
            },
        }
    },
}
