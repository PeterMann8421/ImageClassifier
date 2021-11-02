from fastapi import FastAPI, status, Response
import uvicorn
from dn121 import cDenseNet121, ProcessImage # import native classes

Classifier = cDenseNet121() # create a ML model to classify the image
app = FastAPI()             # create the server

@app.on_event("startup")
async def startup_event() -> None:
    '''Load trained model weights into classifier model.'''
    Classifier.load_weights(szfilepath="data/densenet121_weights_tf_dim_ordering_tf_kernels.h5")

@app.post('/test_predict')
async def post_test_predict(response: Response):
    '''test function to ensure classifier is working'''
    pass

@app.post('/predict')
async def post_predict(pbuf, response: Response):
    '''Request pbuf contains the image to be processed.'''
    try:
        # assume that the payload of the request is the image data
        image_instance = pbuf["image"]

        # insert the image and the model into a handler and classify.
        # This modifies the members of image_instance in-place
        args = {"image": image_instance, "ML_model": Classifier}
        ProcessImage(args).classify_image()

        # return the classified result 
        result = {"response": image_instance.classification}
        response.status_code=status.HTTP_200_OK

    except KeyError:
        result = {"response":f"Incorrect request packet"}
        response.status_code=status.HTTP_400_BAD_REQUEST

    except (...) as e: # TO:DO - better error handling
        result = {"response":f"Error during request"}
        response.status_code=status.HTTP_500_INTERNAL_SERVER_ERROR

    return result

if __name__ == "__main__": 
    uvicorn.run(app, port=5000)