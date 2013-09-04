# Echelon Ignite 2013 Thailand SCM Workshop Sample Server

## Prerequistes

* vagrant ( not installed by gem )
* gem
* bundler
* fabric

## Setup

  git clone https://github.com/nulab/echelon-2013-scm-server.git
  cd echelon-2013-scm-server
  vagrant box add base http://developer.nrel.gov/downloads/vagrant-boxes/CentOS-6.4-x86_64-v20130731.box

## Start Server

  vagrant up
  vagrant ssh

## Generate ssh.config

  vagrant ssh-config > ssh.config

## Run Serverspec Test

  bundle
  rake spec

## Run ansible

by vagrant

  vagrant provision


by ansible

  ansible-playbook --private-key=<listed in ssh.config> provisioning/playbook.yml -i provisioning/ansible_hosts
