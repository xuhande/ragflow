#!/usr/bin/env python3

from huggingface_hub import snapshot_download
import nltk
import os

repos = [
    "InfiniFlow/text_concat_xgb_v1.0",
    "InfiniFlow/deepdoc",
    "BAAI/bge-large-zh-v1.5",
    "BAAI/bge-reranker-v2-m3",
    "maidalun1020/bce-embedding-base_v1",
    "maidalun1020/bce-reranker-base_v1",
]

def download_model(repo_id):
    local_dir = os.path.abspath(os.path.join("huggingface.co", repo_id))
    os.makedirs(local_dir, exist_ok=True)
    snapshot_download(repo_id=repo_id, local_dir=local_dir)


if __name__ == "__main__":
    local_dir = os.path.abspath('nltk_data')
    for data in ['wordnet', 'punkt', 'wordnet']:
        print(f"Downloading nltk {data}...")
        nltk.download(data, download_dir=local_dir)
    for repo_id in repos:
        print(f"Downloading huggingface repo {repo_id}...")
        download_model(repo_id)