## Mini Text-to-Speech Web App
A simple web application built using Flask and pyttsx3 that converts user-entered text into speech and allows playback directly in the browser.

## Features
Convert text to speech

User-friendly web interface

Audio playback in the browser

Responsive UI with custom CSS styling

## Tech Stack
Python

Flask

pyttsx3

HTML

CSS

## Project Structure
Text-To-Speech-Web-App
│── main.py
│── .gitignore
│── README.md
│
├── templates
│   └── index.html
│
├── static
│   ├── style.css
│   └── audio

## How It Works
Enter text in the textarea.

Click Convert to Speech.

The application converts the text into speech using pyttsx3.

The generated audio file is saved in the static/audio folder.

The audio can be played directly from the webpage.
