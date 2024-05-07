install_pyenv_macos:
	brew update
	brew install pyenv

install_pyenv_ubuntu:
	curl https://pyenv.run | bash
	echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
	echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
	echo 'eval "$(pyenv init -)"' >> ~/.bashrc
	source ~/.bashrc # This command might fail

pyenv_pythons: python311 python310 python39

python311:
	pyenv install 3.11
	pyenv local 3.11

python310:
	pyenv install 3.10
	pyenv local 3.10

python39:
	pyenv install 3.9
	pyenv local 3.9pye

find_pyenv_versions:
	ls ~/.pyenv/versions/