"""This is my classes module"""

from abs_data_classes_module import Post, PostAMessage, SocialChannel


class Youtube(PostAMessage):
    """This is Youtube Class"""

    def __init__(self):
        self.account_name = None
        self.password = None

    def connection(self, channel: SocialChannel):
        print(f"Connected to {channel.channel_type} channel established")

    def _get_name(self):
        if self.account_name is None:
            self.account_name = input("What`s the name on Youtube: ")
        return self.account_name

    def _get_password(self):
        if self.password is None:
            self.password = input("What`s the password on Youtube: ")
        return self.password

    def _send_callback_api(self, acc_name: str, password: str):
        if password == "123":
            print(f"Authorizing with account: {acc_name} on Youtube.")
        else:
            raise NameError("Wrong username or password")

    def authorize(self) -> bool:
        """Func to authorize in Youtube"""
        acc_name = self._get_name()
        password = self._get_password()
        self._send_callback_api(acc_name, password)
        return True

    def post_a_message(self, post: Post):
        print(f"The message '{post.message}' is published on Youtube")

    def disconnection(self, channel: SocialChannel):
        """Func to disonnect from Youtube"""
        print(f"Disonnect from {channel.channel_type} channel.")

    @property
    def status(self):
        if getattr(self, "_status", False):
            return "FAILED"
        return "STATUS: SUCCESS"


class Facebook(PostAMessage):
    """This is Facebook Class"""

    def __init__(self):
        self.account_name = None
        self.password = None

    def connection(self, channel: SocialChannel):
        print(f"Connected to {channel.channel_type} channel established")

    def _get_name(self):
        if self.account_name is None:
            self.account_name = input("What`s the name on Facebook: ")
        return self.account_name

    def _get_password(self):
        if self.password is None:
            self.password = input("What`s the password on Facebook: ")
        return self.password

    def _send_callback_api(self, acc_name: str, password: str):
        if password == "123":
            print(f"Authorizing with account: {acc_name} on Facebook.")
        else:
            raise NameError("Wrong username or password")

    def authorize(self) -> bool:
        """Func to authorize in Facebook"""
        acc_name = self._get_name()
        password = self._get_password()
        self._send_callback_api(acc_name, password)
        return True

    def post_a_message(self, post: Post):
        print(f"The message '{post.message}' is published on Facebook")

    def disconnection(self, channel: SocialChannel):
        """Func to disonnect from Facebook"""
        print(f"Disonnect from {channel.channel_type} channel.")

    @property
    def status(self):
        if getattr(self, "_status", False):
            return "FAILED"
        return "STATUS: SUCCESS"


class Twitter(PostAMessage):
    """This is Twitter Class"""

    def __init__(self):
        self.account_name = None
        self.password = None

    def connection(self, channel: SocialChannel):
        print(f"Connected to {channel.channel_type} channel established")

    def _get_name(self):
        if self.account_name is None:
            self.account_name = input("What`s the name on Twitter: ")
        return self.account_name

    def _get_password(self):
        if self.password is None:
            self.password = input("What`s the password on Twitter: ")
        return self.password

    def _send_callback_api(self, acc_name: str, password: str):
        if password == "123":
            print(f"Authorizing with account: {acc_name} on Twitter.")
        else:
            raise NameError("Wrong username or password")

    def authorize(self) -> bool:
        """Func to authorize in Twitter"""
        acc_name = self._get_name()
        password = self._get_password()
        self._send_callback_api(acc_name, password)
        return True

    def post_a_message(self, post: Post):
        print(f"The message '{post.message}' is published on Twitter")

    def disconnection(self, channel: SocialChannel):
        """Func to disonnect from Twitter"""
        print(f"Disonnect from {channel.channel_type} channel.")

    @property
    def status(self):
        if getattr(self, "_status", False):
            return "FAILED"
        return "STATUS: SUCCESS"


class PublishProcessor:
    """Publish Processor class"""

    def __init__(self, post_a_message: PostAMessage):
        self._post_message = post_a_message

    def connection(self, channel: SocialChannel):
        """Func to connect and authorize user"""
        self._post_message.connection(channel)
        self._post_message.authorize()

    def post_my_message(self, post: Post):
        """Func to post a messages"""
        self._post_message.post_a_message(post)

    def disconnect(self, channel):
        """Func to disconnect users"""
        self._post_message.disconnection(channel)

    def get_status(self):
        """Func to get status"""
        return self._post_message.status
