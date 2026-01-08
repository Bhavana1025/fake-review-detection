# Contributing to Fake Review Detection

Thank you for your interest in contributing to this project! This document provides guidelines and instructions for contributing.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/fake-review-detection.git`
3. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   pip install -e ".[dev]"  # Install development dependencies
   ```

## Development Workflow

1. Create a new branch for your feature/fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and test them

3. Ensure code quality:
   ```bash
   # Format code
   black src/ tests/
   
   # Check linting
   flake8 src/ tests/
   
   # Run tests
   pytest tests/
   ```

4. Commit your changes:
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

5. Push to your fork and create a Pull Request

## Code Style

- Follow PEP 8 style guide
- Use type hints where appropriate
- Write docstrings for all functions and classes
- Keep functions focused and single-purpose

## Testing

- Write tests for new features
- Ensure all tests pass before submitting
- Aim for good test coverage

## Pull Request Process

1. Update README.md if needed
2. Update documentation for new features
3. Ensure all tests pass
4. Request review from maintainers

## Questions?

Feel free to open an issue for questions or discussions.
