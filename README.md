# Development Guide

## Quick Start

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed accumsan changeme.


## Prepare Your Development Environment

1. Install pyenv so that you can test with different versions of Python

```
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
```

2. Append the following to your ~/.bashrc then log out and log back in

```
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

3. Install development packages

```
sudo apt install build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git
```

4. Install Python 3.5, 3.6 and 3.7

```
pyenv install 3.5.9
pyenv install 3.6.10
pyenv install 3.7.7
```

NOTE: For more available versions, run `pyenv install --list`

5. Create a virtualenv for this project

```
export charm_name=<NAME-OF-YOUR-CHARM>
pyenv virtualenv 3.5.9 ${charm_name}-3.5.9
pyenv local ${charm_name}-3.5.9 3.5.9 3.6.10 3.7.7
```

Your newly created virtualenv should now be activated if your prompt change
to the following:

```
(<NAME-OF-YOUR-CHARM>-3.5.9) ubuntu@dev-18-04-2:/path/to/your/charm$
```

Notice the things in parentheses that corresponds to the virtualenv you created
in the previous step. This is thanks to the coordination of pyenv-virtualenv and
a newly createdd `.python-version` file in the rootdir of this project.

If you `cd ..` or `cd` anywhere else outside your project directory, the virtualenv
will automatically be deactivated. When you `cd` back into the project dir, the
virtualenv will automatically be activated.


## Change All Placeholder Values in the Template

1. Just run the following to get a real-time list of what you need to change

```
make changes
```

## Install The Dependencies

1. Install more development dependencies:

```
make dependencies
```


## Adding A Development Dependency

1. Add it to `dev-requirements.in` and then run make:

```
echo "foo" >> dev-requirements.in
make dependencies
```

This will crate `dev-requirements.txt` and then install all dependencies


2. Commit `test-requirements.in` and `test-requirements.txt`. Both
   files should now be updated and the `foo` package installed in your
   local machine. Make sure to commit both files to the repo to let your
   teammates know of the new dependency.

```
git add dev-requirements.*
git commit -m "Add foo to test-requirements.txt"
git push origin
```


## Adding A Runtime Dependency

1. Add it to `install_requires=` argument of setup() in setup.py and then run:

```
make dependencies
```

This will crate `requirements.txt` and then install all dependencies


2. Commit `setup.py` and `requirements.txt`. Both
   files should now be updated and the `foo` package installed in your
   local machine. Make sure to commit both files to the repo to let your
   teammates know of the new dependency.

```
git add requirements.txt
git add setup.py
git commit -m "Add bar to setup.py"
git push origin
```


## Running All The Tests

1. Ensure you start with a new terminal session because sometimes the shell
   won't find tox immediately after installation.

2. Run:

```
tox
```

## Viewing the Coverage Report

To view the coverage report, run the tests first and then run:

```
make coverage-server
```

This will run a simple web server on port 5000 that will serve the files
in the auto-generated `htmlcov/` directory. You may leave this server running
in a separate session as you run the tests so that you can just switch back
to the browser and hit refresh to see the changes to your coverage down to
the line of code.
