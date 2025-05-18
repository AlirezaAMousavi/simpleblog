# StandBlog

StandBlog is a simple and clean blogging platform built with Django. It offers basic blog features so users can create, edit, and read blog posts.

## Features

- User registration and authentication  
- Create, edit, and delete blog posts  
- View all posts on the homepage  
- Comment on posts  
- Simple and user-friendly interface  
- Searching based on article title  
- Filtering by tags and categories

## Installation

Follow these steps to get StandBlog running locally:

```bash
# Clone the repository
git clone https://github.com/AlirezaAMousavi/simpleblog

# Navigate to the project folder
cd standblog

# (Optional) Create and activate a virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

## Usage

- Visit `http://127.0.0.1:8000/` in your browser  
- Register or log in to your account  
- Create, manage, and browse blog posts  
- Use search or filter options to find specific posts

## Contributing

Contributions are welcome! Feel free to fork the repository, open issues, or submit pull requests.

## License

This project is licensed under the MIT License.
