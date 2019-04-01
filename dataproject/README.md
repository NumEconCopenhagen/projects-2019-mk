# Dataproject

Should contain a short introduction to your project, and show how to produce your results.

Needed packages:
pytrends




conda install jupyterlab=0.35 "ipywidgets>=7.2"
set NODE_OPTIONS=--max-old-space-size=4096
jupyter labextension install @jupyter-widgets/jupyterlab-manager@0.38 --no-build
jupyter labextension install plotlywidget@0.8.0 --no-build





virker det hvis man kun bruger:
conda install jupyterlab=0.35 "ipywidgets>=7.2"
set NODE_OPTIONS=--max-old-space-size=4096
jupyter labextension install @jupyterlab/plotly-extension@0.18.2 --no-build
jupyter lab build
set NODE_OPTIONS=
