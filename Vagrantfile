Vagrant.configure("2") do |config|

config.vm.box = "debian/bookworm64"

config.vm.network "forwarded_port", guest: 5000, host: 5001

config.vm.provision "shell", inline: <<-SHELL
	/vagrant/automate.sh
SHELL


end

