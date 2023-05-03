"""This is my module of abstractclass and dataclasses"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class SocialChannel:
    """Dataclass created Social Channel"""

    channel_type: str
    followers: int


@dataclass
class Post:
    """Dataclass created Post"""

    message: str
    time_interval: int

    def __str__(self):
        return f"Post: {self.message}: across {self.time_interval}"


class PostAMessage(ABC):
    """Abstract class for connect, authorize, sending
    and disconnect with social channel"""

    @abstractmethod
    def connection(self, channel: SocialChannel):
        """Function to connection to Social Channel"""

    @abstractmethod
    def authorize(self):
        """Func to authorize in Youtube"""

    @abstractmethod
    def post_a_message(self, post: Post):
        """Function to post a message"""

    @abstractmethod
    def disconnection(self, channel: SocialChannel):
        """Function to disconnect from Social Channel"""

    @property
    @abstractmethod
    def status(self):
        """Represents the sending status of a message."""
