import os
import argparse
from openthaigpt_data_test.warc_reader import read_warc_file
from openthaigpt_data_test.image_caption_extracter import (
    extract_image_caption_from_html,
)
FILE_DIR = os.path.dirname(__file__)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert WARC file to huggingface dataset format."
    )
    parser.add_argument(
        "--warc_file",
        type=str,
        default=f"{FILE_DIR}/../artifacts/CC-MAIN-20230527223515-20230528013515-00000.warc.gz",
        help="Path to WARC file",
    )
    parser.add_argument(
        "--output_path",
        type=str,
        default=f"{FILE_DIR}/../artifacts/preprocess_dataset",
        help="Path to save dataset.",
    )
    parser.add_argument(
        "--num_proc",
        type=int,
        default=os.cpu_count(),
        help="Number of processes.",
    )
    args = parser.parse_args()
    # TODO: Complete pipeline
