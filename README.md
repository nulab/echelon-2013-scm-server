# Echelon Ignite 2013 Thailand SCM Workshop Sample Server

## Prerequistes

* vagrant ( not installed by gem )
* gem
* bundler

## Setup

  git clone https://github.com/nulab/echelon-2013-scm-server.git
  cd echelon-2013-scm-server
  vagrant box add base http://developer.nrel.gov/downloads/vagrant-boxes/CentOS-6.4-x86_64-v20130731.box

## Start Server

  vagrant up
  vagrant ssh

## Run Serverspec Test

  bundle
  rake spec

