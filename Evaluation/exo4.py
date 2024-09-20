def spliter(phrase, separateurs=",.!?;:\"':"):
  mots = []
  traitement = ""
 
 # Parcours de la phrase pour séparer les mots
  for caractere in phrase:
    # Séparation des mots à la fin de chaque séparateur
    if caractere in separateurs:
      # Ajout du mot dans la liste si il n'est pas vide
      if traitement:
        mots.append(traitement)
        traitement = ""
      mots.append(caractere)
      # Passage à la ligne pour séparer les phrases 
    else:
      traitement += caractere

  # Ajout du dernier mot si nécessaire
  if traitement:
    mots.append(traitement)

  return mots

# Exemple d'utilisation
phrase = "J'ai découvert, Python, cette semaine."
resultats = spliter(phrase)
print(resultats)