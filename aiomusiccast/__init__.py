from importlib.metadata import version, PackageNotFoundError

from .musiccast_device import (
    MusicCastDevice,
)
from .musiccast_data import MusicCastData, MusicCastZoneData

from .exceptions import (
    MusicCastException,
    MusicCastConnectionException,
    MusicCastGroupException,
)

from .musiccast_media_content import MusicCastMediaContent

from .features import DeviceFeature, ZoneFeature

try:
    __version__ = version('aiomusiccast')
except PackageNotFoundError:
    __version__ = '(local)'
