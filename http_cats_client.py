from requests import Session, Response


class HttpCatsClient:
    def __init__(self):
        self.base_url = "https://http.cat/"
        self._session = Session()

    def status(self, code):
        return self._session.get(self.base_url+str(code)).content

    def status_from_url(self, url: str):
        response = self._session.get(url)
        return self.status(response.status_code)
        
if __name__ == "__main__":
    http_cat = HttpCatsClient()

    print(http_cat.status(451))