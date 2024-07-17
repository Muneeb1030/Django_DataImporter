# Django Data Importer with MongoDB, Redis, and Celery
## Overview
This Django project features a robust data importer tool designed to handle large file imports efficiently. Leveraging Django's custom management commands, MongoDB integration, and asynchronous task processing with Celery and Redis, this project ensures seamless import operations without affecting the UI responsiveness.

## Key Features
- **Custom Management Command:** Utilizes Django's custom command to initiate and manage data imports from various sources.
- **MongoDB Integration:** Incorporates MongoDB as the database backend for storing imported data.
- **Asynchronous Processing:** Uses Celery and Redis to handle import tasks asynchronously, allowing the UI to remain responsive during large file imports.
- **Progress Tracking:** Provides real-time progress updates and status notifications for ongoing import operations.
- **Error Handling:** Implements robust error handling mechanisms to manage exceptions during the import process.
- **Logging:** Utilizes logging to maintain detailed records of import activities and errors.
## Installation
- Clone the repository:
```bash
git clone https://github.com/your_username/your_project.git
cd your_project
```
Install dependencies:
```bash
pip install -r requirements.txt
```
### Configure MongoDB:
- Ensure MongoDB is installed and running.
- Update database settings in settings.py to connect to your MongoDB instance.
### Configure Redis:
- Ensure Redis is installed and running.
- Update Celery settings in settings.py to configure Redis as the broker and backend.
### Apply database migrations:
``bash
python manage.py migrate
```
- Start Celery worker:
```bash
celery -A your_project worker -l info
```
- Run Django development server:
```bash
python manage.py runserver
```
- Access the application at http://localhost:8000/.

## Usage
- **Data Import:** Execute the custom command to initiate data imports:
```bash
python manage.py import_data --file path_to_your_data_file.csv
```
- **Monitor Progress:** View real-time progress updates and logs in the console.

- **Check Imported Data:** Access the imported data stored in MongoDB via the Django admin or custom views.

## Contributing
Contributions are welcome! If you have any suggestions, improvements, or feature requests, feel free to open an issue or submit a pull request.
