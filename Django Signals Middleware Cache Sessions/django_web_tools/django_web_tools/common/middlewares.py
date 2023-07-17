def custom_middleware(get_response):
    def middleware(request, *args, **kwargs):
        response = get_response(*args, **kwargs)

        return response

    return middleware
