# X3IA020 ALMA - Expérience PageRank Performance
### Gestion des données distribuées à large échelle
Profeseur: MOLLI Pascal  
Étudiants: RAGAA Mohammed ali ahmed, JIMENEZ Oswaldo 
PageRank - Pig vs PySpark comparison https://madoc.univ-nantes.fr/mod/assign/view.php?id=1523335 

# Description Expérience
* Objetif: comparer les performance d'execution de l'algorithme pagerank, entre une implantation Pig et une implantation PySpark, 
inspire de l'experience fait lors de la conference NDSI 2012.
* on présente également le résultat obtenu de l'experience, notamment les url ayant les meilleur page rank 
* Afin de messurer la performance d'execution entre ces deux implementation, nous avons eu recours a la suite Google cloud.
* On a utilisé des clusters avec plusieurs configuration, notamment en variant le nombre de workers. Nous avons utilisé 2,3,4 (5?) nombre de workers, visant a comparer l'evolution de temp d'executions entre les deux implementations.
* On presente la comparaison avec des diagrammes, et ensuite produit des conclusions basées sur ces comparaison et le deroulement de l'experience
* Configuration pagerank utilisé: 3 itérations, avec des facteurs 0.15 + 0.85* sum (Brief description algo)

Version PIG utilisé:
liens ver implementation PIG (avec des credit et reference au code Pascal)
Version pyspark utilisé: 
liens ver implementation Pyspark (avec des credit et reference au code Pascal)
liens ver implementation Pyspark partition (avec des credit et reference au code Pascal)


# Comparaisons d'exécutions
* On presente le temps d'execution pris par les deux implementations, en function de nombre de worker utilisés. Pour l'implementation pyspark, on sépare le temps d'execution sans et avec partition.

## PIG
Configuration 1: 
Noeuds: 2
Itérations: 3

Exécution 1 (Exécuté par: Mohammed)
Temps d’exécution: 
Job id: 83edf25aa5e24364a1ea968a99ab415f 
Cluster id:  cluster-a35a 
Start time:  14 Oct 2022, 17:06:45
Elapsed time:  49 min 52 sec

Configuration 2: 
Noeuds: 3
Itérations: 3

Exécution a) (Exécuté par: Mohammed)
Temps d’exécution: 
Job id: 85961f8339bc43bcbaf5cf69cd13719d
Cluster id: cluster-a35a
Start time: 14 Oct 2022, 19:45:41  
Elapsed time:  37 min 25 sec


Configuration 3: 
Noeuds: 4
Itérations: 3

Exécution a) (Exécuté par: Mohammed)
Temps d’exécution: 
Job id: 6d80276d638d4d0096f0d2bbad55debc
Cluster id:  cluster-a35a
Start time:  14 Oct 2022, 18:59:22
Elapsed time:  34 min 34 sec



## PYSPARK BASIC
Configuration 1: 
Noeuds: 2
Itérations: 3


Exécution a) (Exécuté par: OSWALDO)
Temps d’exécution: 
Job id: 895b7b281f794d4393278962e01169ad
Cluster id: cluster-a35a
Start time: Oct 14, 2022, 10:15:21 AM
Elapsed time: 43 min 30 sec


Configuration 2: 
Noeuds: 3
Itérations: 3

Exécution a) (Exécuté par: - Amine )
Job id: 527ace71d1ce4f9da1b5f5ab5581c2dd 
Cluster id: cluster-a35a 
Start time: 14 oct. 2022, 18:52:25
Elapsed time: 38 min 23 s 



Configuration 3: 
Noeuds: 4
Itérations: 3


Exécution a) (Exécuté par: OSWALDO)
Temps d’exécution: 
Id cluster: e870244c239b47e1bf2e6c86691d4bfa
Cluster name: cluster-a35a
Start time: Oct 14, 2022, 11:30:05 AM
Elapsed time: 35 min 28 sec



## PYSPARK PARTITION
Afin d'éviter les shuffles entre join, une mise en place des partition controlé a eté rajouté au script pyspark. Le nombre de partition a eté laissé par défaut (Rajouter implementation pyspark), et pour la function de partitionnement un lambda utilisant les meme partition d'url a ete mis en place.

Configuration 1: 
Noeuds: 2
Itérations: 3

Exécution 1 (Exécuté par: - Mohammed )
Temps d’exécution: 
Job id: 895b7b281f794d4393278962e01169ad
Cluster id: cluster-a35a
Start time: Oct 14, 2022, 10:15:21 AM
Elapsed time: 43 min 30 sec



Configuration 2: 
Noeuds: 3
Itérations: 3
Exécution 1 (Exécuté par: - Mohammed )
Temps d’exécution: 
Job id: 895b7b281f794d4393278962e01169ad
Cluster id: cluster-a35a
Start time: Oct 14, 2022, 10:15:21 AM
Elapsed time: 43 min 30 sec



Exécution 1 (Exécuté par: Mohammed)
Temps d’exécution:

Configuration 3: 
Noeuds: 4
Itérations: 3

Temps d’exécution: 
Job id: 895b7b281f794d4393278962e01169ad
Cluster id: cluster-a35a
Start time: Oct 14, 2022, 10:15:21 AM
Elapsed time: 43 min 30 sec

Exécution 1 (Personne qui exécute: - )
Temps d’exécution:

* Descriptions de ce qu'on peut voir dans les diagrammes, points a souligner. 
* On appercoit une modeste amelioration par rapport a l'implementation basic pyspark, ce qui suggere qu'une meilleure configuration peut encore etre mis en place pour beneficier du partitionnement controler, ce point et abordé plus en détaille dans la section de conclusions et recommendations.

# Meilleur pagerank
On présente les url ayant les meilleur pagerank issue de 3 itérations.
| Url  | Pagerank |
| ------------- | ------------- |
| :1st_place_medal: http://dbpedia.org/resource/Living_people  | 36794.33146754463  |
| :2nd_place_medal: http://dbpedia.org/resource/United_States  | 13201.340151981207  |
| :3rd_place_medal: http://dbpedia.org/resource/Race_and_ethnicity_in_the_United_States_Census  | 10371.162005541351  |
| http://dbpedia.org/resource/List_of_sovereign_states  | 5195.34736186218  |
| http://dbpedia.org/resource/United_Kingdom  | 4923.82130931521  |
| http://dbpedia.org/resource/Year_of_birth_missing_%28living_people%29  | 4615.7939763369795  |
| http://dbpedia.org/resource/France  | 4595.730518177778  |
| http://dbpedia.org/resource/Germany  | 4111.195621667528  |
| http://dbpedia.org/resource/Canada  | 3765.46156061246 |
| http://dbpedia.org/resource/Animal  | 3692.395898434714  |

# Conclusions et recommendations
note: faire remarque pour les possibilités de changement de temps d'exécution
* Recommendation pour améliorer pyspark -> raffiner la sélection de nombre de partitionneurs pour exploiter au maximum les vertus du partitionBy
