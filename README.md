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
- DS blueprint is also mentioned: https://data-science-blueprint.readthedocs.io/en/latest/presentation/schema.html



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
- automated versioning of dvc pipeline outputs

### 5.3. DVC data management under the hood

- DVC creates md5 hashes of files and checks if they already are tracked and their metadata already exists
- the tracked files are saved into the DVC (project) cache directory
- removes the original file from the working directory
- creates a reflink / symlink to the working directory
- saves metadata information to file.csv.dvc
- works similar with directories
- dvc status, dvc checkout available
- manual checkout also the associated git commits
- dvc checkout:
    - helps in checking out local remote files
    - but no version / branch naming?! -> bc. it should be associated with specific git branches and associated .lock - files
    - adds additional source of errors if people miss out on running checkout after git checkout
- dvc get to download files from a remote only
- dvc import to add remote storages into the data versioning & enable tracking of new data


### 5.4. Comparing experiments, plotting and metrics tracking with dvc

- need specific lines in the dvc.yaml, not as straightforward as mlflow, for example
- allows versioning differences in metrics / tracking
- plotting functions can handle csv files and also be used to generate the diff between different runs
- handy, but need a hand-specified underlying template for specific data sources
- everything beyond base templates comes with extra work
- dvc then takes the template and the source & generates html pages from that
- these can be stored as png/jpg files & compared 
- dvc can also help tracking model training checkpoints, integrated code and config changes
- using the `--live` flag enables dvc-live tracking of the model training progress (especially helpful in deep learning scenarios)
- this also needs new lines importing dvclive, for example in the training scripts, as well as epoch start/stop tasks
- details for model training progress tracking (esp. training time, etc.) -> not on the branche of the og training repo?!
- DVC Studio -> setup howto? 
    - create account
    - 

### 5.5. Experiments management and collaboration

- dvc also allows cml-style -S --set-params to edit the params.yaml file with dvc exp ("experiment")
- users can trigger different runs with that, instead of using dv repro to only run specific sections under changes
- hence, dvc also supports hydra-style overrides, including jobs, queuing, etc.
- also allows parallel, sequential job working
- dvc exp show --include-params=featurize
- dvc exp branch + ID + name -> creates a new branch with git
- dvc exp apply + ID -> gets a particular experiment into the current workspace






## OT:
- python PEP index: https://peps.python.org/
- python packaging guide: https://packaging.python.org/en/latest/tutorials/packaging-projects/
- visual git explanations: http://marklodato.github.io/visual-git-guide/index-en.html
- git explanation: https://www.youtube.com/watch?v=P6jD966jzlk