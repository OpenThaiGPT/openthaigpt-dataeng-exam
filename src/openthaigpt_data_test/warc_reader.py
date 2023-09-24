from .constants import (
    WARC_HEADER_MAPPING,
    RAW_STREAM,
)


def read_warc_file(warc_file: str):
    """
    Description: Convert warc file to huggingface dataset
    Args:
        warc_file: Path to `warc` file
    Returns:
        dataset: Huggingface datasets that contains columns
            `warc_type`, `warc_date`, `warc_record_id`, `contenth_length`,
            `content_type`, `warc_warcinfo_id`, `warc_concurrent_to`,
            `warc_ip_adress`, `warc_target_uri`, `warc_payload_digest`,
            `warc_block_digest`, `warc_identified_payload_type`,
            `warc_truncated`, and `raw_stream`
    """
    return
