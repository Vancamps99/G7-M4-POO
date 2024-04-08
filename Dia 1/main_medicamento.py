from medicamento import Medicamento #importar la clase definida

#instancia o creación de un objeto
paracetamol=Medicamento()
aspirina=Medicamento()

print(paracetamol)
print(aspirina  )

paracetamol.IVA=0.25
print(paracetamol.IVA)
print(aspirina.IVA)
#Solo se modifico el iva del parecetamol 