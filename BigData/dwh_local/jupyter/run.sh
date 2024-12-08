#!/bin/bash

# Enable the `widgetsnbextension` extension
echo "Enabling widgetsnbextension..."
jupyter nbextension enable --py widgetsnbextension

# Start Jupyter Notebook with specific options
echo "Starting Jupyter Notebook..."
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --NotebookApp.token='' # --notebook-dir=./home/jupyter
