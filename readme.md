# Effective Testing

This is a simple web app intended to practice test automation.

NOTE:
Given this application is built using Python 2.7 and since 2020 this version is [not longer supported](https://www.python.org/doc/sunset-python-2/), 
a refactor is needed to move it to Python 3.


### Installing
If you want to run this application locally: 
* Install Python 2.7.9.
* Clone this repository
```
$ git clone https://github.com/MarceloCorpucci/effective-testing.git
```
* Install dependencies
```
$ pip install -r requirements.txt
```
* Run the application
```
$ python /path/to/project/main.py
```

If you want to start consuming this application with [Docker](https://www.docker.com/get-started):
* Build the Docker image based on the Dockerfile contained in here:
```
$ docker build -f Dockerfile.effective-testing -t effective-testing .
``
* Run a container based on the compiled image
```
$ docker run --publish 5000:5000 --detach --name effective-testing effective-testing
```
* Enter into the container to launch the app
```
$ docker run -it -p5000:5000 effective-testing
```

## Running the tests
TO-DO unit tests.
E2E tests available in [Test-Suite project](https://github.com/MarceloCorpucci/effective-testing_test-suite)


## Built With
This application has built with the toolset below:

* [Python 2.7](https://www.python.org/downloads/mac-osx/)
* [Flask](https://palletsprojects.com/p/flask/)
* [Pip](https://pip.pypa.io/en/stable/)


