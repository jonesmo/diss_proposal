import os
from ete3 import Tree, TreeStyle, TextFace, NodeStyle

dirname = os.path.dirname(__file__)


t = Tree() # Creates an empty tree

A_name = " Can we model an individual’s unique perception of sounds?\nWhat features are most perceptually relevant?\nHow much do individuals differ?\nAre there patterns? "
B_name = " How can data engineering and ML training techniques\ncapture the musical values of an artist? "
C_name = " How can machine learning be applied to an artist’s own\npersonal data to yield creative projects they deem meaningful? "

A = t.add_child(name=A_name)
B = t.add_child(name=B_name)
C = t.add_child(name=C_name)

D_name = " Can I make models that imitate individual instrumentalists by training on their data? "
D = C.add_child(name=D_name)

E_name = " Wavenet / approximations "
E = D.add_child(name=E_name)
F_name = " What’s a more efficient way to do audio generation than Wavenet? "
F = D.add_child(name=F_name)
G_name = " Diffusion + Neural Vocoder "
G = F.add_child(name=G_name)
H_name = " Can diffusion + neural vocoder capture the sound of an individual alto flute improviser or drummer? "
H = F.add_child(name=H_name)

# Circular Mode
ts = TreeStyle()
ts.mode = "c" # draw tree in circular mode
ts.arc_start = -45
ts.arc_span = 180

# General
ts.scale = 100
ts.show_scale = False
ts.show_leaf_name = True
# ts.title.add_face(TextFace("Hello ETE", fsize=15), column=1)

# Node Style
for n in t.traverse():
    if n.name == A_name:
        nstyle = NodeStyle()
        nstyle["fgcolor"] = "green"
        nstyle["bgcolor"] = "HotPink"
        nstyle["size"] = 20
        n.set_style(nstyle)
        # n.add_face(TextFace(A_name), column=1)
    elif n.name == B_name:
        nstyle = NodeStyle()
        nstyle["fgcolor"] = "DeepSkyBlue"
        nstyle["bgcolor"] = "DarkOrange"
        nstyle["size"] = 20
        n.set_style(nstyle)
        # n.add_face(TextFace(B_name), column=1)
    elif n.name == C_name:
        nstyle = NodeStyle()
        nstyle["fgcolor"] = "Crimson"
        nstyle["bgcolor"] = "LawnGreen"
        nstyle["size"] = 20
        n.set_style(nstyle)
        n.add_face(TextFace(C_name), column=1)
    elif not n.is_leaf():
        n.add_face(TextFace(n.name), column=0)
        nstyle = NodeStyle()
        nstyle["fgcolor"] = "HotPink"
        nstyle["bgcolor"] = "GreenYellow"
        nstyle["size"] = 20
        n.set_style(nstyle)
    elif n.is_leaf():
        nstyle = NodeStyle()
        nstyle["fgcolor"] = "MediumAquamarine"
        nstyle["bgcolor"] = "PaleGreen"
        nstyle["size"] = 10
        n.set_style(nstyle)

t.img_style["size"] = 30
t.img_style["fgcolor"] = "DeepPink"
t.img_style["bgcolor"] = "Indigo"
t.add_face(TextFace(" Can I train a neural network?  \n Yes (Ragdale) ", fgcolor="White"), column=1)

# # Save file out
out_path = os.path.join(dirname, 'images')
t.render(os.path.join(out_path, "question_tree.png"), w=12, units="in", tree_style=ts, dpi=300)

# # print in terminal
# print(t.get_ascii(show_internal=True))

# # show in its own window
# t.show()