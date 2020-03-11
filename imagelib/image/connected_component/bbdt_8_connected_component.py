import cv2

from imagelib.image import Image
from imagelib.image.color_models import GrayColor
from imagelib.image.connected_component import ConnectedComponent


class BBDT8ConnectedComponent(ConnectedComponent):
    def compute(self, image: 'Image') -> 'Image':
        _, data = cv2.connectedComponents(image.to_numpy())
        return Image(data, GrayColor())
