# dl-utils

`dl-utils` is a Python utility package designed to simplify AWS Data Lake operations. It provides reusable tools and CLI support for working with Amazon S3, EMR (Elastic MapReduce), and Athena, ideal for data engineers and ML engineers building pipelines in the Datalake.

## Features

- **S3 Utilities**: Upload, download, list, and manage objects in S3.
- **EMR Utilities**: Submit jobs, monitor clusters, and interact with EMR on EKS.
- **Athena Utilities**: Submit queries, retrieve results, and manage workgroups.
- **CLI Support**: Easily accessible commands via command-line interface.
- **Test Coverage**: Pytest included with a basic test suite.
- **Sphinx Documentation**: Auto-generated docs using type hints and docstrings.

---

## Getting Started

### 🐍 Prerequisites

- Python 3.8+
- [Poetry](https://python-poetry.org/) (for dependency management)
- AWS credentials configured (`~/.aws/credentials`)

### 🛠️ Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"
poetry --version
```

### 📦 Install Dependencies

```bash
poetry install
```

---

## 🧪 Run Tests

```bash
poetry run pytest
```

---

## 🚀 CLI Usage

```bash
poetry run dl-utils s3 list-buckets
poetry run dl-utils emr submit-job --cluster-id j-XXXX
poetry run dl-utils athena run-query "SELECT * FROM my_table"
```

You can explore more CLI subcommands inside `dl_utils/cli/`.

---

## 📚 Generate Documentation

1. Navigate to the `docs` folder:
   ```bash
   cd docs
   ```

2. Build HTML documentation:
   ```bash
   sphinx-build . _build
   ```

3. Open the documentation:
   ```
   open _build/index.html
   ```

---

## 📁 Project Structure

```
dl-utils/
├── dl_utils/
│   ├── __init__.py
│   ├── s3_utils.py
│   ├── emr_utils.py
│   ├── athena_utils.py
│   └── cli/
│       └── __init__.py
├── tests/
│   └── test_basic.py
├── docs/
│   ├── conf.py
│   └── index.rst
├── README.md
├── pyproject.toml
└── poetry.lock
```

---

## 📦 Packaging

To build the package for distribution:

```bash
poetry build
```

---

## 🤝 Contributing

This package is intended to serve as a starter template and utility library for internal teams working on AWS data pipelines. Contributions and suggestions are welcome via internal Nexus or Git systems.

---

## 🔐 License

Internal Use Only – proprietary and confidential.
