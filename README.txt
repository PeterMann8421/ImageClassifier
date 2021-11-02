
Hello! 

Please find enclosed a small Restful API built using FASTAPI and associated backend files.
There is also a requirements.txt file.

The source code is contained within the `source` directory and consits of 3 files:

** main.py **

        Contains the api code. On startup, loads into memory a pre-trained DenseNet121 Image Classifier 
        model from a known file location.

        The api contains a POST routine that pipes the image data to be processed by the classifier.
        There is also a test routine to be written.

** server.py **

        Contains the backend code that is called by the API to handle the classification. A data schema 
        has been chosen for the image data and abstract base classes have been created for the model and the 
        processing task.

** dn121.py ** 

        Implements the overrides of the base classes for the DenseNet121 classifier. 

Future work:
        Implement the client

        Implement the backend details of the image classifier.

        Allow asynchronous dispatch to process multiple images at one time. Perhaps via a seperate POST image
        routine that uploads an image to a cache on the server. The server can then classify images in this cache
        by a queue.

        Allow retraining of the weights based on uploaded images.

        Collect API into a buildpack to create image for cloud deployment including (OS, Python runtime, pip requirments ...)