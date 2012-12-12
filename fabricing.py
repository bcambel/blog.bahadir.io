from fabric.api import *

env.hosts=["production.server",]
env.user = 'deploy'

def hello():
	print "Hello dear"

def hostname_check():    # hostname_check is just a task name, replace with anything
	run("hostname")

def disc_size():
	run("df -h")

def free_memory():
	run("free -lmt")

def restart_nginx():
	run("/etc/init.d/nginx stop")
	run("/etc/init.d/nginx start")

def update_blog():
	run("/")

def command(cmd):
	run(cmd)

def sudo_command(cmd):
	sudo(cmd)

def install(package):
	sudo("apt-get -y install %s" % package)

def local_cmd():
	local("echo fabtest >> test.log")

def go_to_project():
	run("lcd /var/www/blog.bahadir.io && pwd")

def update_codebase():
	go_to_project()
	run("git pull")
project_location = '/var/www/blog.bahadir.io'

def show_git_log():
	with cd(project_location):
		run("git log -2")
