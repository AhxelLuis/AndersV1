import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Asignación de Niveles",
    page_icon="anders_logo.png"  # Reemplaza con el nombre de tu archivo
)

data = pd.read_excel("Datacentrosdecosto.xlsx")
datavendedor = pd.read_excel("Datavendedor.xlsx")


def main():

    st.title("Asignación de niveles")

    st.dataframe(data)
    st.dataframe(datavendedor)

    # eleccion bc

    opcionbc = st.selectbox(
        'Ingresa BC:', data['Nivel 1'].dropna().unique()
    )

    codigo_bc = data.loc[data['Nivel 1'] == opcionbc, 'Codigo 1'].iloc[0]

    # eleccion bt

    opcionbt = st.selectbox(
        'Ingresa BT:', data['Nivel 2'].dropna().unique()
    )

    codigo_bt = data.loc[data['Nivel 2'] == opcionbt, 'Codigo 2'].iloc[0]

    bu_options = {
    
    "Socios": [
        "Socios"
    ],
    "Directorio": [
        "Directorio"
    ],
    "Gerencia General": [
        "Gerencia General"
    ],
    "B1": [
        "Conversion y Empaque", 
        "Galvanoplastia", 
        "Papel y Tratamiento de Aguas", 
        "Plasticos", 
        "Caucho, Poliuretano y Comp.", 
        "Petroleo y Gas", 
        "Procesos de Fabricacion"
    ],
    "B2": [
        "Pinturas, Tintas y Adhesivos", 
        "Construccion y Asfalto", 
        "Textiles y Cueros", 
        "Agroquimicos", 
        "Laboratorios"
    ],
    "B3": [
        "Cuidado Personal y del Hogar", 
        "Farmaceuticos y Veterinario", 
        "Alimentos y Nutricion Humana", 
        "Nutricion Animal"
    ],
    "C1": [
        "Productos para Bebes", 
        "Productos de Limpieza"
    ],
    "Administracion y Finanzas": [
        "Administracion", 
        "Sistema Integral de Gestion", 
        "Contabilidad", 
        "Creditos y Cobranzas", 
        "Control y Gestion", 
        "Legal", 
        "Recursos Humanos", 
        "Tesoreria", 
        "Tecnologia de la Informacion"
    ],
    "Marketing e Intel. Mercado": [
        "Marketing e Intel. Mercado"
    ],
    "Logistica": [
        "Operaciones", 
        "Asuntos Regulatorios", 
        "Compras", 
        "Comercio Exterior", 
        "Inmobiliaria"
    ],
    "Inmobiliaria": [
        "Inmobiliaria"
    ]
}.get(opcionbt, ["Sin opciones disponibles"])



    # eleccion bu

    opcionbu = st.selectbox('Ingresa BU:', bu_options)

    codigo_bu = data.loc[data['Nivel 3'] == opcionbu, 'Codigo 3']
    codigo_bu = codigo_bu.iloc[0] if not codigo_bu.empty else "Sin código disponible"

    bs_options = {

    "Socios": [
        "Socios"
    ],
    "Directorio": [
        "Directorio"
    ],
    "Gerencia General": [
        "Gerencia General"
    ],
    "Conversion y Empaque": [
        "Banda Ancha", "Banda Angosta", "Corrugado"
    ],
    "Galvanoplastia": [
        "Acabado Generales de Metales", "Metales Preciosos"
    ],
    "Papel y Tratamiento de Aguas": [
        "Papel", "Tratamiento de Aguas"
    ],
    "Plasticos": [
        "Plasticos"
    ],
    "Caucho, Poliuretano y Comp.": [
        "Caucho", "Poliuretano", "Compuestos"
    ],
    "Petroleo y Gas": [
        "Petroleo", "Gas", "Biodiesel"
    ],
    "Procesos de Fabricacion": [
        "Procesos de Fabricacion"
    ],
    "Pinturas, Tintas y Adhesivos": [
        "Pinturas", "Tintas", "Adhesivos"
    ],
    "Construccion y Asfalto": [
        "Construccion", "Asfalto", "Explosivos"
    ],
    "Textiles y Cueros": [
        "Textiles", "Cueros"
    ],
    "Agroquimicos": [
        "Agroquimicos"
    ],
    "Laboratorios": [
        "Laboratorios"
    ],
    "Cuidado Personal y del Hogar": [
        "Cuidado Personal", "Cuidado del Hogar e Higiene"
    ],
    "Farmaceuticos y Veterinario": [
        "Farmaceuticos", "Veterinario"
    ],
    "Alimentos y Nutricion Humana": [
        "Alimentos", "Nutricion Humana"
    ],
    "Nutricion Animal": [
        "Nutricion Animal"
    ],
    "Productos para Bebes": [
        "Productos para Bebes"
    ],
    "Productos de Limpieza": [
        "Productos de Limpieza"
    ],
    "Administracion": [
        "Administracion"
    ],
    "Sistema Integral de Gestion": [
        "Sistema Integral de Gestion"
    ],
    "Contabilidad": [
        "Contabilidad"
    ],
    "Creditos y Cobranzas": [
        "Creditos y Cobranzas"
    ],
    "Control y Gestion": [
        "Control y Gestion"
    ],
    "Legal": [
        "Legal"
    ],
    "Recursos Humanos": [
        "Recursos Humanos"
    ],
    "Tesoreria": [
        "Tesoreria"
    ],
    "Tecnologia de la Informacion": [
        "Tecnologia de la Informacion"
    ],
    "Marketing e Intel. Mercado": [
        "Marketing e Intel. Mercado"
    ],
    "Operaciones": [
        "Almacen", "Distribucion", "Facturacion", "Produccion"
    ],
    "Asuntos Regulatorios": [
        "Asuntos Regulatorios"
    ],
    "Compras": [
        "Compras"
    ],
    "Comercio Exterior": [
        "Comercio Exterior"
    ],
    "Inmobiliaria": [
        "Inmobiliaria"
    ]
}.get(opcionbu, ["Sin opciones disponibles"])

    # eleccion bs

    opcionbs = st.selectbox('Ingresa BS:', bs_options)
    codigo_bs = data.loc[data['Nivel 4'] == opcionbs, 'Codigo 4']
    codigo_bs = codigo_bs.iloc[0] if not codigo_bs.empty else "Sin código disponible"

    # eleccion vendedor
    vendedor_por_pais = {
    "Argentina": [
        "Alexis Ortiz", "Andrea Damianich", "Daniel Lagomarsino", 
        "-Ningún empleado del departamento de ventas-", "Pablo Romeo",
        "Ramiro Buscetto", "Sebastian Rivera", "Sin Comercial",
        "Vicente Tarsia"
    ],
    "Bolivia": [
        "Carola Ardaya","Gerencia", "Jean Pierre Justiniano", 
        "Josue Torrez", "Karlita Jordan","Mariela Aguilera",
        "Milenka Flores", "-Ningún empleado del departamento de ventas-",
        "Oscar Ferrel", "Oscar Valderrama", "Pamela Rivero",
        "Patricia Sandi", "Sin Comercial", "Victor Cachi", "Yamilca Gorostiaga"
    ],
    "Chile": [
        "Alexis Carreño", "Carlos Cardenas","Diego Maldonado",
        "Gerencia", "Gerencia General","Jessica Bastias",
        "Lorena Garcia","Natalia Cid", "-Ningún empleado del departamento de ventas-",
        "Paulina Jofre", "Ruben Zamora", "Sin Comercial", "Soledad Sanchez",
        "Yanara Fuentes"
    ],
    "Colombia": [
        "Eliana Roberto", "Gustavo Medina", 
        "Jose Gomez", "Kelly Cordoba", 
        "Neymer Reyes", "-Ningún empleado del departamento de ventas-", 
        "Peter Anders Hornung", "Sandra Rojas", "Sin Comercial"
    ],
    "Ecuador": [
        "Alexander Piedra Cano", "Carol Barahona", "Esteban Flores G.",
        "Gerencia", "Gonzalo Benavides", "Jaime Betancourt",
        "-Ningún empleado del departamento de ventas-",
        "Pablo Perez", "Paola Acosta", "Sin Comercial", "Suheil Palma"
    ],
    "Peru": [
        "Alexander Becerra", "Aracely Mori", "Beatriz Sanchez", 
        "Carlos Caballero", "Carlos Quiroz", "Cesar Avila",
        "Christopher Tasayco", "Elsa Gonzales", "Emigio Gamboa", "Enzo Carpio", 
        "Erick Montes", "Fernando Sobrado", "Florian Ramirez",
        "Frank Saravia", "Gabriel Burga", "Gabriela Anavitarte", 
        "Gianina Anders", "Horst Eichhorn", "Jaasiel Melillo",
        "Jose Anticona", "Lesly Diaz", "Mario Flores", "-Ningún empleado del departamento de ventas-",  
        "Paolo Revilla", "Pedro Levano", 
        "Peter M. Anders Hornung", "Ricardo Palma",
        "Rodrigo Ma", "Ronald Arredondo", "Sin Comercial",
        "Valeria Grimaldi", "Walter Briceno"
    ]
}.get(opcionbc, ["Sin vendedores disponibles"])


    opcionvendedor = st.selectbox('Ingresa Vendedor:', vendedor_por_pais)
    codigo_vendedor = datavendedor.loc[datavendedor['Vendedor'] == opcionvendedor, 'slpcode'].iloc[0]




    docentry = st.text_input("Ingresa un número para docentry:")
    
   
    if docentry:

        update_sql = f"""

        SELECT U_AND_DNIVEL1, U_AND_DNIVEL2, U_AND_DNIVEL3, U_AND_DNIVEL4, slpcode
        FROM INV1
        WHERE docentry = {docentry}

        UPDATE INV1
        SET 
            OcrCode = '{codigo_bc}',
            U_AND_DNIVEL1 = '{opcionbc}',
            ocrcode2 = '{codigo_bt}',
            U_AND_DNIVEL2 = '{opcionbt}',
            OcrCode3 = '{codigo_bu}', 
            U_AND_DNIVEL3 = '{opcionbu}',
            Ocrcode4 = '{codigo_bs}',
            U_AND_DNIVEL4 = '{opcionbs}',
            CogsOcrCod = '{codigo_bc}',
            CogsOcrCo2 = '{codigo_bt}', 
            CogsOcrCo3 = '{codigo_bu}',
            CogsOcrCo4 = '{codigo_bs}',
            slpcode = '{codigo_vendedor}'
        WHERE docentry = {docentry}
        """

        
        st.subheader("Consulta SQL:")
        st.code(update_sql, language="sql")

    
    st.write('Elección final:')
    st.write(f"BC: {opcionbc} - Código BC: {codigo_bc}")
    st.write(f"BT: {opcionbt} - Código BT: {codigo_bt}")
    st.write(f"BU: {opcionbu} - Código BU: {codigo_bu}")
    st.write(f"BS: {opcionbs} - Código BS: {codigo_bs}")
    st.write(f"BS: {opcionvendedor} - Código Vendedor: {codigo_vendedor}")

main()
