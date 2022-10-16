# X3IA020 ALMA - Expérience PageRank Performance
### Faculté des Sciences et des Techniques - Nantes Université  
Gestion des données distribuées à large échelle  
**Professeur**: MOLLI Pascal  
**Étudiants**: RAGAA Mohammed ali ahmed, JIMENEZ Oswaldo  
PageRank - comparaison Pig vs PySpark. Consigne: https://madoc.univ-nantes.fr/mod/assign/view.php?id=1523335 

[1. Introduction - Description de l'expérience](#1-introduction---description-de-lexpérience)  
[2. Exécutions pagerank - Pig vs PySpark](#2-exécutions-pagerank---pig-vs-pyspark)  
[3. Meilleur pagerank](#3-meilleur-pagerank)  
[4. Conclusions et recommendations](#4-conclusions-et-recommendations)

# 1. Introduction - Description de l'expérience
Le but de cette expérience c'est de comparer les performances de l'algorithme [pagerank](https://fr.wikipedia.org/wiki/PageRank), entre une implantation [Pig](https://en.wikipedia.org/wiki/Pig_Latin#:~:text=Pig%20Latin%20is%20a%20language,to%20create%20such%20a%20suffix.) et une implantation [PySpark](https://spark.apache.org/docs/latest/api/python/). Cette expérience est inspiré d'une expérience realisée lors de la conférence [NDSI 2012 présentation des Resilient Distributed Datasets (RDD)](https://www.youtube.com/watch?v=dXG4yC8ICEI).

On compare les temps d'exécutions du pagerank avec des diagrammes dans la [section 2]((#2-exécutions-pagerank---pig-vs-pyspark)  ), ensuite les meilleurs pagerank trouvés sont illustrés dans la [section 3]((#3-meilleur-pagerank) ). Des conclusions basées sur ces comparaison et le déroulement de l'experience sont abordés dans la [section 4](#4-conclusions-et-recommendations).

Ci-apres on enumére les configurations et considérations tenus en compte lors des exécutions Pig et PySpark.

## 1.1 Configurations utilisées
Afin de messurer la performance d'exécution entre les implementations Pig et Pyspark, nous avons eu recours au service d'exécution de taches [Dataproc](https://cloud.google.com/dataproc?hl=fr) de la suite Google cloud. Les considerations et configurations utilisées pour réaliser cette expérience ce résument ci-après:
* **Paramètres pagerank**: le nombre d'iterations a été fixé à 3, et le facteur pagerank utilisé de {d = 0.85}, pour les deux implementations. 
* **Nombres de workers**: 2, 3, 4 et 5
* **La région**: europe-west1, défini en function de la proximité avec le bucket hebergéant les données d'entrée
* **Dataset d'entrée**: dataset [page_links_en.nt.bz2](http://downloads.dbpedia.org/3.5.1/en/page_links_en.nt.bz2), disponibles sur le bucket publique gs://public_lddm_data//page_links_en.nt.bz2
* **Version PIG installé dans le cluster**: Apache Pig version 0.18.0-SNAPSHOT
* **Version pyspark installé dans le cluster**: 

Implementations du pagerank utilisées:
* Implementation Pig (copyright pascal) 
* Implementation PySpark (copyright pascal) 
* Implementation PySpark partition controle 

Les resultats de l'execution avec les configurations cites sont presentes dans la section suivante.
# 2. Exécutions pagerank - Pig vs PySpark
* On presente le temps d'execution pris par les deux implementations, en function de nombre de worker utilisés. Pour l'implementation pyspark, on sépare le temps d'execution sans et avec partition.

## PIG
| Nombre de noeuds | Temps d'exécution  | Dataproc Job id
| ------------- | ------------- | ------------- |
| 2 | 49 min 52 sec | 83edf25aa5e24364a1ea968a99ab415f |
| 3 | 37 min 25 sec | 85961f8339bc43bcbaf5cf69cd13719d |
| 4 | 34 min 34 sec | 6d80276d638d4d0096f0d2bbad55debc |
| 5 | 29 min 45 sec | 1ad6eaf435d24191878899943ae73a15 |

## PySpark Basic
| Nombre de noeuds | Temps d'exécution | Dataproc Job id
| ------------- | ------------- | ------------- |
| 2 | 43 min 30 sec | 895b7b281f794d4393278962e01169ad |
| 3 | 38 min 23 sec | 527ace71d1ce4f9da1b5f5ab5581c2dd |
| 4 | 35 min 28 sec | e870244c239b47e1bf2e6c86691d4bfa |
| 5 | 35 min 04 sec | 9d52c020836c41cba2c50e3da3de29e7 |

## PySpark avec partionnement
Afin d'éviter les shuffles entre join, une mise en place des partition controlé a eté rajouté au script pyspark. Le nombre de partition a eté laissé par défaut (Rajouter implementation pyspark), et pour la function de partitionnement un lambda utilisant les meme partition d'url a ete mis en place.
| Nombre de noeuds | Temps d'exécution | Dataproc Job id
| ------------- | ------------- | ------------- |
| 2 | 42 min 48 sec | 71dd624351af42128d8d321c5fc314dd |
| 3 | 31 min 41 sec | f0c04b5b485b4504952c75b7e51b3e44 |
| 4 | 29 min 12 sec | 3f475ada46de4c7ab8e0ca526c1ed5a5 |
| 5 | 30 min 20 sec | 98c8047900634a33882b2296b8a8293a |

## PIG vs PySpark Basic vs PySpark avec partionnement

* Descriptions de ce qu'on peut voir dans les diagrammes, points a souligner. 
* On appercoit une modeste amelioration par rapport a l'implementation basic pyspark, ce qui suggere qu'une meilleure configuration peut encore etre mis en place pour beneficier du partitionnement controler, ce point et abordé plus en détaille dans la section de conclusions et recommendations.
* Bien préciser si les temps comprend aussi les temps cluster ou seulements les temps d'exec internes du programme
<img align=center src= https://github.com/oahjimenez/x3ia020_pagerank/blob/main/comp_diag.png>
<br/>

* Pyspark basic et partionné montre etre plus performant que Pig quand on met pas en place une amélioration externe (augmentation nombre de workeurs)
* pyspark avec partionnement controlé est plus performant que Pig et que sa version sans partionement, pourtant il arrive a un soeil a un nombre de workeurs donnée, ou il est ratrappé par Pig
* A partir de 3 noeuds, Pyspark avec partionnement controle est plus performant que Pyspark Basic
* Quant a Pyspark basic, on apercoit qu'il est plus performant que Pig au debut, et ensuit entre 3 et 4 worker il est ratrappé par Pig. A partir d'un nombre de workeur donnée, dans ce cas, 5, Pig devient plus performant. 
* Pig bénefici plus de l'augmentation dans le nombre de workers, on peut apercevoir cela surtout dans l'increment de nombre de noueds de 4 a 5, ou on voit que pyspark maintient sont temps d'execution tandis que Pig continue a reduire le temps d'execution



# 3. Meilleur pagerank
Avec cette expérience nous avons obtenu que l'entité avec le plus grand pagerank c'est l'uri <http://dbpedia.org/resource/Living_people>, avec un pagerank de **36,794.33**. On présente ci-après le top 10 d'url ayant les meilleur pagerank, issue de 3 itérations de l'algorithme pagerank.
| Rank | Url  | Pagerank |
| ---- | ------------- | ------------- |
|:1st_place_medal:| http://dbpedia.org/resource/Living_people | 36794.33146754463  |
|:2nd_place_medal:| http://dbpedia.org/resource/United_States | 13201.340151981207  |
|:3rd_place_medal:| http://dbpedia.org/resource/Race_and_ethnicity_in_the_United_States_Census | 10371.162005541351  |
|4| http://dbpedia.org/resource/List_of_sovereign_states  | 5195.34736186218  |
|5| http://dbpedia.org/resource/United_Kingdom  | 4923.82130931521  |
|6| http://dbpedia.org/resource/Year_of_birth_missing_%28living_people%29  | 4615.7939763369795  |
|7| http://dbpedia.org/resource/France  | 4595.730518177778  |
|8| http://dbpedia.org/resource/Germany  | 4111.195621667528  |
|9| http://dbpedia.org/resource/Canada  | 3765.46156061246 |
|10| http://dbpedia.org/resource/Animal  | 3692.395898434714  |

Répondre a la question: résultats calculés avec Pig ou pyspark? résultats similaires ou différents?
Quant a l'implementation Pig, il serait donc recommendé d'utiliser des types long pour éviter les [pertes de précisions](https://www.oreilly.com/library/view/programming-pig/9781449317881/ch04.html)   

# 4. Conclusions et recommendations
note: faire remarque pour les possibilités de changement de temps d'exécutio
* Il faut tenir en compte que les programmers s'executent dans le contexte des cluster google dans des machines suceptibles de prendre plus de temps d'execution de leur disponibilite et utilisation, ce qui peut impacter les temps d'executions
* Recommendation pour améliorer pyspark -> raffiner la sélection de nombre de partitionneurs pour exploiter au maximum les vertus du partitionBy, compte tenus que dans cette expérience nous avons eu recours au calcul de nombre de partition par defaut de pySpark
* Recommendation exécuter plusieurs fois pour calculer un temps d'exécution moyen.
* Prendre en compre l'utilisation des ressources Google et comment ceux peuvent impacter sur les temps d'exécution
* Plus facile de faire du benchmarking et modifications (e.g. calcul max) sur l'implémentation pyspark, du au fait que Pig c'est du code integré tandis que PySpark c'est sur python
* Tester Pig avec des types double, long pour determiner quel type de données minimise la perte de précision

* Défis rencontrés:
* Restrictions crédit, limitations par rapport au nombre de noeuds (1 planté, 6 été pas dispo, pas possible d'executer plusieur configuration de noeuds en paralelle due a la quota, discrepence pagerank pig vs pyspark du au perte de précision
