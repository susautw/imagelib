from dataclasses import dataclass
from typing import List, TYPE_CHECKING

from skimage.measure import regionprops

from ...axis import BoundingBox, Point

if TYPE_CHECKING:
    from .. import Image


class RegionProposal:
    def compute(self, label: 'Image') -> List['Proposal']:
        props = regionprops(label.to_numpy())
        return [self._prop_to_proposal(prop) for prop in props]

    @staticmethod
    def _prop_to_proposal(prop) -> 'Proposal':
        min_row, min_col, max_row, max_col = prop['bbox']
        bounding_box = BoundingBox(
                Point(min_col, min_row),
                Point(max_col, max_row)
            )
        return Proposal(prop['area'], prop['perimeter'], bounding_box)


@dataclass(frozen=True)
class Proposal:
    area: int
    perimeter: float
    bounding_box: BoundingBox
