import pandas as pd
from sklearn import ensemble

#Citim datele din fisier
dataFromFile = pd.read_csv("column_3C.dat", sep = ' ', header = None)
#print(dataFromFile)

# Amestecam random datele din DataFrame-ul dataFromFile pentru a obtine o
# distributie mai buna pentru cand impartim in setul de train si de test
dataFromFile = dataFromFile.sample(frac = 1)
#print("Data shuffled:\n", dataFromFile)

#Impartim in setul de antrenare si de testare (75%-25%)
date_train = dataFromFile.iloc[:234, :6]
#print(date_train)
etichete_train = dataFromFile.iloc[:234, 6].tolist()
#print(etichete_train)
date_test = dataFromFile.iloc[234:, :6]
#print(date_test)
etichete_test = dataFromFile.iloc[234:, 6].tolist()
#print(etichete_test)

for i in [0.25, 0.5, 0.85]: #se variaza procentul "in-bag"
    for j in [0.1, 0.5, 0.8]: #se variaza numarul de dimensiuni din nod
        print("Procent \"in-bag\": {0}%".format(i * 100))
        print("Numarul de dimensiuni alese intr-un nod: {0}%".format(j * 100))
        #RandomForest si antrenare
        clf = ensemble.RandomForestClassifier(n_estimators = 10, max_features=j, max_samples=i)
        clf.fit(date_train,etichete_train)
        predictii = clf.predict(date_test)
        #Calculam acuratetea
        k = 0;
        for it in range(len(etichete_test)):
            if etichete_test[it] == predictii[it]:
                k = k + 1
        print("Acuratetea: {0}%\n".format(k/len(etichete_test) * 100))

