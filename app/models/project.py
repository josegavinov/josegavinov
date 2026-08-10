from app import db

class Project(db.Model):

    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    tittle = db.Column(db.String(100), nullable= False)
    description = db.Column(db.Text, nullable = False)
    technologies = db.Column(db.String(200), nullable = False)
    github_url = db.Column(db.String(255), nullable = True)
    demo_url = db.Column(db.String(255), nullable = True)

    def __repr__(self):
        return f"<Project {self.tittle}>"
    