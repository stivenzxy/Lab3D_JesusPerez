import cadquery as cq

altura_cilindro = 30
radio_cilindro = 5


cilindro = cq.Workplane("XY").cylinder(altura_cilindro, radio_cilindro)

show_object(cilindro)