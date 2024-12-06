# DenseAV Fine-Tuning with Custom VisText Dataset

## Project Overview
This project extends the DenseAV model by adding a custom subclass to its dataset handling class, allowing the model to be fine-tuned on a dataset derived from VisText. The subclass is designed to process both visual and audio components from the VisText dataset for improved attention visualization.

## Requirements

- Python 3.x
- PyTorch (compatible with CUDA)
- torchaudio
- torchvision
- numpy
- matplotlib

Install dependencies with:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Project Structure

\`\`\`
/project-root
├── /dataset_root
│   ├── /train
│   ├── /val
│   ├── /test
│   ├── data.json
│   ├── *.wav  (audio files)
│   ├── *.png  (image files)
│   └── *.npy  (additional data)
├── /models
├── /scripts
└── README.md
\`\`\`

## Custom Dataset Subclass

The main contribution is the addition of a subclass `VisTextDataset` in the `datasets.py` file, extending the base `DenseAVDataset` class. This subclass processes the custom VisText dataset, including both images and TTS-generated audio files, along with their associated metadata.

### Key Updates:
- `VisTextDataset` subclass added to `datasets.py` for handling custom data.
- Adapts the dataset preprocessing pipeline to work with visual, audio, and metadata components from VisText.

## Fine-Tuning the Model

To fine-tune the DenseAV model with your custom dataset, run the following script:

\`\`\`bash
python train.py
\`\`\`

This will initiate the training process using your custom dataset, allowing you to fine-tune the model for attention visualization tasks.
