# initialize all sub-package under /image

from .image.color_models import (
    ColorModel,
    RGBColor,
    BGRColor,
    HSVColor,
    GrayColor
)

from .image import (
    Image,
    NamedWindow
)

from .image.connected_component import (
    ConnectedComponent,
    BBDT8ConnectedComponent,
    RegionProposal,
    Proposal
)

from .image.fillers import (
    Filler,
    FloodFiller
)

from .image.image_factorys import (
    ImageFactory,
    VideoCaptureImageFactory,
    FileImageFactory
)

from .image.image_iterator import (
    ImageIterator,
    NonStoreImageIterator,
    ThreadingImageIterator
)

from .image.image_writers import (
    ImageWriter,
    BlockingImageWriter,
    ThreadingImageWriter
)

from .image.segmentation import (
    ImageSegmenter,
    ChromaKeySegmenter
)

# initialize all sub-package under /bounding_box

from .bounding_box import (
    BoundingBox,
    RectBoundingBox
)

# initialize all sub-package under /lib
from .lib import (
    Point,
    Line,
    Brush,
    BrushFactory
)

# initialize all sub-package under /logger
from .logger import (
    Logger,
    ConsoleLogger
)

# initialize all sub-package under /video
from .video import (
    Video,
    VideoPlayer,
    VideoPlayerState,
    AbstractVideoPlayerState,
    Playing,
    Stopped,
    Closed
)

# initialize all sub-package under /pattern
from .patterns import (
    Singleton
)
