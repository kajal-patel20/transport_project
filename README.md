# Transport Management System

A Django-based transport booking system for employee transport requests with admin portal for transport company assignment.

## Features

- **Employee Portal**: Submit transport requests with details like vehicle type, date, time, pickup/drop locations
- **Admin Portal**: Manage transport companies and assign them to employee requests
- **Dashboard**: View all transport requests with assigned company details

## Local Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Create superuser:
```bash
python manage.py createsuperuser
```

4. Run the development server:
```bash
python manage.py runserver
```

## Deployment to Render

### Prerequisites
- GitHub account
- Render account (free tier works)

### Steps:

1. **Push your code to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Create a new Web Service on Render**:
   - Go to https://dashboard.render.com/
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure the service:
     - **Name**: transport-project (or your preferred name)
     - **Environment**: Python
     - **Build Command**: `./build.sh`
     - **Start Command**: `gunicorn transport_project.wsgi:application`
     - **Instance Type**: Free

3. **Add Environment Variables** in Render Dashboard:
   - `SECRET_KEY`: Generate a new secret key (use Django's get_random_secret_key())
   - `DEBUG`: `False`
   - `PYTHON_VERSION`: `3.9.0`

4. **Create PostgreSQL Database** (Optional - for production):
   - In Render Dashboard, click "New +" → "PostgreSQL"
   - Name it `transport_db`
   - After creation, copy the "Internal Database URL"
   - Add it as `DATABASE_URL` environment variable in your Web Service

5. **Deploy**:
   - Render will automatically deploy when you push to GitHub
   - First deployment takes 5-10 minutes
   - Check logs for any errors

6. **Create Admin User** (After first deployment):
   - Go to Render Dashboard → Your Web Service → Shell
   - Run: `python manage.py createsuperuser`
   - Follow prompts to create admin account

7. **Access Your App**:
   - Your app will be available at: `https://<your-service-name>.onrender.com`
   - Admin panel: `https://<your-service-name>.onrender.com/admin/`

## Environment Variables

- `SECRET_KEY`: Django secret key (required in production)
- `DEBUG`: Set to `False` in production
- `DATABASE_URL`: PostgreSQL connection string (optional, uses SQLite if not set)
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `PYTHON_VERSION`: Python version (3.9.0)

## File Structure

```
transport_project/
├── manage.py
├── requirements.txt
├── build.sh                 # Render build script
├── runtime.txt              # Python version
├── render.yaml              # Render configuration (optional)
├── transport_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── requests_app/
    ├── models.py            # TransportRequest, TransportCompany models
    ├── views.py             # Login, dashboard, request views
    ├── forms.py             # Request forms
    ├── urls.py
    ├── admin.py
    ├── templates/
    └── static/
```

## Important Notes

- The app uses SQLite locally and PostgreSQL on Render (recommended)
- Static files are served using WhiteNoise
- Make sure to set `DEBUG=False` in production
- Keep your `SECRET_KEY` secure and never commit it to Git
- The free tier on Render may sleep after inactivity (takes 30s to wake up)

## Support

For issues or questions, contact your system administrator.
