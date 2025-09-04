import config

TORTOISE_ORM = {
    "connections": {"default": config.database_url},
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
