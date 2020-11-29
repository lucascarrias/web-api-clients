from requests import Session
import os

class DetectLanguageClient:
    '''
        Language detection webservice analyzes provided text and returns identified language code with score. 
    '''

    def __init__(self, token: str):
        self._token = token
        self.base_url = "https://ws.detectlanguage.com/0.2"

        self._session = Session()
        self._session.headers.update({'Authorization' : f"Bearer {token}"})

    def user_status(self):
        return self._session.get(self.base_url+"/user/status").json()

    def language_list(self):
        return self._session.get(self.base_url+"/languages").json()

    def detect_language(self, *content):
        params_key = "q[]" if len(content) > 1 else "q"   
        return self._session.post(self.base_url+"/detect", params={params_key:content}).json()


if __name__ == "__main__":
    dl_client = DetectLanguageClient(os.getenv("TOKEN"))