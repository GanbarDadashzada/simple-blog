# Simple Blog API with FastAPI

This is a simple Blog API built using FastAPI. It allows users to create, delete, update blogs, like and comment on blogs, and save drafts.

## Features

- **Create, Read, Update, Delete (CRUD) Blogs**: Users can create new blog posts, edit existing ones, and delete them.
- **Like and Comment**: Users can like and comment on blog posts.
- **Draft Mode**: Blog posts can be saved as drafts for later publishing.
- **API Documentation**: Automatically generated with Swagger UI at `/docs`.

## Requirements

- Docker
- Docker Compose

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Build and run the application using Docker Compose:

    ```bash
    docker-compose up --build
    ```

3. The FastAPI application will be running at `http://localhost:8000`.

## Usage

- Open the browser and go to `http://localhost:8000/docs` to explore the API documentation using Swagger UI.
- Use `curl`, Postman, or any HTTP client to test the API endpoints.

## Environment Variables

Set up a `.env` file with the necessary environment variables (e.g., database credentials, secret keys). Make sure the `.env` file is added to your `.gitignore` so it isn't committed to the repository.

## Acknowledgments

This project uses several open-source libraries, each of which is licensed under their respective terms. Please see the `NOTICE.txt` file for details.

## Contributing

Feel free to fork this project and submit pull requests.

## License

This project is licensed under the MIT License.
