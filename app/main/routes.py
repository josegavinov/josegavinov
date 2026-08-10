from flask import render_template
from app.main import main_bp


@main_bp.route('/')
def home():
    perfil={
        
        'habilidades': ['Python', 'Flask', 'HTML', 'CSS', 'JavaScript', 'SQL', 'Git']
    }
    return render_template('index.html', usuario=perfil)


@main_bp.route('/sobre-mi')
def sobre_mi():
    return render_template('sobre_mi.html')