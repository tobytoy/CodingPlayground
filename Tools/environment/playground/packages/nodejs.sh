#!/bin/bash                                                                                                                                                 

curl --silent -o- https://raw.githubusercontent.com/creationix/nvm/v0.38.0/install.sh | bash
source "$HOME/.nvm/nvm.sh"
nvm install v14
