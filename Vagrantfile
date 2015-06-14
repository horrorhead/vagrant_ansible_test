Vagrant.configure("2") do |config|

  config.vm.provision :ansible do |ansible|
    ansible.playbook = "site.yml"
    ansible.verbose = false
    ansible.groups = {
      "lb" => ["lb"],
      "web" => ["web01","web02"],
      "all_groups:children" => ["lb", "web"]}
  end
  
  config.vm.define "lb" do |lb|
    lb.vm.box = "hashicorp/precise32"
    lb.vm.hostname = "loadbalancer"
    lb.vm.network "private_network", ip: "192.168.1.110"
  end

  config.vm.define "web01" do |web01|
    web01.vm.box = "hashicorp/precise32"
    web01.vm.hostname = "web01"
    web01.vm.network "private_network", ip: "192.168.1.120"
  end

  config.vm.define "web02" do |web02|
    web02.vm.box = "hashicorp/precise32"
    web02.vm.hostname = "web02"
    web02.vm.network "private_network", ip: "192.168.1.121"
  end

end