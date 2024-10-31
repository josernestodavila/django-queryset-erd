import importlib.metadata

from .generator import generate_erd_from_queryset


try:
    __version__ = importlib.metadata.version(__name__)
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"

