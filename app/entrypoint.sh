#!/bin/sh

echo "🚀 Starting the application..."
echo "🔍 Checking database migrations..."

# Checking whether migrations exist
if [ ! -d "migrations" ]; then
    echo "📂 No migrations found. Initializing migrations..."
    flask db init
else
    echo "✅ Migrations directory found."
fi

# Applying migrations to the database
echo "📌 Applying migrations..."
flask db migrate -m "Auto migration"
flask db upgrade

echo "✅ Database migrations applied successfully!"

# Launching the application
exec flask run --host=0.0.0.0 --port=5000 --debug