import json
from stats import Stats

class Player:
    def __init__(self, full_name,   short_name, image_url, url, status):
        self._full_name = full_name
        self._short_name = short_name
        self._image_url = image_url
        self._url = url
        self._status = status
        self._stats = Stats()

    def to_dict(self):
        return {
            'full_name': self.full_name,
            'short_name': self.short_name,
            'image_url': self.image_url,
            'url': self.url,
            'status': self.status,
            'stats': self.stats.to_dict()
        }
    
    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value

    @property
    def short_name(self):
        return self._short_name

    @short_name.setter
    def short_name(self, value):
        self._short_name = value

    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def stats(self):
        return self._stats
    
    @stats.setter
    def stats(self, value):
        self._stats = value
