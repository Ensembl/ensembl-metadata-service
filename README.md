# Ensembl Metadata Service

[ARCHIVED] This repository is not maintained anymore - related service and code has been moved back to https://github.com/Ensembl/ensembl-metadata-api/

[![Build Status](https://travis-ci.com/Ensembl/ensembl-metadata-service.svg?branch=main)](https://travis-ci.com/Ensembl/ensembl-metadata-service)

gRPC layer for the Ensembl Metadata database.

## System Requirements

- Python 3.8+
- MySQL Client

## Usage

Clone the repository:
```
git clone -b main https://github.com/Ensembl/ensembl-metadata-service.git
```

Install the environment (with pyenv)

```
cd ensembl-metadata-service
pyenv virtualenv 3.8 ensembl_metadata_service
pyenv local ensembl_metadata_service
pip install --upgrade pip
pip install -r requirements.txt
```

## Related repositories

[ensembl-metadata](https://github.com/Ensembl/ensembl-metadata): Legacy Ensembl Metadata database and Perl API

[ensembl-metadata-admin](https://github.com/Ensembl/ensembl-metadata-admin): Django ORM for the Ensembl Metadata database

[ensembl-metadata-api](https://github.com/Ensembl/ensembl-metadata-api): SQLAlchemy ORM for the Ensembl Metadata database

[ensembl-metadata-registry](https://github.com/Ensembl/ensembl-metadata-registry): GUI for the Ensembl Metadata database


## Development

Install the development environment (with pyenv)

```
cd ensembl-metadata-service
pyenv virtualenv 3.8 ensembl_metadata_service
pyenv local ensembl_metadata_service
pip install --upgrade pip
pip install -r requirements-dev.txt
```

Install the development environment (with mkvirtualenv)

```
cd ensembl-metadata-service
mkvirtualenv ensembl_metadata_service -p python3.8
workon ensembl_metadata_service
pip install --upgrade pip
pip install -r requirements-dev.txt
```

To generate client and server files
(Remember to run these after adding a new method in ensembl_metadata.proto)
```
python3 -m grpc_tools.protoc -Iprotos --python_out=src --grpc_python_out=src protos/ensembl/production/metadata/grpc/ensembl_metadata.proto
```

Start the server script

```
PYTHONPATH='src' python3 src/ensembl/production/metadata/grpc/service.py
```

Start the client script
```
PYTHONPATH='src' python3 src/ensembl/production/metadata/grpc/client_examples.py
```

### Testing

Run test suite:
```
cd ensembl-metadata-service
PYTHONPATH='src' pytest
```

To run tests, calculate and display testing coverage stats:
```
cd ensembl-metadata-service
coverage run -m pytest
coverage report -m
```

#### Explore test DB content

As for now, some of the test DB sqlite content is different from what's in MySQL metadata DB (e.g. release `version` in `ensembl_release`)

> `test.db` created when running tests is deleted once tests are executed.

To take a look at the test data you can create a temporary `sampledb.db` importing `tables.sql` content using the command:

```
cat tables.sql | sqlite3 sampledb.db
```

You can then open `sampledb.db` using [DB Browser for SQLite](https://sqlitebrowser.org/dl/).

### Automatic Formatting
```
cd ensembl-metadata-service
black --check src tests
```
Use `--diff` to print a diff of what Black would change, without actually changing the files.

To actually reformat all files contained in `src` and `test`:
```
cd ensembl-metadata-service
black src tests
```

### Linting and type checking
```
cd ensembl-metadata-service
pylint src tests
mypy src tests
```
Pylint will check the code for syntax, name errors and formatting style.
Mypy will use type hints to statically type check the code.

### To build docker image
```
docker build -t ensembl-metadata-service .
```

### To run docker container
```
 docker run -t -i -e METADATA_URI=<URI> -e TAXONOMY_URI=<URI> -p 80:80 ensembl-metadata-service
```
