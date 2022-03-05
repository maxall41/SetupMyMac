# Welcome

## Configuring Custom app NAS

To use custom apps inside of your nas create a folder path called `Utils/apps` then inside of that folder place your `.dmg` files for your apps.
The name of your .dmg files has to be in this format:
```
ImageName OTHER
```
Where ImageName is the name of the volume that will be mounted when the `.dmg` file is mounted you can put anything after that as long as it is seperated by a space

## Installation

### One command install
```
curl -sSL setup.maxc.codes | bash
```
### Manual

IMPORTANT: ⚠️ If using Manual install make sure to run this in your `Downloads` directory ⚠️

```python3 run.py```
or if that fails
```python run.py```
