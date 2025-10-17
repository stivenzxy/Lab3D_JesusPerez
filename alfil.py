import cadquery as cq

altura_cilindro = 30
radio_cilindro = 5
radio_esfera_grande = 10
radio_esfera_pequena1 = 6
radio_esfera_pequena2 = 4
punta_cilindro = altura_cilindro / 2

cilindro = cq.Workplane("XY").cylinder(altura_cilindro, radio_cilindro)
esfera_grande = cq.Workplane("XY").workplane(offset=punta_cilindro).sphere(radio_esfera_grande)
pos_esfera1 = punta_cilindro + radio_esfera_grande + radio_esfera_pequena1*0.7
esfera_pequena1 = cq.Workplane("XY").workplane(offset=pos_esfera1).sphere(radio_esfera_pequena1)


pos_esfera2 = pos_esfera1 + 2 * radio_esfera_pequena2
esfera_pequena2 = cq.Workplane("XY").workplane(offset=pos_esfera2).sphere(radio_esfera_pequena2)


resultado = cilindro.union(esfera_grande).union(esfera_pequena1).union(esfera_pequena2)

show_object(resultado)