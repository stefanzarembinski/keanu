## INSTALLATION

### Add the package to the Python path

To build wheel:

PS .... keanu> python -m build

To install from wheel:

PS .... keanu> pip install dist\keanu-0.1-py3-none-any.whl

To uninstall:

    PS ... > pip uninstall keanu

To install in editable mode:

    PS ... > keanu> pip install -e .

### Set the storage directory of the project according to the forex instrument used

    PS .... keanu> python -m keanu.config

