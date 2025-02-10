Env Setup

1. Create Conda env
conda create  -n art_words python=3.10
conda activate art_words

2. Install packages
pip install torch==2.5.1
pip install pandas requests Pillow diffusers transformers streamlit
pip install accelerate


3. Check version:
python -c "import torch; print(torch.__version__)"
python -c "import pandas; print(pandas.__version__)"
python -c "import accelerate; print(accelerate.__version__)"
python -c "import diffusers; print(diffusers.__version__)"