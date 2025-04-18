# AI-work

**Notice:** This project was developed using Python 3.12.10. Functionality on other Python versions is not guaranteed and may not work as expected.

## Installation (Python 3.12.10 on Windows)

1. Go to [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/) and download the installer for Python 3.12.10.
2. Run the installer, ensuring "Add Python 3.12 to PATH" is checked.
3. Click "Install Now".
4. Verify installation in Command Prompt with `python --version`.

## Environment Setup

This project includes a pre-configured virtual environment in the `env` folder. To use it:

1. Navigate to the repository directory:

    ```bash
    cd AI-work
    ```

    (Adjust the path if your local directory name is different.)

2. Activate the virtual environment:

    ```bash
    .\env\Scripts\activate
    ```

## Pre-installed Packages in the Virtual Environment

The virtual environment in the `env` folder already has the following packages installed:

* `fer`
* `opencv-python`
* `tensorflow` (which includes `keras`)
* `mediapipe`
* `deepface` (note: `tf-keras` is also included for proper functionality)
