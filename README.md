# Node Server

## Overview

The Node Server represents a server running on a node of a distributed file storage system. This repository provides functionalities for accepting files and storing them. Additionally, it offers functionalities to retrieve file chunks. In practical distributed storage systems, there would typically be a server like this running on every node.

## Setup

### Prerequisites

- Python 3.x installed on your system.
- Ensure pip is installed (Python's package installer).

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/jananga99/node-server.git
```

2. Navigate to the project directory:

```bash
cd node-server
```

3. Create the .env

```bash
cp .env.example .env
```

4. Create a virtual environment:

```bash
python3 -m venv .venv
```

4. Activate the virtual environment. This step may vary depending on your operating system:

#### For Windows:

```bash
.venv\Scripts\activate
```

#### For MacOS and Linux:

```bash
source .venv/bin/activate

```


5. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Server

To start the server, run the following command:

```bash
python3 index.py
```

### Interacting with the Server

Once the server is running, you can interact with it through HTTP requests. Here are some of the available endpoints:

- Upload File Chunk: POST request to /chunks with the file chunk data to be uploaded.
- Retrieve File Chunk: GET request to /chunk/<file_id> to retrieve a specific chunk of a file by its ID.

## File Storage

The server stores files locally on the node. Ensure that sufficient storage space is available on the node for storing files.
