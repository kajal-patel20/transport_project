# Render Deployment Checklist

## ✅ Files Created/Updated:

1. ✅ `requirements.txt` - Production dependencies (Django, gunicorn, psycopg2, whitenoise, etc.)
2. ✅ `build.sh` - Build script for Render (install deps, collectstatic, migrate)
3. ✅ `runtime.txt` - Python version specification (3.9.0)
4. ✅ `render.yaml` - Render configuration (optional, for automated setup)
5. ✅ `.gitignore` - Git ignore file
6. ✅ `README.md` - Documentation with deployment instructions
7. ✅ `settings.py` - Updated for production:
   - Added WhiteNoise middleware
   - Added dj-database-url for PostgreSQL
   - Added .onrender.com to ALLOWED_HOSTS
   - Configured static files with WhiteNoise

## 📋 Deployment Steps:

### 1. Initialize Git Repository
```bash
cd "c:\Users\Kajal Patel\OneDrive\Desktop\kajal\vs code files\SMG(Training)\transport_project"
git init
git add .
git commit -m "Initial commit - Transport Management System"
```

### 2. Create GitHub Repository
- Go to https://github.com/new
- Create a new repository (e.g., "transport-management-system")
- **Do NOT** initialize with README, .gitignore, or license

### 3. Push to GitHub
```bash
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
git branch -M main
git push -u origin main
```

### 4. Create Render Account
- Go to https://render.com/
- Sign up with GitHub account (recommended)

### 5. Create PostgreSQL Database (Recommended)
- In Render Dashboard: New + → PostgreSQL
- Name: `transport_db`
- Region: Choose closest to you
- Instance Type: Free
- Click "Create Database"
- **Copy the "Internal Database URL"** (starts with postgres://)

### 6. Create Web Service
- In Render Dashboard: New + → Web Service
- Connect your GitHub repository
- Configure:
  - **Name**: `transport-project` (or your choice)
  - **Region**: Same as database
  - **Branch**: `main`
  - **Runtime**: Python
  - **Build Command**: `./build.sh`
  - **Start Command**: `gunicorn transport_project.wsgi:application`
  - **Instance Type**: Free

### 7. Add Environment Variables
Click "Advanced" → "Add Environment Variable":

| Key | Value |
|-----|-------|
| `SECRET_KEY` | Generate using: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| `DEBUG` | `False` |
| `DATABASE_URL` | Paste the Internal Database URL from step 5 |
| `PYTHON_VERSION` | `3.9.0` |

### 8. Deploy
- Click "Create Web Service"
- Render will automatically build and deploy
- Monitor the logs for progress
- First deployment: 5-10 minutes

### 9. Create Superuser (After Deployment)
- In Render Dashboard → Your Web Service → Shell (top right)
- Run:
```bash
python manage.py createsuperuser
```
- Enter username, email, and password

### 10. Test Your Application
- Visit: `https://YOUR-SERVICE-NAME.onrender.com`
- Login at: `https://YOUR-SERVICE-NAME.onrender.com/admin/`
- Test transport request submission
- Test transport company assignment

## 🔧 Troubleshooting:

### Build Fails:
- Check logs in Render Dashboard
- Verify `build.sh` has executable permissions
- Ensure all packages in `requirements.txt` are compatible

### Static Files Not Loading:
- Run `python manage.py collectstatic` in Shell
- Verify WhiteNoise is in MIDDLEWARE
- Check STATIC_ROOT and STATICFILES_DIRS in settings.py

### Database Errors:
- Verify DATABASE_URL is set correctly
- Check PostgreSQL database is running
- Run migrations in Shell: `python manage.py migrate`

### App Not Starting:
- Check START_COMMAND is correct
- Verify gunicorn is in requirements.txt
- Check logs for Python errors

## 📝 Post-Deployment Tasks:

1. ✅ Create superuser account
2. ✅ Test login functionality
3. ✅ Add transport companies via admin
4. ✅ Test transport request submission
5. ✅ Test transport company assignment
6. ✅ Verify email notifications (if configured)

## 🔒 Security Checklist:

- ✅ DEBUG set to False in production
- ✅ SECRET_KEY is unique and secure
- ✅ ALLOWED_HOSTS configured correctly
- ✅ Database credentials secured via environment variables
- ✅ .gitignore prevents committing sensitive files

## 📊 Monitoring:

- Monitor logs in Render Dashboard
- Set up uptime monitoring (e.g., UptimeRobot)
- Enable email notifications for deployments

## 🚀 Automatic Deployments:

Render automatically deploys when you push to GitHub:
```bash
git add .
git commit -m "Your changes"
git push
```

## 💡 Tips:

1. Free tier sleeps after 15 min of inactivity (wakes in ~30s)
2. Upgrade to paid tier for always-on service
3. Use PostgreSQL backup feature in Render
4. Monitor database size (100MB limit on free tier)
5. Consider upgrading for production use

## 🆘 Need Help?

- Render Documentation: https://render.com/docs
- Django Deployment: https://docs.djangoproject.com/en/4.2/howto/deployment/
- Check Render community forum
