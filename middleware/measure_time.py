import time

class ResponseTimeMeasureMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()

        response = self.get_response(request)

        end = time.time()
        print(f'レスポンスまでの所要時間：{(end-start)*1000}ミリ秒')

        return response