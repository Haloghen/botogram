"""
    botogram.objects.media
    Representation of media-related upstream API objects

    Copyright (c) 2015 Pietro Albini <pietro@pietroalbini.io>
    Released under the MIT license
"""

from .base import BaseObject
from . import mixins


class PhotoSize(BaseObject, mixins.FileMixin):
    """Telegram API representation of a photo size

    https://core.telegram.org/bots/api#photosize
    """

    required = {
        "file_id": str,
        "width": int,
        "height": int,
    }
    optional = {
        "file_size": int,
    }


class Photo(mixins.FileMixin):
    """Custom representation of a photo

    The current API provided by Telegram for photos sucks, so this tries to
    provide a better one.
    """

    def __init__(self, data, api=None):
        self._api = api
        # Accept only lists of PhotoSize
        if not isinstance(data, list):
            raise ValueError("You must provide a list of PhotoSize")

        # A photo without sizes is nothing
        if len(data) == 0:
            raise ValueError("No sizes passed...")

        # Put all the sizes in an array
        self.sizes = []
        for size in data:
            self.sizes.append(PhotoSize(size, api))

        # Calculate the smaller and the biggest sizes
        with_size = {}
        for size in self.sizes:
            with_size[size.height * size.width] = size
        self.smallest = with_size[min(with_size.keys())]
        self.biggest = with_size[max(with_size.keys())]

        # Publish all the attributes of the biggest-size photo
        attrs = list(PhotoSize.required.keys()) + list(PhotoSize.optional.keys())
        for attr in attrs:
            setattr(self, attr, getattr(self.biggest, attr))

    def set_api(self, api):
        """Change the API instance"""
        self._api = api

        # Set the API on all the photo sizes
        for size in self.sizes:
            size.set_api(api)

    def serialize(self):
        """Serialize this object"""
        result = []
        for size in self.sizes:
            result.append(size.serialize())

        return result


class Audio(BaseObject, mixins.FileMixin):
    """Telegram API representation of an audio track

    https://core.telegram.org/bots/api#audio
    """

    required = {
        "file_id": str,
        "duration": int,
    }
    optional = {
        "performer": str,
        "title": str,
        "mime_type": str,
        "file_size": int,
    }


class Voice(BaseObject, mixins.FileMixin):
    """Telegram API representation of a voice message

    https://core.telegram.org/bots/api#voice
    """

    required = {
        "file_id": str,
        "duration": int,
    }
    optional = {
        "mime_type": str,
        "file_size": int,
    }


class Document(BaseObject, mixins.FileMixin):
    """Telegram API representation of a document

    https://core.telegram.org/bots/api#document
    """

    required = {
        "file_id": str,
    }
    optional = {
        "thumb": PhotoSize,
        "file_name": str,
        "mime_type": str,
        "file_size": int,
    }


class Sticker(BaseObject, mixins.FileMixin):
    """Telegram API representation of a sticker

    https://core.telegram.org/bots/api#sticker
    """

    required = {
        "file_id": str,
        "width": int,
        "height": int,
    }
    optional = {
        "thumb": PhotoSize,
        "file_size": int,
    }


class Video(BaseObject, mixins.FileMixin):
    """Telegram API representation of a video

    https://core.telegram.org/bots/api#video
    """

    required = {
        "file_id": str,
        "width": int,
        "height": int,
        "duration": int,
    }
    optional = {
        "thumb": PhotoSize,
        "mime_type": str,
        "file_size": int,
    }


class Contact(BaseObject):
    """Telegram API representation of a contact

    https://core.telegram.org/bots/api#contact
    """

    required = {
        "phone_number": str,
        "first_name": str,
    }
    optional = {
        "last_name": str,
        "user_id": int,
    }


class Location(BaseObject):
    """Telegram API representation of a location mark

    https://core.telegram.org/bots/api#location
    """

    required = {
        "longitude": float,
        "latitude": float,
    }
