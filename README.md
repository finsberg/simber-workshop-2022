# Lecture notes for Simber coding workshop

## Lecture: Introduction to the cardiac MPS database and analysis package

## Practical: Code design underlying the MPS package and modifying it to your use case

## Building the slides

### Short version: 
Run
```
make lecture
```

### Long version
Slides are built with [`marpit`](https://marpit.marp.app). This is a tool for converting markdown to html.
To build the slides you need to first install `marp` with `yarn` or `npm`, see <https://marpit.marp.app/?id=installation>.

Then you should be able to run
```
marp lecture.md
```
and it will create a new file called `lecture.html` containing the slides. 

## Coding session

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


In [`scripts`](scripts) you will find some python scripts that will be used in the coding session, and the same files can be found as notebooks in the [`notebooks`](notebooks) folder

The python files can be converted to notebooks by running the command 

```
make py2notebooks
```

It is also possible to convert the notebooks to python files by running the command
```
make notebooks2py
```