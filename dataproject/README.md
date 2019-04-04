# Dataproject

Should contain a short introduction to your project, and show how to produce your results.

Needed packages:
pip install pytrends
pip install plotly
pip install cufflinks
pip install fix_yahoo_finance



To see the interactive plot the following should be run in the terminal

conda install jupyterlab=0.35 "ipywidgets>=7.2"
set NODE_OPTIONS=--max-old-space-size=4096
jupyter labextension install @jupyter-widgets/jupyterlab-manager@0.38 --no-build
jupyter labextension install plotlywidget@0.8.0 --no-build

Documentation is available at https://github.com/plotly/plotly.py#jupyterlab-support-python-35




virker det hvis man kun bruger:
conda install jupyterlab=0.35 "ipywidgets>=7.2"
set NODE_OPTIONS=--max-old-space-size=4096
jupyter labextension install @jupyterlab/plotly-extension@0.18.2 --no-build
jupyter lab build
set NODE_OPTIONS=


