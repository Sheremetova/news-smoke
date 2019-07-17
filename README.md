# news-smoke

1) Need to be installed:
  - nodejs
  - appium 1.13 (http://appium.io/docs/en/about-appium/getting-started/)
  - pyenv
2) Install python 3:
  - pyenv install 3.7.4
  - pyenv global 3.7.4

3) Add the following to ~/.bash_profile
  - export PYENV_ROOT="$HOME/.pyenv"
  - export PATH="$PYENV_ROOT/bin:$PATH"
  - export PATH="$PYENV_ROOT/shims:$PATH"
  - export PATH="$PYENV_ROOT/completions/pyenv.bash:$PATH"

4) Install following:
  - pip install pytest
  - pip install pylint
  - pip install Appium-Python-Client
  
5) Clone and cd to repository
6) Run tests via comand line:
  pytest
