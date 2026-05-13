# E-Commerce Test Automation Platform

A scalable end-to-end automation framework built using Python, Selenium, Pytest, and API testing principles.

This project simulates a real-world e-commerce automation platform inspired by enterprise-scale systems such as Wayfair and modern retail applications.

---

# Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Requests (API Testing)
- Page Object Model (POM)
- GitHub Actions (CI/CD)
- HTML Reporting
  
---

# Features

## UI Automation
- Login validation
- Add-to-cart workflow
- Checkout flow
- Parameterized test execution

## API Automation
- GET API validation
- POST API validation
- JSON response assertions

## Framework Design
- Layered Page Object Model
- Reusable BasePage abstraction
- Explicit waits
- Logging support
- Screenshot capture on failures

## CI/CD
- Automated execution using GitHub Actions
- HTML report generation

---

# Project Structure

```text
pages/       -> Page Object classes
tests/       -> Test cases
api/         -> API client and endpoints
utils/       -> Driver and logger utilities
data/        -> Test datasets
reports/     -> HTML execution reports
```

---

# Running Tests

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run all tests

```bash
pytest
```

## Run specific test

```bash
pytest tests/test_checkout_parametrized.py
```

---

# Sample Scenarios

- Successful login
- Invalid login validation
- Add item to cart
- End-to-end checkout
- Parameterized checkout datasets
- API user validation

---

# CI/CD Pipeline

The framework is integrated with GitHub Actions for continuous integration and automated regression execution.

---

# Future Enhancements

- Docker integration
- Parallel execution using pytest-xdist
- Allure reporting
- Database validation layer
- Performance testing

---

# Author

Automation framework developed as part of advanced SDET portfolio engineering.

# Framework Architecture

```text
                +-------------------+
                |   Test Cases      |
                +-------------------+
                          |
                          v
                +-------------------+
                |   Page Objects    |
                +-------------------+
                          |
                          v
                +-------------------+
                |    Base Page      |
                +-------------------+
                          |
                          v
                +-------------------+
                | Selenium WebDriver|
                +-------------------+

                +-------------------+
                |    API Layer      |
                +-------------------+
                          |
                          v
                +-------------------+
                |   Requests Lib    |
                +-------------------+
```