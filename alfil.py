import cadquery as cq


altura_cilindro = 30
radio_cilindro = 5
radio_esfera_grande = 10
radio_esfera_pequena1 = 6
radio_esfera_pequena2 = 4


collar_height = 3                  
collar_radius = radio_cilindro * 2 


top_of_main = altura_cilindro


cilindro = cq.Workplane("XY").cylinder(altura_cilindro, radio_cilindro)


collar = cq.Workplane("XY").workplane(offset=12+collar_height / 2).cylinder(collar_height, collar_radius)


esfera_grande = cq.Workplane("XY").workplane(offset=12 + collar_height + radio_esfera_grande).sphere(radio_esfera_grande)


pos_esfera1 = (12 + collar_height + radio_esfera_grande) + radio_esfera_grande + radio_esfera_pequena1 * 0.7
esfera_pequena1 = cq.Workplane("XY").workplane(offset=pos_esfera1).sphere(radio_esfera_pequena1)

pos_esfera2 = pos_esfera1 + 2 * radio_esfera_pequena2
esfera_pequena2 = cq.Workplane("XY").workplane(offset=pos_esfera2).sphere(radio_esfera_pequena2)


resultado = cilindro.union(collar).union(esfera_grande).union(esfera_pequena1).union(esfera_pequena2)

show_object(resultado) 