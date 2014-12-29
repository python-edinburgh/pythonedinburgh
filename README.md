# Python Edinburgh Website

This is the code for the Python Edinburgh website. It is built with Python and
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

To run the website inside your VM, run

* `vagrant ssh`
* `workon pew`
* `cd /vagrant`
