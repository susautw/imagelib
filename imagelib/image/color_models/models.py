import cv2

from imagelib.image import Image

from imagelib.image.color_models import ColorModel


class BGRColor(ColorModel):
    def number_of_channels(self) -> int:
        return 3

    def to_rgb(self, context: Image) -> Image:
        rgb_data = cv2.cvtColor(context.data, cv2.COLOR_BGR2RGB)
        return Image(rgb_data, RGBColor())

    def to_hsv(self, context: Image) -> Image:
        hsv_data = cv2.cvtColor(context.data, cv2.COLOR_BGR2HSV)
        return Image(hsv_data, HSVColor())

    def to_bgr(self, context: Image) -> Image:
        return context.clone()

    def to_gray(self, context: Image) -> Image:
        gray_data = cv2.cvtColor(context.data, cv2.COLOR_BGR2GRAY)
        return Image(gray_data, GrayColor())


class RGBColor(ColorModel):
    def number_of_channels(self) -> int:
        return 3

    def to_rgb(self, context: Image) -> Image:
        return context.clone()

    def to_hsv(self, context: Image) -> Image:
        hsv_data = cv2.cvtColor(context.data, cv2.COLOR_RGB2HSV)
        return Image(hsv_data, HSVColor())

    def to_bgr(self, context: Image) -> Image:
        bgr_data = cv2.cvtColor(context.data, cv2.COLOR_RGB2BGR)
        return Image(bgr_data, BGRColor())

    def to_gray(self, context: Image) -> Image:
        gray_data = cv2.cvtColor(context.data, cv2.COLOR_RGB2GRAY)
        return Image(gray_data, GrayColor())


class HSVColor(ColorModel):
    def number_of_channels(self) -> int:
        return 3

    def to_rgb(self, context: Image) -> Image:
        rgb_data = cv2.cvtColor(context.data, cv2.COLOR_HSV2RGB)
        return Image(rgb_data, RGBColor())

    def to_hsv(self, context: Image) -> Image:
        return context.clone()

    def to_bgr(self, context: Image) -> Image:
        bgr_data = cv2.cvtColor(context.data, cv2.COLOR_HSV2BGR)
        return Image(bgr_data, BGRColor())

    def to_gray(self, context: Image) -> Image:
        return context.to_rgb().to_gray()


class GrayColor(ColorModel):
    def number_of_channels(self) -> int:
        return 1

    def to_rgb(self, context: Image) -> Image:
        rgb_data = cv2.cvtColor(context.data, cv2.COLOR_GRAY2RGB)
        return Image(rgb_data, RGBColor())

    def to_hsv(self, context: Image) -> Image:
        return context.to_rgb().to_hsv()

    def to_bgr(self, context: Image) -> Image:
        bgr_data = cv2.cvtColor(context.data, cv2.COLOR_GRAY2BGR)
        return Image(bgr_data, BGRColor())

    def to_gray(self, context: Image) -> Image:
        return context.clone()
