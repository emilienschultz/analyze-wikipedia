from huggingface_hub import hf_hub_download

path = hf_hub_download(
repo_id="omarkamali/wikipedia-monthly",
repo_type="dataset",
filename="20250702.en/train_00016.parquet",
local_dir="../data/raw",
)
print(path)