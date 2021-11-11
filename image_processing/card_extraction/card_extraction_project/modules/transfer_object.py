from enum import Enum
from typing import List, Tuple
from abstract.dao import DAO


class Point(DAO):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, n):
        return Point(self.x * n, self.y * n)

    def __truediv__(self, n):
        return Point(self.x / n, self.y / n)


class CardConfidence(DAO):
    def __init__(self, card_extraction: float = None, classification: float = None, rotation: float = None):
        super(CardConfidence, self).__init__()
        self.card_extraction = card_extraction
        self.classification = classification
        self.rotation = rotation


class SanityConfidence(DAO):
    def __init__(self, spoof: float = None, id_spoof: float = None, blur: float = None, darkness: float = None, brightness: float = None, cut: float = None):
        super(SanityConfidence, self).__init__()
        self.spoof = spoof
        self.id_spoof = id_spoof
        self.blur = blur
        self.darkness = darkness
        self.brightness = brightness
        self.cut = cut


class TextLineConfidence(DAO):
    def __init__(self, field_extraction: float = None, ocr: float = None):
        super(TextLineConfidence, self).__init__()
        self.field_extraction = field_extraction
        self.ocr = ocr


class TextLine(DAO):
    def __init__(self, coordinates: List[Point] = None, text: str = None, confidence: TextLineConfidence = None,
                 char_confidence: List[float] = None):
        self.coordinates = coordinates if coordinates is not None else []
        self.text = text
        self.confidence = confidence
        self.char_confidence = char_confidence


class FieldInfo(DAO):
    def __init__(self, field: str = None, boxes: List[TextLine] = None):
        self.field = field
        self.boxes = boxes if boxes is not None else []


class CorrectionFieldInfo(DAO):
    def __init__(self, field: str = None, text: str = None, boxes: List[TextLine] = None,
                 confidence: TextLineConfidence = None, char_confidence: List[float] = None):
        self.field = field
        self.text = text
        self.boxes = boxes
        self.confidence = confidence
        self.char_confidence = char_confidence


class Error(Enum):
    NOT_FOUND = 1
    IS_FAKE = 2
    WRONG_ORDER = 3
    WRONG_FORMAT = 4
    IS_SPOOF = 5
    HAS_CUT = 6
    BLUR = 7
    IS_DARK = 8
    IS_BRIGHT = 9
    IMAGE_BAD_QUALITY = 10
    ID_FAKE = 11
    MISMATCHED = 12
    IS_BINARY = 13


class CardInfo(DAO):
    def __init__(self, idx=None, original_image=None, image=None, confidence: float = None,
                 card_confidence: CardConfidence = None, sanity_confidence: SanityConfidence = None,
                 warped_size=None, location: List[Point] = None,
                 card_type: str = None, angle: int = None, info: List[FieldInfo] or List[CorrectionFieldInfo] = None,
                 errors: List[Tuple] = None):
        self.idx = idx
        self.original_image = original_image
        self.image = image
        self.confidence = confidence
        self.card_confidence = card_confidence
        self.sanity_confidence = sanity_confidence
        self.warped_size = warped_size
        self.location = location if location is not None else []
        self.card_type = card_type
        self.angle = angle
        self.info = info if info is not None else []
        self.errors = errors if errors is not None else []
        self.province = None
        self.district = None
        self.precinct = None
        self.street = None
        self.street_name = None
        self.rerun = None
        self.ignore = None
