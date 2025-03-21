# lyricSanctuary

[![License](https://img.shields.io/badge/License-CC--BY--SA%204.0-lightgrey.svg)](LICENSE.md)
![Google Gemini](https://img.shields.io/badge/google%20gemini-8E75B2?style=for-the-badge&logo=google%20gemini&logoColor=white)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Table of Contents

* [Introduction](#introduction)
* [Design Patterns](#design-patterns)
* [Installation](#installation)
* [References, Inspirations, and Acknowledgements](#references)
* [AI Usage](#AI)
* [License](#license)

## Introduction

Welcome to **lyricSanctuary**, a web-based application designed to store, manage, and retrieve lyrics with associated musical and contextual information. This application is built with a focus on organization and extensibility, allowing users to store details such as song titles, authors, CCLI numbers, copyright information, detailed lyric breakdowns (verses, choruses, bridges, etc.), keys, associated documents (PDFs, MusicXML), songbook references, and Bible passages.

**lyricSanctuary** uses a document-oriented database (CouchDB with Mango Query Server) to provide flexible data storage and retrieval, with a Python-based web UI and API. The application is designed to be scalable and maintainable, making it suitable for both personal use and collaborative projects.

## Design Patterns

**lyricSanctuary** is designed with the following architectural and design patterns in mind:

* **Hexagonal Architecture (Ports and Adapters):**
    * The application is structured into distinct layers: Domain, Application, and Infrastructure (Adapters).
    * This separation allows for independent development and testing of each layer.
    * Adapters provide interfaces to external systems (e.g., CouchDB, web UI, API), ensuring that the core application logic remains decoupled.
* **Model-View-Controller (MVC) Principles:**
    * While not a strict MVC implementation, the application adheres to similar principles:
        * **Model:** The `lyricsRepository` and database represent the data model.
        * **View:** The web UI and API handle the presentation of data.
        * **Controller:** The `lyricsService` acts as a controller, coordinating interactions between the model and the view.
* **Document-Oriented Database:**
    * CouchDB with Mango Query Server is used to store data in JSON format, providing flexibility and scalability.
    * Mango queries allow for powerful json based searches.
* **Short GUIDs:**
    * Each song is assigned a short guid for use in retreival, update, and deletion.

## Installation

This application is designed to run on a LEMP (Linux, Nginx, Mango/CouchDB, Python) Stack on a server.

Basic server setup is:
    ```bash
    sudo apt update
    sudo apt install nginx ufw
    sudo ufw allow 'Nginx HTTP'
    sudo ufw allow 'Nginx HTTPS' #If you will use https
    sudo ufw enable
    ```

Follow these steps to set up **lyricSanctuary** on your local machine:

1.  **Prerequisites:**
    * Python 3.8 or later
    * CouchDB (with Mango Query Server enabled)
    * Git

2.  **Clone the Repository:**
    ```bash
    git clone https://github.com/mawdesign/lyricSanctuary
    cd lyricSanctuary
    ```

3.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    venv\Scripts\activate # On Windows
    source venv/bin/activate # On macOS/Linux
    ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure CouchDB:**
    * Ensure that CouchDB is running and accessible.
    * Update the application's configuration to point to your CouchDB instance.
    * The application expects the COUCHDB_URL and COUCHDB_DATABASE to be set.

6.  **Run the Application:**
    * Start the python web app using your selected python web framework.

7.  **Access the Application:**
    * Open your web browser and navigate to the appropriate URL.

8. **Database Creation:**
    * The database will be created on the first run, if it does not already exist.

## References, Inspirations, and Acknowledgements {#references}

* [Hexagonal architecture](https://dzone.com/articles/hexagonal-architecture-lyrics-app-example-java?edition=965104) for the idea to make a lyric store using hexagonal architecture.
* [OpenSong](https://opensong.org/development/file-formats/) has been used as a basis for ensuring the schema for songs has all the necessary fields.


## AI Usage {#AI}

This project is an experiment with utilising AI as a coding companion, Google Gemini has been used to help write code and Gemini Code Assist has been used to review code.

## License

This project is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. See the [LICENSE](LICENSE.md) file for details.
