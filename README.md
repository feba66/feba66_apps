<!-- Copyright (C) 2024  Felix Baumkötter <contact@feba66.de> -->
<!-- Copyright (C) 2024  Jonathan Sigrist -->

# feba66_apps
One repo for all the services


# setup
```sh
py -m venv .venv
.\.venv\Scripts\Activate.ps1

pip install poetry
poetry install
```
# initial setup
```sh
py -m venv .venv
.\.venv\Scripts\Activate.ps1

pip install poetry

poetry self add poetry-multiproject-plugin@latest
poetry self add poetry-polylith-plugin@latest

poetry poly create workspace --name feba66_apps --theme loose
poetry poly create component --name hello

poetry install
```
