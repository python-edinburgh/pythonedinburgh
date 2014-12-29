# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = 'ubuntu/trusty64'
  #config.vm.box_url = 'http://files.vagrantup.com/' + config.vm.box + '.box'

  # PostgreSQL port:
  config.vm.network "forwarded_port", guest: 5432, host: 15432
  config.ssh.forward_agent = true

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "vagrant_provisioning/playbook.yml"
  end
end
