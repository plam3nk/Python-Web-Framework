def custom_middleware(get_response, *args, **kwargs):
    response = get_response(*args, **kwargs)

    return response