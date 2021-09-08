#!/bin/bash

# install sdkman
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"

# install kotlin
sdk install kotlin

# node v14
curl --silent -o- https://raw.githubusercontent.com/creationix/nvm/v0.38.0/install.sh | bash
source "$HOME/.nvm/nvm.sh"
nvm install v14

# fzf
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install
