#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk

def clique(botao):
   botao.set_label("Clicou no botao")

janela = gtk.Window()
janela.connect("delete-event", gtk.main_quit)
botao = gtk.Button("www.GeeksBR.com")
botao.connect("clicked", clique)
janela.add(botao)
janela.show_all()
gtk.main()
