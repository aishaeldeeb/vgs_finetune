# Project Overview

This is a part of this [project]()

## Objective: 
Extend the [DenseAV](https://github.com/mhamilton723/DenseAV) codebase by introducing a custom dataset handling subclass to fine-tune the model on a dataset derived from VisText.


## Custom Dataset Subclass
The main contribution is the addition of a subclass `VisTextDataset` in the `datasets.py` file, extending the base `DenseAVDataset` class. This subclass processes the custom VisText dataset, including both images and TTS-generated audio files, along with their associated metadata.

### Key Updates:
- `VisTextDataset` subclass added to `datasets.py` for handling custom data.
- Adapts the dataset preprocessing pipeline to work with visual, audio, and metadata components from [VisText](https://vis.csail.mit.edu/vistext/).

---

## Dataset Structure
```
/dataset_root
- /audio
- /frames
- test_data.json
- train_data.json
- validation_data.json
```


## Fine-Tuning the Model
To fine-tune the DenseAV model with your custom dataset, run the following script:

```bash
python train.py
```

This will initiate the training process using your custom dataset, allowing you to fine-tune the model for attention visualization tasks.

## References

- Hamilton et al., 2024: [DenseAV GitHub Repository](https://github.com/mhamilton723/DenseAV)

## License

This tool is open-source under the MIT License.

This incorporates portions of the DenseAV codebase, which is also licensed under the MIT License. For details, see the original [DenseAV License](https://github.com/mhamilton723/DenseAV/blob/main/LICENSE).
