class SampleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('サーバー起動のときのみ')

    def __call__(self, request):
        print('1: リクエストがviews.pyで処理される前')

        response = self.get_response(request)

        print('2: リクエストがviews.pyで処理された後')

        return response