# coding: utf-8

__author__ = 'Aimen CHERIF'

class Node:
    def __init__(self, param_data):
        self.data = param_data
        self.link = None

    def __str__(self):
        liste = []
        node = self
        while node.link is not None:
            liste.append(node.data)
            node = node.link
        liste.append(node.data)
        return str(liste)
