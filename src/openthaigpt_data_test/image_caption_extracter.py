from .constants import (
    RAW_STREAM,
    WARC_TARGET_URI,
    IMAGE_CAPTION,
    IMAGE_URL,
)


def extract_image_caption_from_html(batch):
    """
    Description: Add `image_caption` and `image_url` to dataset
    """
    return batch
