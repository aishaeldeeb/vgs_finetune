from denseav.data.AVDatasets import VisTexDataset
import torch

dataset = VisTexDataset(root="/Users/aishaeldeeb/Desktop/VGS/dataset", split="train", use_audio=True)
print(f"Number of samples: {len(dataset)}")

for idx, sample in enumerate(dataset):
    print(f"Sample {idx}: {sample.keys()}")
    for key, value in sample.items():
        print(f"  {key}: Type: {type(value)}, Shape/Value: {value.shape if isinstance(value, torch.Tensor) else value}")
    if idx == 5:  # Test only a few samples
        break

