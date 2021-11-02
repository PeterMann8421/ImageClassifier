
from typing import List
from pydantic import BaseModel

class Image(BaseModel):
    '''Data structure to be populated from request payload JSON'''
    name: str
    data: List[int] = []
    classification: str = None
    
class MLModelBase(object):
    '''Machine learning classifier model abstract base'''
    pass

class ProcessImageBase(object):
    '''Wrapper for the image processing and ML model.
    Inject the image and the ML model'''
    image = None
    ML_model = None

    def __init__(self, args) -> None:
        self.ML_model = args['ML_model'] # is an instance of MLModel
        self.image = args['image']       # is an instance of Image schema

    def pre_process(self):
        pass
    
    def main_process(self):
        '''main processing code for classifier'''
        raise NotImplementedError

    def post_process(self):
        pass

    def get_image(self):
        return self.image

    def classify_image(self):
        '''main driver code for image classification'''
        self.pre_process()
        self.main_process() # override this method
        self.post_process()
        return self.get_image()

def override(f):
    '''decorator to indicate override base method'''
    return f

