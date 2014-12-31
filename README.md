[![Build Status](https://img.shields.io/travis/python-edinburgh/pythonedinburgh/django-rewrite.svg)](https://travis-ci.org/python-edinburgh/pythonedinburgh)
[![Code Health](https://landscape.io/github/python-edinburgh/pythonedinburgh/django-rewrite/landscape.svg)](https://landscape.io/github/python-edinburgh/pythonedinburgh/django-rewrite)
[![Coverage Status](https://img.shields.io/coveralls/python-edinburgh/pythonedinburgh/django-rewrite.svg)](https://coveralls.io/r/python-edinburgh/pythonedinburgh?branch=django-rewrite)
[![Requirements Status](https://requires.io/github/python-edinburgh/pythonedinburgh/requirements.svg?branch=django-rewrite)](https://requires.io/github/python-edinburgh/pythonedinburgh/requirements/?branch=django-rewrite)

# Python Edinburgh Website

This is the code for the [Python Edinburgh](http://www.pythonedinburgh.org) website. It is built with Python and
Django.


##  Installation

The site has been designed to run on Heroku in production, and under Vagrant
in development. You can run it without Vagrant, but that's not
really recommended.

To get up and running, install
[Vagrant](https://www.vagrantup.com/) and
[Ansible](http://docs.ansible.com/)
(easiest to do with `pip install ansible`), then run `vagrant up`.
This will set up a VirtualBox
virtual machine, install and configure PostgreSQL and Python 3. It will also
set up virtualenvwrapper and create a virtual environment called `pew` with
all the development dependencies installed into it.

To start working with your installed site, do the following:

* `vagrant ssh`
* `workon pew`

### Configuration

The site is built as a [12 Factor](http://12factor.net/) app, so configuration
is passed in via environment variables. To make it easier to work with locally,
configuration can be stored in a file in the top-level directory called `.env`.
The following will work in the Vagrant VM:

```
DEBUG=True
DATABASE_URL=postgres://pew:pew@localhost/pew
SECRET_KEY=this-doesn't-matter-for-development
```

Once you have created your `.env` file, run the following commands:

```bash
dj migrate  # This will run the project's migrations on the development db.
djr         # This alias runs the Django development server.
```

## Run Tests

Run `make test` to run the code checks & unit tests and print a coverage
report. The alias `djt` will also run the tests without the coverage report or
quality check.


## Finding Your Way Around

The site's homepage can be browsed at `http://localhost:18000/` if you are
running the Vagrant VM. The admin site is configured to run at `/admin`.
