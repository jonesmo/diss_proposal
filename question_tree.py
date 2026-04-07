import os
from ete3 import Tree, TreeStyle, TextFace, NodeStyle

dirname = os.path.dirname(__file__)


t = Tree() # Creates an empty tree

A = t.add_child(name="A")
B = t.add_child(name="B")
C = t.add_child(name="C")

D = C.add_child(name="D")

# Circular Mode
ts = TreeStyle()
ts.mode = "c" # draw tree in circular mode
ts.arc_start = -45
ts.arc_span = 135

# General
ts.scale = 50
ts.show_scale = False
ts.show_leaf_name = True
ts.title.add_face(TextFace("Hello ETE", fsize=15), column=1)

# Node Style
for n in t.traverse():
    if n.is_leaf():
        nstyle = NodeStyle()
        nstyle["fgcolor"] = "red"
        nstyle["size"] = 10
        n.set_style(nstyle)
    else:
        n.add_face(TextFace(n.name), column=0)
        nstyle = NodeStyle()
        nstyle["fgcolor"] = "green"
        nstyle["size"] = 10
        n.set_style(nstyle)

t.img_style["size"] = 20
t.img_style["fgcolor"] = "blue"
t.add_face(TextFace("R"), column=1)

# # Save file out
out_path = os.path.join(dirname, 'images')
t.render(os.path.join(out_path, "question_tree.png"), w=183, units="mm", tree_style=ts)

# # print in terminal
# print(t.get_ascii(show_internal=True))

# # show in its own window
# t.show()