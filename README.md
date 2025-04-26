# Palliative Care Management System

A web-based healthcare management system specifically designed for palliative care services, built with Django and Bootstrap.

## Features

- **User Management**
  - User registration and authentication
  - User profile management
  - Role-based access control (Admin, Staff, Patients)

- **Patient Management**
  - Add and manage patient records
  - Track patient details (name, age, height, weight, gender)
  - Medical history documentation
  - Palliative care progress tracking

- **Payment System**
  - Secure payment processing
  - Payment history tracking
  - Transaction confirmation

- **Admin Dashboard**
  - Built with Skydash Admin Template
  - Comprehensive analytics and reporting
  - User management interface
  - System monitoring tools

## Technology Stack

- **Backend**
  - Django (Python Web Framework)
  - SQLite/PostgreSQL Database

- **Frontend**
  - HTML5, CSS3, JavaScript
  - Bootstrap 4
  - jQuery
  - Chart.js for analytics
  - TinyMCE for rich text editing

- **Admin Interface**
  - Skydash Admin Template
  - Material Design Icons
  - Various JS plugins for enhanced functionality

## Installation

1. Clone the repository
```bash
git clone [repository-url]
cd [project-directory]
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up the database
```bash
python manage.py migrate
```

5. Create superuser
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
python manage.py runserver
```

## Project Structure

```
PaliativeCare/
├── Guest/
│   ├── static/
│   │   ├── Admin/  # Admin template files
│   │   └── Main/   # Main site static files
│   └── Templates/
├── User/
│   └── Templates/
│       └── User/   # User-related templates
├── PaliativeCare/
│   └── Templates/
└── manage.py
```

## Configuration

1. Update `settings.py` with your specific configurations
2. Set up your environment variables
3. Configure your database settings

## Usage

1. Access the admin interface at `/admin`
2. Regular users can access the main application at `/`
3. Add patients through the patient management interface
4. Track and manage palliative care progress
5. Process payments and view transaction history

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Skydash Admin Template
- Bootstrap Team
- Django Framework
- All other open-source contributors