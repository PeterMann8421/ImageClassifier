from keras.applications.densenet import DenseNet121
from server import*     # native classes for the server

##################################
## inject specific details here ##
##################################

class cDenseNet121(MLModelBase):

    model = DenseNet121(weights=None)

    def __init__(self) ->None:
        super().__init__()

    def load_weights(self, szfilepath):
        self.model.load_weights(szfilepath)

class ProcessImage(ProcessImageBase):

    def __init__(self, args) -> None:
        super().__init__(args)

    @override
    def main_process(self):
        pass
