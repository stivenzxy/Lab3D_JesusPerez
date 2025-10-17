import cadquery as cq

# Parámetros originales
altura_cilindro = 30
radio_cilindro = 5
radio_esfera_grande = 10
radio_esfera_pequena1 = 6
radio_esfera_pequena2 = 4


collar_height = 3
collar_radius = radio_cilindro * 2


top_ref = 12


cilindro = cq.Workplane("XY").cylinder(altura_cilindro, radio_cilindro)


collar = cq.Workplane("XY").workplane(offset=top_ref + collar_height / 2).cylinder(collar_height, collar_radius)


esfera_grande = cq.Workplane("XY").workplane(offset=top_ref + collar_height + radio_esfera_grande).sphere(radio_esfera_grande)

pos_esfera1 = (top_ref + collar_height + radio_esfera_grande) + radio_esfera_grande + radio_esfera_pequena1 * 0.7
esfera_pequena1 = cq.Workplane("XY").workplane(offset=pos_esfera1).sphere(radio_esfera_pequena1)

pos_esfera2 = pos_esfera1 + 2 * radio_esfera_pequena2
esfera_pequena2 = cq.Workplane("XY").workplane(offset=pos_esfera2).sphere(radio_esfera_pequena2)


base_upper_height = 2.5                    
base_upper_radius = radio_cilindro * 1.6 


base_lower_height = 4.5                   
base_lower_radius = radio_cilindro * 2.2   


base_upper_center_z = - base_upper_height / 2


base_lower_center_z = - base_upper_height - base_lower_height / 2


base_upper = cq.Workplane("XY").workplane(offset=base_upper_center_z-9).cylinder(base_upper_height, base_upper_radius)
base_lower = cq.Workplane("XY").workplane(offset=base_lower_center_z-10).cylinder(base_lower_height, base_lower_radius)


resultado = (
    cilindro
    .union(base_upper)
    .union(base_lower)
    .union(collar)
    .union(esfera_grande)
    .union(esfera_pequena1)
    .union(esfera_pequena2)
)

show_object(resultado)