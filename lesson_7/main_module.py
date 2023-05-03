"""This is my module"""

from time import sleep

from abs_data_classes_module import Post, PostAMessage, SocialChannel
from classes_module import Facebook, PublishProcessor, Twitter, Youtube


def publish_dispatcher(channel: SocialChannel) -> PostAMessage:
    """Func to publish dispatcher"""
    if channel.channel_type == "youtube":
        return Youtube()
    if channel.channel_type == "facebook":
        return Facebook()
    if channel.channel_type == "twitter":
        return Twitter()

    raise TypeError("Unknown social channel")


def main():
    """The main Func"""
    channels = [
        SocialChannel(channel_type="youtube", followers=150),
        SocialChannel(channel_type="facebook", followers=180),
        SocialChannel(channel_type="twitter", followers=160),
    ]
    texts = [
        Post(message="Hello", time_interval=2),
        Post(message="How are you?", time_interval=4),
        Post(message="Goodbye", time_interval=3),
    ]

    for channel in channels:
        publish_channel = publish_dispatcher(channel)
        publish_processor = PublishProcessor(publish_channel)
        publish_processor.connection(channel=channel)
        for text in texts:
            sleep(text.time_interval)
            publish_processor.post_my_message(post=text)
        publish_processor.disconnect(channel=channel)
        print("======================")
        stat_report = publish_processor.get_status()

    print(stat_report)


if __name__ == "__main__":
    main()
