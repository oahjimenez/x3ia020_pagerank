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
* **Nombres de workers**: 2,3,4 (5?)
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
| 2 | x | x |
| 3 | x | x |
| 4 | x | x |
| 5 | x | x |

## PySpark Basic
| Nombre de noeuds | Temps d'exécution | Dataproc Job id
| ------------- | ------------- | ------------- |
| 2 | x | x |
| 3 | x | x |
| 4 | x | x |
| 5 | x | x |

## PySpark avec partionnement
Afin d'éviter les shuffles entre join, une mise en place des partition controlé a eté rajouté au script pyspark. Le nombre de partition a eté laissé par défaut (Rajouter implementation pyspark), et pour la function de partitionnement un lambda utilisant les meme partition d'url a ete mis en place.
| Nombre de noeuds | Temps d'exécution | Dataproc Job id
| ------------- | ------------- | ------------- |
| 2 | x | x |
| 3 | x | x |
| 4 | x | x |
| 5 | x | x |

## PIG vs PySpark Basic vs PySpark avec partionnement

* Descriptions de ce qu'on peut voir dans les diagrammes, points a souligner. 
* On appercoit une modeste amelioration par rapport a l'implementation basic pyspark, ce qui suggere qu'une meilleure configuration peut encore etre mis en place pour beneficier du partitionnement controler, ce point et abordé plus en détaille dans la section de conclusions et recommendations.
* Bien préciser si les temps comprend aussi les temps cluster ou seulements les temps d'exec internes du programme

# 3. Meilleur pagerank
Avec cette expérience nous avons obtenu que l'entité avec le plus grand pagerank c'est l'uri **<http://dbpedia.org/resource/Living_people>**, avec un pagerank de **36,794.33**. On présente ci-après le top 10 d'url ayant les meilleur pagerank, issue de 3 itérations de l'algorithme pagerank.
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

# 4. Conclusions et recommendations
note: faire remarque pour les possibilités de changement de temps d'exécution
* Recommendation pour améliorer pyspark -> raffiner la sélection de nombre de partitionneurs pour exploiter au maximum les vertus du partitionBy
* Recommendation exécuter plusieurs fois pour calculer un temps d'exécution moyen.
* Prendre en compre l'utilisation des ressources Google et comment ceux peuvent impacter sur les temps d'exécution

* Défis rencontrés:
* Restrictions crédit, limitations par rapport au nombre de noeuds (1 planté, 6 été pas dispo, pas possible d'executer plusieur configuration de noeuds en paralelle due a la quota, discrepence pagerank pig vs pyspark du au perte de précision
