# Turn Test

# Setup Instructions

## Python Setup

This project requires _**Python 3.8**_ or higher. You can download the latest Python version from Python.org.

You should also have a Python editor/IDE of your choice. But take note that this project was delelop in _**Visual Studio Code**_.

You will also need Git to copy this project code. If you are new to Git, try learning the basics.

## WebDriver Setup

For Web UI testing, you will need to install the latest versions of Google Chrome and Mozilla Firefox.

You will also need to install the latest versions of the WebDriver executables for these browsers: ChromeDriver for Chrome and geckodriver for Firefox. Each test case will launch the WebDriver executable for its target browser. The WebDriver executable will act as a proxy between the test automation and the browser instance. Please use the latest versions of both the browsers and the WebDriver executables. Older versions might be incompatible with each other.

_**ChromeDriver**_ and _**geckodriver**_ must be installed on the system path.

## Test WebDriver Setup

To verify correct setup on any operating system, simply try to run them from the terminal:

>$ ChromeDriver

>$ geckodriver

You may or may not see any output. Just verify that you can run them without errors.

## Project Setup

* Clone this repository.
* Verify have pytest installed
* Create a branch for your code changes.

## Repository Branching

The master branch contains the code for the project. If you want to code along, then create a branch for your work off the master branch.

## Files description

### Documents
Will find all the files will be handle on the project

### Drivers
Will find the web drivers and in this folder the files need to be up to date on the version

### Data Handler
This file will handle the used data for test, just need to change the values here to be reflected in all the tests

### Selenium driver
This file habdle the driver path for the given browser on the data handler **DO NOT TOUCH THIS FILE**


