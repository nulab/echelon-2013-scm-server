# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "base"

  config.vm.network :private_network, ip: "192.168.33.10"

  # http://docs.vagrantup.com/v2/provisioning/ansible.html
  config.vm.provision :ansible do |ansible|
    ansible.playbook = "provisioning/playbook.yml"
#    ansible.inventory_file = "provisioning/ansible_hosts"
    ansible.inventory_path = "provisioning/ansible_hosts"
    ansible.verbose = true
  end  
end
