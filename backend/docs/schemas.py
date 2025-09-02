from drf_yasg import openapi

file_param = openapi.Parameter(
    name="image",
    in_=openapi.IN_FORM,
    type=openapi.TYPE_FILE,
    description="Upload an image file (JPG/PNG/WEBP)",
    required=True,
)

binary_output_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "prediction": openapi.Schema(type=openapi.TYPE_BOOLEAN, example=True),
        "confidence": openapi.Schema(type=openapi.TYPE_NUMBER, format="float", example=0.87),
    },
    required=["prediction", "confidence"],
)

character_output_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "character": openapi.Schema(type=openapi.TYPE_STRING, enum=["Goten", "Goku"], example="Goten"),
        "confidence": openapi.Schema(type=openapi.TYPE_NUMBER, format="float", example=0.91),
    },
    required=["character", "confidence"],
)

binary_response_schema = openapi.Response("Binary classification result", binary_output_schema)
character_response_schema = openapi.Response("Character classification result", character_output_schema)

error_output_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "error": openapi.Schema(type=openapi.TYPE_STRING, example="Error message here"),
    },
    required=["error"],
)

unsupported_format_response = openapi.Response(
    description="Unsupported media type",
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "error": openapi.Schema(
                type=openapi.TYPE_STRING,
                example="Unsupported image format. Allowed formats: JPG, PNG, WEBP."
            )
        },
        required=["error"],
    ),
)

bad_size_response = openapi.Response(
    description="Image size outside allowed bounds",
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "error": openapi.Schema(
                type=openapi.TYPE_STRING,
                example="Minimum 100x100px; got 80x60px"
            )
        },
        required=["error"],
    ),
)

internal_error_response = openapi.Response(
    description="Internal server error",
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "error": openapi.Schema(
                type=openapi.TYPE_STRING,
                example="Unexpected error while processing the image"
            )
        },
        required=["error"],
    ),
)

binary_responses = {
    200: binary_response_schema,
    400: bad_size_response,
    415: unsupported_format_response,
    500: internal_error_response,
}

character_responses = {
    200: character_response_schema,
    400: bad_size_response,
    415: unsupported_format_response,
    500: internal_error_response,
}
