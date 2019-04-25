# DevHub

Hub for DEVelopment related stuff: news, articles, source codes, ideas, etc.

## Related [YouTube](http://youtube.com/CoderVlogger "CoderVlogger's YouTube channel") videos

Please check out the following videos to learn more about DevHub:

1. [Introduction & Custom User Model](https://youtu.be/cg0KNJZqInY)
2. [Setup URLs, templates and HTML views for Account application](https://youtu.be/yNlRzTfZi8Q)

# Setup

## Using `virtualenv`

1. Make sure you have [Python 3] and [virtualenv] installed
2. Clone this repository: `git clone https://github.com/CoderVlogger/devhub.git`
3. Move into the project folder: `cd devhub`
4. Create a new virtualenv: `virtualenv venv -p python3`
5. Activate the virtualenv: `source ./venv/bin/activate`
6. Install dependencies: `pip install -r requirements.txt`

## Using `Docker`

1. Make sure you have Docker installed
2. Clone this repository: `git clone https://github.com/CoderVlogger/devhub.git`
3. Move into the project folder: `cd devhub`
4. Build the Image using Dockerfile: `docker build -t [Image-Name] .`
5. Run a container: `docker run -p 8000:8000 -it --rm --name [Container-Name] [Image-Name]`

# Project Structure

## Repository structure

1. `src` - source code
2. `docs` - auto generated Sphinx documentation (to be added)
3. `tests` - high level tests (e2e, load, etc. - to be added)

## Django applications

1. Account
   1. User side register, login and logout
   2. Profile and account settings
2. Board (to be added)
   1. Share public posts
   2. Post rating system
   3. Post comments

[Python 3]: https://www.python.org/downloads/
[virtualenv]: https://virtualenv.pypa.io/en/stable/
