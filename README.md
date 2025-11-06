# Nebula Admin

## Command Notes

### Sass Commands
```bash
# Install Sass globally
npm install -g sass

# Compile SCSS to CSS
sass <src> <destination> --style=compressed
```


## Database

### Connection URI
```
mysql+pymysql://root:yourpassword@localhost/admin_panel
```

### Database Seeding
```bash
# Seed database with sample users
python seeders.py

# Clear database and seed fresh data
python seeders.py --fresh

# Only clear database without seeding
python seeders.py --clear-only
```

**Default Seeded Users:**
- john.doe@example.com
- jane.smith@example.com
- admin@example.com
- test@example.com

All users have password: `password123`