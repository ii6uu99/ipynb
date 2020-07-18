# pyv
 Simple Batch CLI to automate some of Windows Python Virtual Environment Management

## Basic Manual Setup

- Move file to permanent directory
- Add directory location to Windows user ```path``` Environment Variable

## Usage

### Create or activate python virtual environment

- Open cmd in target directory for the virtual environment
- Input ```pyv```
- pyv will activate or setup an environment:
    - If a python virtual environment exists named ```venv``` pyv will activate that environment
    - If not python virtual environment exists pyv will perform the following:
        - Create a python virtual environment named ```venv```
        - Activate the new virtual environment
        - Upgrade pip to the latest version
        - If a requirements.txt file is present, pyv will install specified dependencies

### Delete python virtual environment

- Open cmd in target directory
- Input ```pyv delete```
- If a python virtual environment directory exists named ```venv``` pyv will delete the directory

### Help

- Open cmd
- Input ```pyv help```
- pyv will show a simple help prompt