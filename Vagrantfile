# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Silly but effective syntax for declaring box hostname
  config.vm.define :septajawn do |t|
  end

  # Canonical builds nightly Vagrant images for Ubuntu: http://cloud-images.ubuntu.com/vagrant/
  # Still using 12.04 LTS, since 14.04 LTS isn't ready yet.
  config.vm.box = "septajawn"
  config.vm.box_url = "http://cloud-images.ubuntu.com/vagrant/precise/current/precise-server-cloudimg-amd64-vagrant-disk1.box"

  config.vm.network :forwarded_port, guest: 8000, host: 8000
  config.vm.network :private_network, ip: "192.168.33.33"

  config.vm.provider :lxc do |lxc, override|

    # The author of vagrant-lxc maintains base boxses at https://github.com/fgrehm/vagrant-lxc/wiki/Base-boxes
    override.vm.box = "raring64-lxc"
    override.vm.box_url = "http://bit.ly/vagrant-lxc-raring64-2013-10-23"
    # Same effect as as 'customize ["modifyvm", :id, "--memory", "1024"]' for VirtualBox
    #lxc.customize 'cgroup.memory.limit_in_bytes', '2014M'

  end

  config.vm.provider :aws do |aws, override|

    # We need a box to base this image on, so point Vagrant to a dummy one.
    override.vm.box = "dummy-aws"
    override.vm.box_url = "https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box"

    # Make sure these environment variables are populated in the host OS 
    # (i.e. the machine deploying the VM).
    aws.access_key_id = ENV['AWS_ACCESS_KEY']
    aws.secret_access_key = ENV['AWS_SECRET_KEY']
    override.ssh.private_key_path = ENV['EC2_PRIVATE_KEY']
    override.ssh.username = "ubuntu"

    # Set these security options in the EC2 Console
    aws.security_groups = [ 'vagrant' ]
    aws.keypair_name = "vagrant-aws"

    # Specify the instance type here, e.g. [ "t1.micro", "t1.small", "t1.large" ]
    aws.instance_type = "t1.micro"

    # Canonical maintains an index for EC3 images: http://cloud-images.ubuntu.com/locator/ec2/
    # us-east-1 raring 13.04 amd64 instance-store ami-ad83d7c4
    aws.ami = "ami-ad83d7c4"
    aws.region = "us-east-1"

  end

  config.vm.provider :virtualbox do |vb, override|

    # Enable vagrant-cachier support, so packages aren't downloaded for every provisioning.
    config.cache.auto_detect = true
    config.cache.enable :apt
    config.cache.enable :chef

    vb.customize ["modifyvm", :id, "--memory", "1024"]
    vb.customize ["modifyvm", :id, "--cpus", "2"]
    vb.name = "djangobox"

  end

  config.vm.provision :ansible do |ansible|
     ansible.playbook = "ansible/playbook.yml"
     ansible.inventory_file = "ansible/hosts" 
     ansible.extra_vars = { :project_name => "septajawn" }
     ansible.verbose = "extra"
  end
end
