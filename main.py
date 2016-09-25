from bs4 import BeautifulSoup
from os.path import join as join_path, dirname
from uuid import uuid1


def generar_conceptos_cfdi(ruta_xml, conceptos, ruta_nueva=''):
    # Obtener el archivo xml
    with open(ruta_xml) as file_xml:
        documento_xml = BeautifulSoup(file_xml.read(), 'xml')
        documento_xml.Conceptos.clear()

        # Genera una lista de tags Concepto
        for concepto in conceptos:
            # Generar un tag Concepto
            tag_concepto = BeautifulSoup(
                '<cfdi:Concepto cantidad="" descripcion="" importe="" unidad="" valorUnitario=""/>', 'xml')
            tag_concepto.Concepto['cantidad'] = concepto['cantidad']
            tag_concepto.Concepto['descripcion'] = concepto['descripcion']
            tag_concepto.Concepto['importe'] = concepto['importe']
            tag_concepto.Concepto['valorUnitario'] = concepto['valorUnitario']
            documento_xml.Conceptos.append(tag_concepto.Concepto)

    # Escribe el nuevo archivo y regresa la ruta
    nuevo_archivo = join_path(dirname(ruta_xml),
                              ruta_nueva if len(ruta_nueva) != 0 else '{0}.xml'.format(str(uuid1())))

    # Guarda el archivo a disco
    with open(nuevo_archivo, 'w') as file_dest:
        file_dest.write(str(documento_xml))
        return nuevo_archivo

    return ''


if __name__ == '__main__':
    print 'Hola Mundo'
