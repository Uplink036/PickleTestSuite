install_pyenv_macos:
	brew update
	brew install pyenv

pyenv_pythons: python311 python310 python39
	pyenv local 3.9 3.10 3.11

python311:
	pyenv install 3.11

python310:
	pyenv install 3.10

python39:
	pyenv install 3.9

find_pyenv_versions:
	ls ~/.pyenv/versions/

clean: ## Only works on UNIX systems
	rm -r logs/