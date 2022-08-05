# Lecture notes for Simber coding workshop

In this repo you will find the [slides for the MPS database tutorial](lecture.md) and the [notebooks](notebooks) for the coding session.


## Setting up you environment for the coding session

Before the coding session, make sure to create a virtual environment
```
python -m venv venv
```
Activate it

Unix (Linux/MacOSX)
```
. venv/bin/activate
```
Windows
```
. venv\Scripts\activate
```
and install the dependencies

```
python -m pip install -r requirements.txt
```

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