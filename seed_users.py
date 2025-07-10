# seed_users.py
from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    # Lista de usuarios de prueba
    users = [
        {'username': 'diego', 'password': '1234'},
        {'username': 'mayra', 'password': 'solcito'},
        {'username': 'admin', 'password': 'admin123'},
        {'username': 'invitado', 'password': 'guestpass'},
        {'username': 'usuario1', 'password': 'clave1'}
    ]

    for u in users:
        user = User(username=u['username'], password=generate_password_hash(u['password']))
        db.session.add(user)

    db.session.commit()
    print("✅ Usuarios de prueba insertados correctamente.")
