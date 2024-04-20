# Market Web App

Market is a Django-based web application that allows users to browse and view information about various books available in the market.

## Features

- Browse a list of books available in the market.
- View detailed information about each book.
- Add books to the cart for purchase (future feature).
- User authentication and authorization (future feature).

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/market.git
    ```

2. Navigate to the project directory:

    ```bash
    cd market
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run database migrations:

    ```bash
    python manage.py migrate
    ```

7. Create a superuser (admin account):

    ```bash
    python manage.py createsuperuser
    ```

8. Run the development server:

    ```bash
    python manage.py runserver
    ```

9. Access the application in your web browser at `http://127.0.0.1:8000/`.

## Usage

1. Visit the home page to browse the list of available books.
2. Click on a book to view detailed information about it, including title, author, description, etc.
3. (Future feature) Use the cart functionality to add books for purc
