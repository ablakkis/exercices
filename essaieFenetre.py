import tkinter         # import de tkinter
zone_texte = tkinter.Label (text = "premier texte")
# ...
# pour changer de texte
zone_texte.config (text = "second texte")
root = tkinter.Tk ()   # création de la fenêtre principale
# ...
obj = tkinter.Label (text = "zone de texte")
# ...
obj.pack ()            # on ajoute l'objet à la fenêtre principale
root.mainloop ()       # on affiche enfin la fenêtre principal et on attend
                       # les événements (souris, clic, clavier)
