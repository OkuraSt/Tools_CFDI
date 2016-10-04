from os.path import join as join_path, dirname, abspath, isfile
from main import generar_conceptos_cfdi, generar_xml_uuid_folio
from bs4 import BeautifulSoup

# generar_conceptos_cfdi es una funcion que nos permite modificar
# los conceptos de un cdfi desde una ruta dada, y generar nuevos a
# partir de un arreglo de diccionarios que nos indiquen la informacion
# requerida. La funcion regresa la ruta del nuevo archivo creado la cual
# tambien se puede especificar en el parametro opcional file_to_create.
def test_generar_conceptos_cfdi():
    # Obtener la ruta del archivo
    current_directory = dirname(abspath(__file__))
    filename = join_path(current_directory, '..\\xmls\\2469.xml')

    # Genera un diccionario con la informacion requerida
    lista_conceptos = []
    concepto_1 = {'cantidad': '3',
                  'descripcion': 'Jabones',
                  'importe': '64.2',
                  'unidad': 'PZA',
                  'valorUnitario': '21.4'}
    concepto_2 = {'cantidad': '6',
                  'descripcion': 'Shampoo',
                  'importe': '313.8',
                  'unidad': 'BOT',
                  'valorUnitario': '52.3'}
    lista_conceptos.append(concepto_1)
    lista_conceptos.append(concepto_2)

    ruta_archivo_nuevo = generar_conceptos_cfdi(filename, lista_conceptos)

    # Verificar que el archivo existe
    assert isfile(ruta_archivo_nuevo)
    # Probar que el archivo generado tiene los conceptos enviados
    with open(ruta_archivo_nuevo) as file:
        xml = BeautifulSoup(file.read(), 'xml')
        conceptos = xml.Comprobante.Conceptos.children
        concepto_1_xml = conceptos.next()
        assert concepto_1['cantidad'] == concepto_1_xml['cantidad']
        assert concepto_1['descripcion'] == concepto_1_xml['descripcion']
        assert concepto_1['importe'] == concepto_1_xml['importe']
        assert concepto_1['valorUnitario'] == concepto_1_xml['valorUnitario']
        concepto_2_xml = conceptos.next()
        assert concepto_2['cantidad'] == concepto_2_xml['cantidad']
        assert concepto_2['descripcion'] == concepto_2_xml['descripcion']
        assert concepto_2['importe'] == concepto_2_xml['importe']
        assert concepto_2['valorUnitario'] == concepto_2_xml['valorUnitario']


# generar_xml_uuid_folio es una funcion que nos permitira generar un xml
# basado en otro, al cual se le generara un nuevo uuid, serie y folio
# quedando los demas datos intactos.
def test_generar_xml_uuid_folio():
    # Obtener la ruta del archivo
    current_directory = dirname(abspath(__file__))
    filename = join_path(current_directory, '..\\xmls\\b_3_par.xml')

    ruta_archivo_nuevo = generar_xml_uuid_folio(filename)

    # Verificar que el archivo existe
    assert isfile(ruta_archivo_nuevo)

    # Abrir los 2 archivos y comparar uuid, serie y folio
    with open(ruta_archivo_nuevo) as file:
        xml_nuevo = BeautifulSoup(file.read(), 'xml')

        with open(filename) as file_original:
            xml_original = BeautifulSoup(file_original.read(), 'xml')

            assert xml_nuevo.TimbreFiscalDigital['UUID'] != xml_original.TimbreFiscalDigital['UUID']
            assert xml_nuevo.Comprobante['serie'] != xml_original.Comprobante['serie']
            assert xml_nuevo.Comprobante['folio'] != xml_original.Comprobante['folio']