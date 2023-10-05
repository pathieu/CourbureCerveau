#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 14:29:31 2023

@author: mdemartini
"""

import pymesh
#EXTRACTION DES DONNEES

mesh=pymesh.load_mesh("mar0002_recons_nobias_cortex_smooth_hemil_bouchee.mesh")

print(mesh.num_vertices, mesh.num_faces, mesh.num_voxels)
