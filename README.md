# Lecture notes for Simber coding workshop

In this repo you will find instructions for how to set up your computer for the coding session as well as the [slides for the MPS database tutorial](lecture.md) and the [notebooks](notebooks) for the coding session.


## Setting up you environment for the coding session


### Installing python

Before installing any packages you need to make sure that you have python installed. You can get a python installer from [python.org/downloads](https://www.python.org/downloads/). You can also install python using a package manager. For example `apt` on Debian, `brew` on Mac and `chocolatey` on Windows. On Windows you can also install python through Microsoft store.

Make sure to check off the tick box where it says "Add python to PATH". That way python will accessible from the command line

### Opening terminal
To run python you first need to open a terminal

#### Windows
Open the start menu and search for `CMD`. `CMD` is the most basic terminal on Windows. Another option is PowerShell which is also usually already installed. I would recommend to install [Windows terminal](https://docs.microsoft.com/en-us/windows/terminal/) which has many more features.

#### Mac
To open a terminal on Mac hit `CMD+SPACE` and type terminal.

#### Linux
If you are running Linux you don't need instructions on how to open a terminal. 

### Testing your python installation

Once you have installed python you should be able to open a terminal and type 
```
python
```
and hit `ENTER`, which should throw you into a python session. Try to execute
```python
import this
```
which should diplay a text that known as the *Zen of python*.


### Installing python packages

Whenever you are working on a python project, you should always install you dependencies in a virtual environment. This is to avoid conflicts with system depedencies

#### Creating a virtual environment
To create a virtual environment execute the following command
```
python -m venv env
```
This will create a new folder called `env` containing a link to python and all your dependencies. If you at some later point mess up your installation you can safely delete this folder and start over again. If you had installed your dependencies on your global system you would be in more trouble.

If you are working on a different project, then you can just make a new virtual environment for example
```
python -m venv env2
```
will make a different folder valled `env2` 

#### Activate a virtual environment
Before you can start using a virtual environnement you need to activate it.

On Unix (Mac and Linux) you can do so using the following command
```
. env/bin/activate
```
(or `env2/bin/activate` if the name of the folder is `env2`).

For Windows, the command is
```
. env\Scripts\activate
```

#### Installing a single package (`cardiac-mps`)
Once you have activated the virtual environment you can install the `cardiac-mps` using the following command
```
python -m pip install cardiac-mps
```
Later in this workshop you need to install a few other packages and you can use a similar command for that (only swap out `cardiac-mps` with the name of the package you want to install).

#### Verify that `cardiac-mps` is installed

To check that the `cardiac-mps` library was installed you should be able to run the following command without any errors
```
python -c "import mps"
```

#### Installing all dependencies for the coding session
All dependencies you need for the coding session is listed in the [`requirements.txt`](requirements.txt). You can install all dependencies listed in the file using the command
```
python -m pip install -r requirements.txt
```

#### Deactivating the virtual environnement
When you are done working in python, or you want to work on another python project you should deactivate the virtual environment. You can do so by executing the command
```
deactivate
```

## Data sources

For the coding session you also need access to some raw data that can be analyzed. This will be provided during the workshop.

In [`scripts`](scripts) you will find some python scripts that will be used in the coding session, and the same files can be found as notebooks in the [`notebooks`](notebooks) folder.

The python scripts and notebooks are the same so use whatever format you prefer.
The python files can be converted to notebooks by running the command 

```
make py2notebooks
```

It is also possible to convert the notebooks to python files by running the command
```
make notebooks2py
```


## Building the slides

The slides for the MPS database tutorial are written in markdown, which is a text format. You can perfectly read the slides on GitHub.

To build the slides (so that they look similar to what was presented), you need to run
```
make lecture
```

This will run a tool called [`marpit`](https://marpit.marp.app) which will convert the markdown file to and html document.
To build the slides you need to first install `marp` with `yarn` or `npm`, see <https://marpit.marp.app/?id=installation>.

Then you should be able to run
```
marp lecture.md
```
and it will create a new file called `lecture.html` containing the slides. 