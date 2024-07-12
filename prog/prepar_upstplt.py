import glob
import json

def lire_json (chemin):
    with open(chemin) as mon_fichier:
        data = json.load(mon_fichier)
    return data
def model_ocr(chemin):

    ocr_mod=chemin.split("/")[5]
    ocr_mod = ocr_mod.split("_")[-1]
    # liste_moteur.append(ocr_mod)
    # moteur = set(liste_moteur)
    return ocr_mod

def corpus(chemin):
    ocr_mod="/".join(chemin.split("/")[:3])
    # ocr_mod = ocr_mod.split("_")[0]
    return ocr_mod


def stocker(chemin, contenu):
    w = open(chemin, "w")
    w.write(json.dumps(contenu, indent=2))
    w.close()
    # print(chemin)
    return chemin

path_corpora = "../DATA_ELTeC_spaCy3.5.1_ENliste/DATA_ELTeC-Por_spaCy3.5.1/*"
dico_resultat={}

for gen_path in glob.glob(path_corpora):
    print("_____________",gen_path)
    corp = corpus(gen_path)
    print(corp)
    paths_ocr="%s/*OCR/*/NER/*liste.json" % gen_path
    paths_ref = "%s/*REF/NER/*liste.json" % gen_path
    # dico_resultat={}
    for path_ocr in glob.glob(paths_ocr):
        # print(path_ocr)
        moteur_ocr = model_ocr(path_ocr)
        data_ocr=lire_json(path_ocr)
        # print(data_ocr)
        # data_ocr=set(data_ocr)
        if moteur_ocr in dico_resultat:
            set_tmp=dico_resultat[moteur_ocr]
            set_tmp+=data_ocr
            dico_resultat[moteur_ocr]= set_tmp

        else:
            dico_resultat[moteur_ocr] = data_ocr

    # print((json.dumps(dico_resultat, indent=2)))

    for path_ref in glob.glob(paths_ref):
        # print(path_ref)
        data_ref=lire_json(path_ref)
        # dico_resultat["Ref"] = data_ref
        if "Ref" in dico_resultat:
            set_tmp_ref=dico_resultat["Ref"]
            set_tmp_ref+=data_ref
            print(set_tmp_ref)
            dico_resultat["Ref"]= set_tmp_ref

        else:
            dico_resultat["Ref"] = data_ref
    #
    #
    #
    # print(dico_resultat)
    stocker("%s_moteurOCR-global.json"%corp,dico_resultat)



