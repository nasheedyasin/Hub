from .codec import Codec
import numpy
import pickle

class DefaultCodec(Codec):
    def __init__(self):
        super().__init__()

    def encode(self, array: numpy.ndarray) -> bytes:
        info = {}
        info['shape'] = array.shape
        info['dtype'] = array.dtype
        info['data'] = array.tobytes()
        return pickle.dumps(info)

    def decode(self, bytes: bytes) -> numpy.ndarray:
        info = pickle.loads(bytes)
        return numpy.frombuffer(info['data'], dtype=info['dtype']).reshape(info['shape'])