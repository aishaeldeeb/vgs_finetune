from pytorch_lightning import Trainer
from denseav.data.AVDatasets import AVDataModule
from denseav.shared import create_model_from_cfg
from denseav.train import LitAVAligner  # Ensure this is correctly imported

# Data module configuration
datamodule = AVDataModule(
    dataset_name="VisTex",
    load_size=(224, 224),
    image_aug=True,
    audio_aug=True,
    extra_audio_masking=False,
    audio_model_type="cavmae",
    use_cached_embs=False,
    audio_level=1,
    neg_audio=False,
    data_for_plotting=False,
    use_original_val_set=True,
    use_extra_val_sets=False,
    quad_mixup=False,
    bg_mixup=False,
    patch_mixup=False,
    patch_size=16,
    pytorch_data_dir="/Users/aishaeldeeb/Desktop/VGS/dataset",
    batch_size=8,  # Reduced for sanity check
    num_workers=2  # Reduced for faster checks
)

# Model configuration
aligner = create_model_from_cfg(
    LitAVAligner,
    cfg={
        "code_dim": 512,
        "image_model_type": "dino8",  # Replace based on your repo's requirements
        "audio_model_type": "cavmae",
        "gradient_clipping": 0.1,
        "lr": 0.001,
        "loss_type": "ce",  # Example; replace as needed
        "batch_size": 8,  # Match batch size in the data module
    },
    extra_args={}  # If no extra args are required, provide an empty dictionary
)

# Trainer setup
trainer = Trainer(fast_dev_run=True)  # Short run to verify pipeline
trainer.fit(model=aligner, datamodule=datamodule)
