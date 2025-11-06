from app import app
from models import db, User, Credential


def seed_users():
    users_data = [
        {
            'firstname': 'John',
            'lastname': 'Doe',
            'email': 'john.doe@example.com',
            'password': 'password123'
        },
        {
            'firstname': 'Jane',
            'lastname': 'Smith',
            'email': 'jane.smith@example.com',
            'password': 'password123'
        },
        {
            'firstname': 'Admin',
            'lastname': 'User',
            'email': 'admin@example.com',
            'password': 'password123'
        },
        {
            'firstname': 'Test',
            'lastname': 'User',
            'email': 'test@example.com',
            'password': 'password123'
        }
    ]

    print("Seeding users...")

    for user_data in users_data:
        existing_user = User.query.filter_by(email=user_data['email']).first()

        if existing_user:
            print(f"User {user_data['email']} already exists, skipping...")
            continue

        user = User(
            firstname=user_data['firstname'],
            lastname=user_data['lastname'],
            email=user_data['email'],
            is_active=True
        )

        db.session.add(user)
        db.session.flush()

        credential = Credential(
            uid=user.uid,
            email=user_data['email']
        )
        credential.set_password(user_data['password'])

        db.session.add(credential)

        print(f"Created user: {user_data['email']} (password: {user_data['password']})")

    db.session.commit()
    print("User seeding completed!\n")


def seed_all():
    with app.app_context():
        print("\n" + "="*50)
        print("  DATABASE SEEDER")
        print("="*50)

        seed_users()

        print("="*50)
        print("  ALL SEEDERS COMPLETED SUCCESSFULLY!")
        print("="*50 + "\n")


def clear_database():
    with app.app_context():
        print("\nWARNING: Clearing database...")

        Credential.query.delete()
        User.query.delete()

        db.session.commit()
        print("Database cleared!\n")


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == '--fresh':
        clear_database()
        seed_all()
    elif len(sys.argv) > 1 and sys.argv[1] == '--clear-only':
        clear_database()
    else:
        seed_all()