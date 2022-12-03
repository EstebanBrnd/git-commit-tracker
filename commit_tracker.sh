while true
do
git fetch
git pull --quiet                                                  #Les fichiers sont désormais à jour
git log -10 HEAD --pretty=format:%s >com.txt                      #Récupération des 10 derniers messages de commit
git log -10 --pretty=format:'%an' >author.txt                     #Récupération des 10 derniers auteurs de commit
git log -10 --format=%cd >date.txt                                #Récupération des 10 dernieres dates de commit
git log -10 --format=format:"%H" >hash.txt                        #Récupération des 10 derniers hashs de commit
basename -s .git `git config --get remote.origin.url` >name.txt   #Récupération des 10 dernieres listes de fichiers modifiés
git show -10 --name-only --oneline HEAD >sortie.txt               #Récupération des 10 derniers commit-ish de commit
python3 commit_tracker.py                                         #Appel au fichier python pour envoyer le message
rm date.txt                                                       #Suppression de tous les fichiers générés par les fonctions précédentes
rm author.txt
rm com.txt
rm name.txt
rm hash.txt
rm sortie.txt
rm -f commit.txt                                                  #Suppression sans message d'erreur car commit.txt est produit dans commit_tracker.py 
                                                                  #uniquement si il y a eu des modifications
sleep $1                                                          #Pause avant de rafraichir de nouveau
done
