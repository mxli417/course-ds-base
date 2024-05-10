# course-ds-base

## Preparation

### 1. Fork / Clone this repository

```bash
git clone https://github.com/iterative/course-ds-base.git
cd course-ds-base
```


### 2. Create and activate virtual environment

Create virtual environment named `dvc-venv` (you may use other name)
```bash
python3 -m venv dvc-venv
echo "export PYTHONPATH=$PWD" >> dvc-venv/bin/activate
source dvc-venv/bin/activate
```
Install python libraries

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

Add Virtual Environment to Jupyter Notebook

```bash
python -m ipykernel install --user --name=dvc-venv
``` 

Configure ToC for jupyter notebook (optional)

```bash
jupyter contrib nbextension install --user
jupyter nbextension enable toc2/main
```

## 3. Run Jupyter Notebook

```bash
jupyter notebook
```

## 4. synopsis
- don't use WOTs in jupyter NBs
- start from a usable / concise project layout
- modularize the code into a reusable, package(-able) structure and format
- use config files rather than hard-coded config
- structurize the POC / model training code into manageable pipeline stages
- use dvc to track and version trainig data/assets/pipelines 
- use dvc to run and reproduce the pipeline


## 5. Thoughts going through my head

- no linter / import cleanup tools? 
- config management by diverse, folder-dispersed yaml-files? -> hydra?!
- sensitive information in jp-notebooks? -> better use nbstripout instead
- usage of namespace packages: https://docs.python.org/3/reference/import.html#namespace-packages
- relative imports on Windows systems requires careful handling of env vars / thoughts on structure -> better use packaging (as done here)
- why special repo structure and not usage of a widely accepted cookiecutter approach?
- basically only refers to PEP420, but is used here in context simply via grouping code under ./src
- arg parse in stages instead of hydra / other config management packages and/or typer


### 5.1 topic of the envvars + environment setup

- setup of the environment is centered on linux systems only
- tips and hints are linux-specific
- the PYTHONPATH bake-in at environment generation helps to include code seamlessly
- however, for other platforms, this does not work as intended or is not possible
- a more platform-independent solution for managing environment variables is not included 
- a better solution, using a real packaging approach for code-submodules is not included
- open: what is the connection between PYTHONPATH and python / jupyter on linux?
- setting windows system - wide environment variable: https://www3.ntu.edu.sg/home/ehchua/programming/howto/Environment_Variables.html
- setting windows system - wide environment variable w. powershell: https://www.sharepointdiary.com/2021/05/powershell-set-environment-variable.html
- using PYTHONPATH requires manual starts of jupyter w.o. using the VS Code integrated NB viewer / runner

### 5.2. DVC as a versioning and ml workflow management tool

- pip install dvc
- pip install "dvc[s3]" (or [all] to support all remote stages)
- init: dvc init (-> creates .dvc)
- then after the init git add . / git commit -m "init dvc"
- adding changes to dvc works just like with git 
- dvc run -n "name" -d "dependency" -o "outputs" -p "params"
- programmtically: dvc.yaml
    - specifies cmds, params, names, stages and the like
- dvc run is outdated -> use dvc stage add instead
- dvc repro to reproduce the stages
- dvc repro -f to force complete rerun, -s for specific changes

## OT:
- python PEP index: https://peps.python.org/
- python packaging guide: https://packaging.python.org/en/latest/tutorials/packaging-projects/
- visual git explanations: http://marklodato.github.io/visual-git-guide/index-en.html