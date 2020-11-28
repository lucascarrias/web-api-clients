from requests import Session
import sys

class BaconIpsumClient:
    def __init__(self):
        self.base_url = "https://baconipsum.com/api/"
        self._session = Session()

    def get_bacon(self, params: dict):
        '''
            Parameters:

                type: all-meat for meat only or meat-and-filler for meat mixed with miscellaneous ‘lorem ipsum’ filler.
                paras: optional number of paragraphs, defaults to 5.
                sentences: number of sentences (this overrides paragraphs)
                start-with-lorem: optional pass 1 to start the first paragraph with ‘Bacon ipsum dolor sit amet’.
                format: ‘json’ (default), ‘text’
        '''

        if not params or type(params) is not dict:
            raise RuntimeError(f"You must provide parameters! {self.get_bacon.__doc__}")

        response = self._session.get(self.base_url, params=params)

        try:
            return response.json()
        except:
            return {"error": "Invalid params"}

    @classmethod
    def help(self):
        '''
            The Bacon Ipsum JSON API is a REST interface for generating meaty lorem ipsum text 
            and can be used by any application. Pass in the following parameters using 
            an HTTPS GET and we’ll return a JSON string array of paragraphs.
        '''
        print(self.help.__doc__)


if __name__ == "__main__":
    bacon_client = BaconIpsumClient()