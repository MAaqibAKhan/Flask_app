from application import db
from application.models import Admin, Continant, Country
db.create_all()
admin1 = Admin(id='1', username='admin', password='password')
db.session.add(admin1)
db.session.commit()
