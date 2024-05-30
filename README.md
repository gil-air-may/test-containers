# Test Containers with FastAPI

![Coverage](https://your-username.github.io/your-repository/coverage.svg)

## Overview

This project demonstrates how to set up and use Testcontainers with FastAPI to ensure reliable and isolated test environments. By automating your tests, you can maintain high code quality and gain valuable insights into your system's performance and behavior.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [GitHub Actions Setup](#github-actions-setup)
- [Contributing](#contributing)
- [License](#license)

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/gil-air-may/test-containers.git
cd test-containers
pip install -r requirements.txt
```

## Usage

Start the FastAPI application:

```bash
uvicorn main:app --reload
```

## Running Tests

Run tests with coverage:

```bash
pytest --cov=app tests/
```

## GitHub Actions Setup

This project uses GitHub Actions for continuous integration (CI) to automate testing. The CI workflow is defined in the `.github/workflows/ci.yml` file and includes the following steps:

1. **Checkout code**: Checks out the repository code.
2. **Set up Python**: Sets up the specified version of Python.
3. **Install dependencies**: Installs the required dependencies listed in `requirements.txt`.
4. **Run tests with coverage**: Executes tests and generates a coverage report.
5. **Set up Git for Pages**: Configures Git with GitHub Actions bot credentials.
6. **Checkout `gh-pages` branch**: Checks out the `gh-pages` branch for updating the coverage badge.
7. **Copy coverage badge**: Copies the generated coverage badge to the correct location.
8. **Add and commit coverage badge**: Adds and commits the coverage badge.
9. **Push to `gh-pages` branch**: Pushes the updated badge to the `gh-pages` branch.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

---
