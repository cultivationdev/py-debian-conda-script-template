# Cultivation.dev Python Level Up: Dockerize Python 

## py-debian-conda-script-template

### Docker Instructions

#### Docker Build & Run App

```
docker build --target python-base -f Dockerfile -t py-debian-conda-script .
docker run --user=appuser --env APP_ENV=DEV py-debian-conda-script
```

#### Docker Build & Run Tests

```
docker build --target testing -f Dockerfile -t py-debian-conda-script .
docker run --user=appuser --env APP_ENV=DEV py-debian-conda-script
```

---

### Local Environment

#### Pre-requisites

- Install anaconda via homebrew e.g. `brew cask install anaconda`

#### Environment Setup

- Create conda environment via `conda env create -f conf/environment.yml`