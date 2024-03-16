from flask import Flask, request, render_template
import math
from datetime import datetime, timedelta

app = Flask(__name__)

def calcul_patisseries_et_baguettes(nb_petits_dejeuners):
    # Calcul du nombre total de croissants et de pains au chocolat nécessaires
    if nb_petits_dejeuners > 10:
        nb_croissants_par_personne = math.ceil(0.75)
        nb_pains_chocolat_par_personne = math.ceil(0.75)
    else:
        nb_croissants_par_personne = 1
        nb_pains_chocolat_par_personne = 1
    
    nb_croissants = nb_petits_dejeuners * nb_croissants_par_personne
    nb_pains_chocolat = nb_petits_dejeuners * nb_pains_chocolat_par_personne

    # Calcul du nombre de baguettes nécessaires
    nb_baguettes = math.ceil(nb_petits_dejeuners / 3)  # Une baguette pour 3 personnes, arrondie à l'entier supérieur
    nb_baguettes_aux_graines = nb_baguettes // 3  # 1/3 de baguettes aux graines
    nb_baguettes_blanches = nb_baguettes - nb_baguettes_aux_graines  # 2/3 de baguettes blanches

    return nb_croissants, nb_pains_chocolat, nb_baguettes, nb_baguettes_aux_graines, nb_baguettes_blanches

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nb_petits_dejeuners = int(request.form['nb_petits_dejeuners'])

        nb_croissants, nb_pains_chocolat, nb_baguettes, nb_baguettes_aux_graines, nb_baguettes_blanches = calcul_patisseries_et_baguettes(nb_petits_dejeuners)

        date_lendemain = datetime.now() + timedelta(days=1)
        date_lendemain_str = date_lendemain.strftime('%d-%m-%Y')

        return render_template('result.html', nb_croissants=nb_croissants, nb_pains_chocolat=nb_pains_chocolat, nb_baguettes=nb_baguettes, nb_baguettes_aux_graines=nb_baguettes_aux_graines, nb_baguettes_blanches=nb_baguettes_blanches, date_lendemain=date_lendemain_str)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
