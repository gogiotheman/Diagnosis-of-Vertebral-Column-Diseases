# Diagnosis-of-Vertebral-Column-Diseases
Avem o bază de date furnizată de un centru ortopedic ce se referă la situația medicală
privind starea coloanei vertebrale a fiecărui pacient si vrem să implementăm un program care să
verifice dacă un pacient suferă de vreuna dintre bolile de coloană analizate. Baza de date, numită
Vertebral Column Data Set (aici), instantiaza 310 pacienti, pentru care asociaza 6 atribute (pelvic 
incidence, pelvic tilt, lumbar lordosis angle, sacral slope, pelvic radius and grade of 
spondylolisthesis) și atribuie o etichetă: normal, hernie de disc sau spondilolistezis. Împărțirea 
pacienților este astfel: Normal (100 patients), Disk Hernia (60 patients) or Spondylolisthesis (150 
patients).
În implementarea codului in Python am folosit bibliotecile pandas - pentru citirea datelor 
din fișierul .dat – și scikit-learn modulul ensemble - pentru folosirea algoritmului Random Forest.
Am antrenat un Random Forest pentru problema noastră de clasificare. 
Înaintea împărțirii în setul de antrenament și test (75-25), amestecăm aleatoriu, la fiecare 
rulare, setul de date, astfel încît să avem pacienții distribuiți cît mai variat în seturi (ei fiind inițial
ordonați după etichetele lor, cînd avem un număr foarte mic de instanțe cu o anumită etichetă 
în setul de train și setul de test unanim cu acea etichetă). Acest lucru îmbunătățește performanța 
programului, acuratețea crescînd pînă la aproximativ 90%; dacă se comentează linia de cod 
dataFromFile = dataFromFile.sample(frac = 1) și nu se mai face, deci, această amestecare, 
observăm că acuratețea calculată scade pînă pe la 30%.
Pentru măsurarea performaței folosim acuratețea (=nr. de predicții corecte/nr. total de 
predicții). Ea se modifică la fiecare rulare, firește – pentru că și datele sunt ordonate altfel la 
împărțirea în seturi – dar variază în jurul a 85%, depinzînd de cum variază procentul “in-bag”
(max_samples) și numărul de dimensiuni din nod (max_features). Notăm mai jos acuratețea 
calculată cu ajutorul programului pentru diferite valori ale celor doi parametri:
Procent "in-bag": 25.0%
Numarul de dimensiuni alese intr-un nod: 10.0%
Acuratetea: 85.52631578947368%
Procent "in-bag": 25.0%
Numarul de dimensiuni alese intr-un nod: 50.0%
Acuratetea: 88.1578947368421%
Procent "in-bag": 25.0%
Numarul de dimensiuni alese intr-un nod: 80.0%
Acuratetea: 86.8421052631579%
Procent "in-bag": 50.0%
Numarul de dimensiuni alese intr-un nod: 10.0%
Acuratetea: 81.57894736842105%
Procent "in-bag": 50.0%
Numarul de dimensiuni alese intr-un nod: 50.0%
Acuratetea: 90.78947368421053%
Procent "in-bag": 50.0%
Numarul de dimensiuni alese intr-un nod: 80.0%
Acuratetea: 86.8421052631579%
Procent "in-bag": 85.0%
Numarul de dimensiuni alese intr-un nod: 10.0%
Acuratetea: 84.21052631578947%
Procent "in-bag": 85.0%
Numarul de dimensiuni alese intr-un nod: 50.0%
Acuratetea: 88.1578947368421%
Procent "in-bag": 85.0%
Numarul de dimensiuni alese intr-un nod: 80.0%
Acuratetea: 85.52631578947368%
Acuratețea nu e neapărat grozavă, dar cred că amestecarea aleatorie a ordinii datelor 
citite e cea mai bună soluție în obținerea unei acurateți cît mai ridicate. 
Ne-am aștepta ca performanța maximă să fie atinsă cu cît dimensiunile din nod sunt mai 
multe și numărul de exemple este mai mare, dar nu e neapărat (cum putem observa în exemplele 
de mai sus, o acuratețe maximă se găsește cînd inițializăm fiecare arbore cu o jumătate din 
exemple și din atribute; la alte rulări, obținem alte rezultate). Oricum, acuratețea se păstrează în 
jurul lui 85% pentru oricare variație a parametrilor, la rulările făcute pînă acum, valoare cu care 
putem fi confortabili
