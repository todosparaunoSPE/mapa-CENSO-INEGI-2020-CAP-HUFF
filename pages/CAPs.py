# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:30:00 2024

@author: jperezr
"""

import folium
import branca
# creamos el mapa de nuevo para partir de 0
mi_mapa = folium.Map(location=(21.886228789501768, -102.28507865221279), zoom_start=8)
# La información de los popups la añadiremos usando branca
# La información solo será la posición del marcador
# os dejo a vosotros la innovación

#AGUASCALIENTES
html = "<p>Ciudad: Aguascalientes</p><p>CAP AGUASCALIENTES</p><p>No. de oficina 019</p><p>Calle: AV ADOLFO LOPEZ MATEOS OTE. 323 ORIENT</p><p>Col. Centro</p><p>C.P. 20000</p>"
iframe1 = branca.element.IFrame(html=html, width=500, height=300)

html = "<p>ciudad: Aguascalientes</p><p>CAP AGUASCALIENTES SUPERISSSTE</p><p>No. de oficina 0060</p><p>Calle: PROLONGACION ZARAGOZA</p><p>Colonia: SAN PABLO</p><p>C.P. 20050</p>"
iframe2 = branca.element.IFrame(html=html, width=500, height=300)

#BAJA CALIFORNIA
html = "<p>Ciudad: Mexicali</p><p>CAP Mexicali</p><p>No. de oficina 0025</p><p>Calle: BLVD BENITO JUAREZ 1298</p><p>Col. FRACC JARDINES DEL VALLE</p><p>C.P 21270</p>"
iframe3 = branca.element.IFrame(html=html, width=500, height=300)

html = "<p>Ciudad: Tijuana</p><p>CAP La Paz</p><p>No. de oficina 0012</p><p>Calle: BLVD INSURGENTES 18015 L H1</p><p>Col. RIO TIJUANA TERCERA ETAPA</p><p>C.P. 22226</p>"
iframe4 = branca.element.IFrame(html=html, width=500, height=300)

#BAJA CALIFORNIA SUR
html = "<p>Ciudad: La Paz</p><p>CAP La Paz</p><p>No. de oficina 0012</p><p>Calle: MEXICO CASI ESQ NICOLAS BRAVO </p><p>Col. Centro</p><p>C.P. 23000</p>"
iframe5 = branca.element.IFrame(html=html, width=500, height=300)

#CAMPECHE

html = "<p>Ciudad: Campeche</p><p>CAP Campeche</p><p>No. de oficina 0017</p><p>Calle: RICARDO CASTILLO OLIVER, SN TORRE A</p><p>Col. SAN FRANCISCO</p><p>C.P. 24010</p>"
iframe6 = branca.element.IFrame(html=html, width=500, height=300)


#CIUDAD DE MEXICO

html = "<p>Ciudad: Ciudad de México</p><p>CAP BUENAVISTA</p><p>No. de oficina 0001</p><p>Calle: AV JESUS GARCIA, 140</p><p>Col. Centro</p><p>C.P. 06350</p>"
iframe7 = branca.element.IFrame(html=html, width=500, height=300)

html = "<p>Ciudad: Ciudad de México</p><p>CAP EUGENIA</p><p>No. de oficina 0033</p><p>Calle: EUGENIA, 197</p><p>Col. Centro</p><p>C.P. 03020</p>"
iframe8 = branca.element.IFrame(html=html, width=500, height=300)

html = "<p>Ciudad: Ciudad de México</p><p>CAP MAGNA SUR</p><p>No. de oficina 0046</p><p>Calle: CALZADA DE LOS LEONES, 253</p><p>Col. Centro</p><p>C.P. 01010</p>"
iframe9 = branca.element.IFrame(html=html, width=500, height=300)

html = "<p>Ciudad: Ciudad de México</p><p>CAP VILLA COAPA</p><p>No. de oficina 0057</p><p>Calle: ESCUELA NAVAL MILITAR, s/n</p><p>Col. Centro</p><p>C.P. 04800</p>"
iframe10 = branca.element.IFrame(html=html, width=500, height=300)

html = "<p>Ciudad: Ciudad de México</p><p>CAP CULHUACÁN</p><p>No. de oficina 0059</p><p>Calle: AV SANTA ANA</p><p>Col. Centro</p><p>C.P. 04480</p>"
iframe11 = branca.element.IFrame(html=html, width=500, height=300)

html = "<p>Ciudad: Ciudad de México</p><p>CAP Vasconcelos</p><p>No. de oficina 0063</p><p>Calle: AV JOSE VASCONCELOS, 221</p><p>Col. Centro</p><p>C.P. 11850</p>"
iframe12 = branca.element.IFrame(html=html, width=500, height=300)

#CHIAPAS

html= "<p>Ciudad: TUXTLA GUTIERREZ</p><p>CAP TUXTLA GTZ</p><p>No. de oficina 0015</p><p>Calle: 11 ORIENTE SUR, s/n</p><p>Col. TZOCOTUMBAK</p><p>C.P. 29000</p>"
iframe13=branca.element.IFrame(html=html, width=500, height=300)

html= "<p>Ciudad: TAPACHULA</p><p>CAP TAPACHULA</p><p>No. de oficina 0039</p><p>Calle: AV TUXTEPEC Y OAXACA, s/n </p><p>Col. FRANCISCO VILLA</p><p>C.P. 30740</p>"
iframe14=branca.element.IFrame(html=html, width=500, height=300)


html="<p>Ciudad: SAN CRISTOBAL DE LAS CASAS</p><p>CAP San Cristobal de las Casas</p><p>No. de oficina 0061</p><p>Calle: AV BELISARIO DOMINGUEZ, s/n</p><p>Col. 14 DE SEPTIEMBRE</p><p>C.P. 29120</p>"
iframe15=branca.element.IFrame(html=html, width=500, height=300)


#CHIHUAHUA

html="<p>Ciudad: Chihuahua</p><p>CAP Chihuahua</p><p>No. de oficina 0011</p><p>Calle: OCEANO PACIFICO, 3620</p><p>Col. Centro</p><p>C.P. 31206</p>"
iframe16=branca.element.IFrame(html=html, width=500, height=300)

html="<p>Ciudad: Ciudad Juárez</p><p>CAP CD. JUAREZ</p><p>No. de oficina 0037</p><p>Calle: AV PASEO DEL TRIUNFO, 4630</p><p>Col. Centro</p><p>C.P. 32310</p>"
iframe17=branca.element.IFrame(html=html, width=500, height=300)


#COAHUILA

html= "<p>Ciudad: Saltillo</p><p>CAP SALTILLO (LA JOYA)</p><p>No. de oficina 0003</p><p>Calle: BLVD SALTILLO, 509</p><p>Col. DE LOS MAESTROS</p><p>C.P. 25260</p>"
iframe18=branca.element.IFrame(html=html, width=500, height=300)


html= "<p>Ciudad: Ramos Arizpe</p><p>CAP RAMOS ARIZPE</p><p>No. de oficina 0053</p><p>Calle: BLVD PLAN DE GUADALUPE, 1200 L LB0</p><p>Col. FIDEL VELAZQUEZ</p><p>C.P. 25900</p>"
iframe19=branca.element.IFrame(html=html, width=500, height=300)

#COLIMA

html= "<p>Ciudad: Colima</p><p>CAP Colima</p><p>No. de oficina 0022</p><p>Calle: AV MARIA AHUMADA DE GOMEZ, 100</p><p>Col. SENDEROS DEL CARMEN</p><p>C.P. 28979</p>"
iframe20=branca.element.IFrame(html=html, width=500, height=300)

#DURANGO

html= "<p>Ciudad: Durango</p><p>CAP EUGENIA</p><p>No. de oficina 0021</p><p>Calle: BRUNO MARTINEZ, 520 NTE</p><p>Col. Zona Centro</p><p>C.P. 34000</p>"
iframe21=branca.element.IFrame(html=html, width=500, height=300)

html= "<p>Ciudad: Gómez Palacio</p><p>CAP EUGENIA</p><p>No. de oficina 0038</p><p>Calle: BLVD MIGUEL ALEMAN, s/n</p><p>Col. Centro</p><p>C.P. 35000</p>"
iframe22=branca.element.IFrame(html=html, width=500, height=300)

#ESTADO DE MEXICO

html= "<p>Ciudad: Estado de México</p><p>CAP TOLUCA</p><p>No. de oficina 0006</p><p>Calle: AV IND OTE ESQ ROBERT FULTON, 1808</p><p>Col. ZONA INDUSTRIAL</p><p>C.P. 50071</p>"
iframe23=branca.element.IFrame(html=html, width=500, height=300)

html= "<p>Ciudad: Estado de México</p><p>CAP IXTAPALUCA</p><p>No. de oficina 0047</p><p>Calle: CARR FED MEXICO CUAUTLA, KM 37 LOCA</p><p>Col. HACIENDA DE STA BARBARA</p><p>C.P. 56530</p>"
iframe24=branca.element.IFrame(html=html, width=500, height=300)

html= "<p>Ciudad: Estado de México</p><p>CAP TULTITLÁN</p><p>No. de oficina 0048</p><p>Calle: AV MEXIQUENSE MAXI PLAZA TUl, 4 LOCAL S</p><p>Col. EX HACIENDA LOS PORTALES</p><p>C.P. 54910</p>"
iframe25=branca.element.IFrame(html=html, width=500, height=300)


html= "<p>Ciudad: Estado de México</p><p>CAP CUAUTITLÁN IZCALLI</p><p>No. de oficina 0049</p><p>Calle: AV HUEHUETOCA PZA LAS HDAS, s/n LOC LE0</p><p>Col. EX HACIENDA DE SAN MIGUEL</p><p>C.P. 54715</p>"
iframe26=branca.element.IFrame(html=html, width=500, height=300)

html= "<p>Ciudad: Estado de México</p><p>CAP ECATEPEC</p><p>No. de oficina 0055</p><p>Calle: s/n LOC L H</p><p>Col. SANTA CRUZ VENTA DE CARPIO</p><p>C.P. 55065</p>"
iframe27=branca.element.IFrame(html=html, width=500, height=300)

#GUANAJUATO

html= "<p>Ciudad: Celaya</p><p>CAP Celaya</p><p>No. de oficina 0020</p><p>Calle: AV FRANCISCO JUAREZ, s/n</p><p>Col. LOS LAURELES</p><p>C.P. 38144</p>"
iframe28=branca.element.IFrame(html=html, width=500, height=300)

html= "<p>Ciudad: León</p><p>CAP León</p><p>Calle: BLVD. MARIANO ESCOBEDO PONIENTE Y BLVD. FRANCISCO GONZÁLEZ BOCANEGRA</p><p>EL TLACUACHE</p><p>C.P. 37526</p>"
iframe29=branca.element.IFrame(html=html, width=500, height=300)


#GUERRERO

html= "<p>Ciudad: Acapulco</p><p>CAP Acapulco</p><p>No. de oficina 0035</p><p>Calle: COSTERA MIGUEL ALEMAN, 63</p><p>Col. FRACC CLUB DEPORTIVO</p><p>C.P. 39690</p>"
iframe30=branca.element.IFrame(html=html, width=500, height=300)

#HIDALGO

html= "<p>Ciudad: Pachuca de Soto</p><p>CAP Pachuca</p><p>No. de oficina 0014</p><p>Calle: AV REVOLUCION, 1203</p><p>Col. PERIODISTAS</p><p>C.P. 42060</p>"
iframe31=branca.element.IFrame(html=html, width=500, height=300)

#JALISCO

html= "<p>Ciudad: Guadalajara</p><p>CAP GUADALAJARA</p><p>No. de oficina 0005</p><p>Calle: AV FRAY ANTONIO ALCALDE, 500 PB</p><p>Col. Centro</p><p>C.P. 44100</p>"
iframe32=branca.element.IFrame(html=html, width=500, height=300)

html= "<p>Ciudad: Guadalajara</p><p>CAP GUADALAJARA SUPERISSSTE</p><p>No. de oficina 0058</p><p>Calle: ANTONIO ENRIQUEZ, 50</p><p>Col. SAN ANDRES SECTOR LIBERTAD</p><p>C.P. 44810</p>"
iframe33=branca.element.IFrame(html=html, width=500, height=300)

#MICHOACÁN

html= "<p>Ciudad: Morelia</p><p>CAP Morelia</p><p>No. de oficina 0027</p><p>Calle: PERIFERICO PASEO DE LA REP, 3380 L E02</p><p>Col. EL LAGO 1</p><p>C.P. 58115</p>"
iframe34=branca.element.IFrame(html=html, width=500, height=300)

#MORELOS

html= "<p>Ciudad: Cuernavaca</p><p>CAP Cuernavaca</p><p>No. de oficina 0032</p><p>Calle: AV PLAN DE AYALA, 501</p><p>Col. TEOPANZOLCO</p><p>C.P. 62350</p>"
iframe35=branca.element.IFrame(html=html, width=500, height=300)

#NAYARIT

html= "<p>Ciudad: Tepic</p><p>CAP Tepic</p><p>No. de oficina 0024</p><p>Calle: AV INSURGENTES, 104 PONIEN</p><p>Col. Centro</p><p>C.P. 63000</p>"
iframe36=branca.element.IFrame(html=html, width=500, height=300)

#NUEVO LEON

html= "<p>Ciudad: Monterrey</p><p>CAP MONTERREY DELEGACIÓN</p><p>No. de oficina 0018</p><p>Calle: DEGOLLADO, 734 Sur</p><p>Col. Centro</p><p>C.P. 64000</p>"
iframe37=branca.element.IFrame(html=html, width=500, height=300)

html= "<p>Ciudad: Monterrey</p><p>CAP MONTERREY CENTRIKA</p><p>No. de oficina 0052</p><p>Calle: AV VICENTE GUERRERO G PTO MTY, 2500 LOC S</p><p>Col. CENTRIKA</p><p>C.P. 64550</p>"
iframe38=branca.element.IFrame(html=html, width=500, height=300)

#OAXACA

html= "<p>Ciudad: Oaxaca de Juárez</p><p>CAP OAXACA DE JUÁREZ</p><p>No. de oficina 0002</p><p>Calle: GARDENIA, 613</p><p>Col. REFORMA</p><p>C.P. 68050</p>"
iframe39=branca.element.IFrame(html=html, width=500, height=300)

#PUEBLA

html= "<p>Ciudad: Puebla</p><p>CAP Puebla</p><p>No. de oficina 0026</p><p>Calle: AV REFORMA, 1907</p><p>Col. SAN  MATIAS</p><p>C.P. 72160</p>"
iframe40=branca.element.IFrame(html=html, width=500, height=300)


#QUERETARO

html= "<p>Ciudad: Querétaro</p><p>CAP Querétaro</p><p>No. de oficina 0016</p><p>Calle: AV TECNOLOGICO, 101</p><p>Col. Centro</p><p>C.P. 76000</p>"
iframe41=branca.element.IFrame(html=html, width=500, height=300)

html= "<p>Municipio: San Juan del Río</p><p>CAP San Juan del Río</p><p>No. de oficina 0056</p><p>Calle: AV PASEO CENTRAL, 183 L 26</p><p>Col. Centro</p><p>C.P. 76800</p>"
iframe42=branca.element.IFrame(html=html, width=500, height=300)

#QUINTANA ROO

html= "<p>Ciudad: Chetumal</p><p>CAP Chetumal</p><p>No. de oficina 0028</p><p>Calle: AV 22 DE ENERO ESQ 5 DE MAYO, s/n</p><p>Col. Centro</p><p>C.P. 77000</p>"
iframe43=branca.element.IFrame(html=html, width=500, height=300)


html= "<p>Ciudad: Cancún</p><p>CAP Cancún</p><p>No. de oficina 0043</p><p>Calle: AV XCARET, MZ 2 LT 2</p><p>Col. SUPERMANZANA 36</p><p>C.P. 77505</p>"
iframe44=branca.element.IFrame(html=html, width=500, height=300)

#SAN LUIS POTOSI

html= "<p>Ciudad: San Luis Potosí</p><p>CAP SAN LUIS POTOSÍ</p><p>No. de oficina 0034</p><p>Calle: AV VENUSTIANO CARRANZA, 985</p><p>Col. MODERNA</p><p>C.P. 78233</p>"
iframe45=branca.element.IFrame(html=html, width=500, height=300)


html= "<p>Ciudad: Ciudad Valles</p><p>CAP Ciudad Valles</p><p>No. de oficina 0062</p><p>Calle: GENERAL BLAS ESCONTRIA, 722</p><p>Col. OBRERA</p><p>C.P. 79050</p>"
iframe46=branca.element.IFrame(html=html, width=500, height=300)

#SINALOA

html= "<p>Ciudad: Culiacán</p><p>CAP CULIACÁN</p><p>No. de oficina 0023</p><p>Calle: BLVD ROTARISMO, 1733</p><p>Col. DESARROLLO URBANO TRES RIOS</p><p>C.P. 80000</p>"
iframe47=branca.element.IFrame(html=html, width=500, height=300)

#SONORA

html= "<p>Ciudad: Hermosillo</p><p>CAP HERMOSILLO</p><p>No. de oficina 0013</p><p>Calle: AV DE LA CULTURA, s/n</p><p>Col. VILLA DE SERIS NORTE</p><p>C.P. 83280</p>"
iframe48=branca.element.IFrame(html=html, width=500, height=300)


html= "<p>Ciudad: Ciudad Obregón</p><p>CAP CD. OBREGÓN</p><p>No. de oficina 0044</p><p>Calle: SUFRAGIO EFECTIVO, 801 LOC 11</p><p>Col. URBANIZABLE 1 CENTRO</p><p>C.P. 85050</p>"
iframe49=branca.element.IFrame(html=html, width=500, height=300)

#TABASCO

html= "<p>Ciudad: Villahermosa</p><p>CAP VILLAHERMOSA</p><p>No. de oficina 0029</p><p>Calle: BLVD ADOLFO RUIZ CORTINES, 917</p><p>Col. Centro</p><p>C.P. 86079</p>"
iframe50=branca.element.IFrame(html=html, width=500, height=300)

#TAMAULIPAS

html= "<p>Ciudad: CIUDAD VICTORIA</p><p>CAP CD. VICTORIA</p><p>No. de oficina 0009</p><p>Calle: BLVD FIDEL VELAZQUEZ, 2417 273</p><p>Col. TAMAULIPAS</p><p>C.P. 87090</p>"
iframe51=branca.element.IFrame(html=html, width=500, height=300)


html= "<p>Ciudad: REYNOSA</p><p>CAP REYNOSA</p><p>No. de oficina 0054</p><p>Calle: BLVD HIDALGO, 101 LOC LC</p><p>Col. LAS FUENTES</p><p>C.P. 88710</p>"
iframe52=branca.element.IFrame(html=html, width=500, height=300)

#TLAXCALA

html= "<p>Ciudad: Tlaxcala</p><p>CAP TLAXCALA</p><p>No. de oficina 0008</p><p>Calle: LIRA Y ORTEGA, 69</p><p>Col. Centro</p><p>C.P. 90000</p>"
iframe53=branca.element.IFrame(html=html, width=500, height=300)

#VERACRUZ

html= "<p>Ciudad: Xalapa</p><p>CAP XALAPA</p><p>No. de oficina 0010</p><p>Calle: AV XALAPA, 205</p><p>Col. UNIDAD DEL BOSQUE</p><p>C.P. 91017</p>"
iframe54=branca.element.IFrame(html=html, width=500, height=300)

html= "<p>Ciudad: Coatzacoalcos</p><p>CAP COATZACOALCOS</p><p>No. de oficina 0050</p><p>Calle: MALECON COSTERO, 1701 LOC S</p><p>Col. FRACC PARAISO</p><p>C.P. 96538</p>"
iframe55=branca.element.IFrame(html=html, width=500, height=300)

#YUCATÁN

html= "<p>Ciudad: Mérida</p><p>CAP MÉRIDA</p><p>No. de oficina 0004</p><p>Calle: CALLE 19, 93</p><p>Col. ITZIMNA</p><p>C.P. 97100</p>"
iframe56=branca.element.IFrame(html=html, width=500, height=300)

#ZACATECAS

html= "<p>Ciudad: Zacatecas</p><p>CAP Zacatecas</p><p>No. de oficina 0030</p><p>Calle: CARR A CD CUAUHTEMOC, KM 0 5  SN</p><p>Col. ANT ESC DE CIENCIAS QUIMICAS</p><p>C.P. 98600</p>"
iframe57=branca.element.IFrame(html=html, width=500, height=300)





################
# creamos 4 marcadores y añadimos la información del popup usando folium.Popup
# además, añadimos un icono que será de un color para los marcadores al este
# y de otro color para los marcadores del oeste.



marcador1 = folium.Marker(
    location=(21.8788660, -102.2927330),
    popup=folium.Popup(iframe1, max_width=500),
    icon=folium.Icon(color="red")
)

marcador2 = folium.Marker(
    location=(21.8919916, -102.2971318),
    popup=folium.Popup(iframe2, max_width=500),
    icon=folium.Icon(color="red")
)


marcador3 = folium.Marker(
    location=(32.6418060, -115.4523420),
    popup=folium.Popup(iframe3, max_width=500),
    icon=folium.Icon(color="red")
)

marcador4 = folium.Marker(
    location=(32.4949210, -116.9351520),
    popup=folium.Popup(iframe4, max_width=500),
    icon=folium.Icon(color="red")
)

marcador5 = folium.Marker(
    location=(24.1484360, -110.3052730),
    popup=folium.Popup(iframe5, max_width=500),
    icon=folium.Icon(color="red")
)


marcador6 = folium.Marker(
    location=(19.8537408, -90.5283937),
    popup=folium.Popup(iframe6, max_width=500),
    icon=folium.Icon(color="red")
)

#CIUDAD DE MEXICO

marcador7 = folium.Marker(
    location=(19.4448420, -99.1519020),
    popup=folium.Popup(iframe7, max_width=500),
    icon=folium.Icon(color="red")
)

marcador8 = folium.Marker(
    location=(19.3843930, -99.1485840),
    popup=folium.Popup(iframe8, max_width=500),
    icon=folium.Icon(color="red")
)

marcador9 = folium.Marker(
    location=(19.3574074, -99.1987345),
    popup=folium.Popup(iframe9, max_width=500),
    icon=folium.Icon(color="red")
)


marcador10 = folium.Marker(
    location=(19.3167491, -99.1237739),
    popup=folium.Popup(iframe11, max_width=500),
    icon=folium.Icon(color="red")
)

marcador11 = folium.Marker(
    location=(19.3286155, -99.1086078),
    popup=folium.Popup(iframe12, max_width=500),
    icon=folium.Icon(color="red")
)

marcador12 = folium.Marker(
    location=(19.4136232, -99.1813129),
    popup=folium.Popup(iframe12, max_width=500),
    icon=folium.Icon(color="red")
)

############
#CHIAPAS

marcador13 = folium.Marker(
    location=(16.7513094, -93.1069386),
    popup=folium.Popup(iframe13, max_width=500),
    icon=folium.Icon(color="red")
)

marcador14 = folium.Marker(
    location=(14.8993629, -92.2495908),
    popup=folium.Popup(iframe14, max_width=500),
    icon=folium.Icon(color="red")
)

marcador15 = folium.Marker(
    location=(16.7443033, -92.6342542),
    popup=folium.Popup(iframe15, max_width=500),
    icon=folium.Icon(color="red")
)


marcador16 = folium.Marker(
    location=(28.6180364, -106.1034114),
    popup=folium.Popup(iframe16, max_width=500),
    icon=folium.Icon(color="red")
)

marcador17 = folium.Marker(
    location=(31.7349424, -106.4435867),
    popup=folium.Popup(iframe17, max_width=500),
    icon=folium.Icon(color="red")
)

#COAHUILA

marcador18 = folium.Marker(
    location=(25.4462940, -100.9949010),
    popup=folium.Popup(iframe18, max_width=500),
    icon=folium.Icon(color="red")
)
marcador19 = folium.Marker(
    location=(25.5486569, -100.9437106),
    popup=folium.Popup(iframe19, max_width=500),
    icon=folium.Icon(color="red")
)

marcador20 = folium.Marker(
    location=(19.2725480, -103.7349670),
    popup=folium.Popup(iframe20, max_width=500),
    icon=folium.Icon(color="red")
)


marcador21 = folium.Marker(
    location=(24.0211620, -104.6712330),
    popup=folium.Popup(iframe21, max_width=500),
    icon=folium.Icon(color="red")
)

marcador22 = folium.Marker(
    location=(25.5545574, -103.5080860),
    popup=folium.Popup(iframe22, max_width=500),
    icon=folium.Icon(color="red")
)


#ESTADO DE MEXICO

marcador23 = folium.Marker(
    location=(19.2922765, -99.6233734),
    popup=folium.Popup(iframe23, max_width=500),
    icon=folium.Icon(color="red")
)

marcador24 = folium.Marker(
    location=(19.3572844, -99.1984595),
    popup=folium.Popup(iframe24, max_width=500),
    icon=folium.Icon(color="red")
)

marcador25 = folium.Marker(
    location=(19.6416550, -99.1359530),
    popup=folium.Popup(iframe25, max_width=500),
    icon=folium.Icon(color="red")
)

marcador26 = folium.Marker(
    location=(19.6857200, -99.2136460),
    popup=folium.Popup(iframe26, max_width=500),
    icon=folium.Icon(color="red")
)

marcador27 = folium.Marker(
    location=(19.6044288, -99.0123901),
    popup=folium.Popup(iframe27, max_width=500),
    icon=folium.Icon(color="red")
)


marcador28 = folium.Marker(
    location=(20.5322690, -100.8271530),
    popup=folium.Popup(iframe28, max_width=500),
    icon=folium.Icon(color="red")
)

marcador29=folium.Marker(location=(21.12273265086836, -101.69014391499321),popup=folium.Popup(iframe29, max_width=500),icon=folium.Icon(color="red"))


marcador30 = folium.Marker(
    location=(16.8540200, -99.8571970),
    popup=folium.Popup(iframe30, max_width=500),
    icon=folium.Icon(color="red")
)


marcador31 = folium.Marker(
    location=(20.1162570, -98.7422390),
    popup=folium.Popup(iframe31, max_width=500),
    icon=folium.Icon(color="red")
)



marcador32 = folium.Marker(
    location=(20.6849620, -103.3473740),
    popup=folium.Popup(iframe32, max_width=500),
    icon=folium.Icon(color="red")
)

marcador33 = folium.Marker(
    location=(20.6630626, -103.2965445),
    popup=folium.Popup(iframe33, max_width=500),
    icon=folium.Icon(color="red")
)

marcador34 = folium.Marker(
    location=(19.7280990, -101.2232810),
    popup=folium.Popup(iframe34, max_width=500),
    icon=folium.Icon(color="red")
)


marcador35 = folium.Marker(
    location=(18.9244110, -99.2176650),
    popup=folium.Popup(iframe35, max_width=500),
    icon=folium.Icon(color="red")
)

marcador36 = folium.Marker(
    location=(21.5072020, -104.9005490),
    popup=folium.Popup(iframe36, max_width=500),
    icon=folium.Icon(color="red")
)

marcador37 = folium.Marker(
    location=(25.6712230, -100.3376190),
    popup=folium.Popup(iframe37, max_width=500),
    icon=folium.Icon(color="red")
)

marcador38 = folium.Marker(
    location=(25.7001902, -100.3093165),
    popup=folium.Popup(iframe38, max_width=500),
    icon=folium.Icon(color="red")
)

marcador39 = folium.Marker(
    location=(17.0771560, -96.7069450),
    popup=folium.Popup(iframe39, max_width=500),
    icon=folium.Icon(color="red")
)


marcador40 = folium.Marker(
    location=(19.0516960, -98.2130720),
    popup=folium.Popup(iframe40, max_width=500),
    icon=folium.Icon(color="red")
)

marcador41 = folium.Marker(
    location=(20.5930070, -100.4062770),
    popup=folium.Popup(iframe41, max_width=500),
    icon=folium.Icon(color="red")
)

marcador42 = folium.Marker(
    location=(20.3941780, -99.9845350),
    popup=folium.Popup(iframe42, max_width=500),
    icon=folium.Icon(color="red")
)

marcador43 = folium.Marker(
    location=(18.4935890, -88.2962400),
    popup=folium.Popup(iframe12, max_width=500),
    icon=folium.Icon(color="red")
)

marcador44 = folium.Marker(
    location=(21.1539820, -86.8383440),
    popup=folium.Popup(iframe13, max_width=500),
    icon=folium.Icon(color="red")
)


marcador45 = folium.Marker(
    location=(22.1504450, -100.9875310),
    popup=folium.Popup(iframe45, max_width=500),
    icon=folium.Icon(color="red")
)
marcador46 = folium.Marker(
    location=(21.9873727, -99.0108345),
    popup=folium.Popup(iframe46, max_width=500),
    icon=folium.Icon(color="red")
)

marcador47 = folium.Marker(
    location=(24.8198090, -107.4083580),
    popup=folium.Popup(iframe47, max_width=500),
    icon=folium.Icon(color="red")
)


marcador48 = folium.Marker(
    location=(29.0680158, -110.9578327),
    popup=folium.Popup(iframe48, max_width=500),
    icon=folium.Icon(color="red")
)


marcador49 = folium.Marker(
    location=(27.4814187, -109.9272276),
    popup=folium.Popup(iframe49, max_width=500),
    icon=folium.Icon(color="red")
)

marcador50 = folium.Marker(
    location=(18.0004660, -92.9258710),
    popup=folium.Popup(iframe50, max_width=500),
    icon=folium.Icon(color="red")
)

marcador51 = folium.Marker(
    location=(23.7320460, -99.1300710),
    popup=folium.Popup(iframe51, max_width=500),
    icon=folium.Icon(color="red")
)


marcador52 = folium.Marker(
    location=(26.0737540, -98.3186850),
    popup=folium.Popup(iframe52, max_width=500),
    icon=folium.Icon(color="red")
)

marcador53 = folium.Marker(
    location=(19.3246045, -98.2339656),
    popup=folium.Popup(iframe53, max_width=500),
    icon=folium.Icon(color="red")
)


marcador54 = folium.Marker(
    location=(19.5607808, -96.9290164),
    popup=folium.Popup(iframe54, max_width=500),
    icon=folium.Icon(color="red")
)


marcador55 = folium.Marker(
    location=(18.1487570, -94.4685560),
    popup=folium.Popup(iframe55, max_width=500),
    icon=folium.Icon(color="red")
)

marcador56 = folium.Marker(
    location=(20.9927598, -89.6115249),
    popup=folium.Popup(iframe56, max_width=500),
    icon=folium.Icon(color="red")
)

marcador57 = folium.Marker(
    location=(22.7430220, -102.4971950),
    popup=folium.Popup(iframe57, max_width=500),
    icon=folium.Icon(color="red")
)



#################


# Creamos dos grupos para los marcadores
grp_este = folium.FeatureGroup(name='Este')
grp_oeste = folium.FeatureGroup(name='Oeste')
# Añadimos los marcadores AL GRUPO AL QUE CORRESPONDAN (NO AL MAPA)

marcador1.add_to(grp_este)
marcador2.add_to(grp_este)
marcador3.add_to(grp_este)
marcador4.add_to(grp_este)
marcador5.add_to(grp_este)
marcador6.add_to(grp_este)
marcador7.add_to(grp_este)
marcador8.add_to(grp_este)
marcador9.add_to(grp_este)
marcador10.add_to(grp_este)
marcador11.add_to(grp_este)
marcador12.add_to(grp_este)
marcador13.add_to(grp_este)
marcador14.add_to(grp_este)
marcador15.add_to(grp_este)
marcador16.add_to(grp_este)
marcador17.add_to(grp_este)
marcador18.add_to(grp_este)
marcador19.add_to(grp_este)
marcador20.add_to(grp_este)
marcador21.add_to(grp_este)
marcador22.add_to(grp_este)
marcador23.add_to(grp_este)
marcador24.add_to(grp_este)
marcador25.add_to(grp_este)
marcador26.add_to(grp_este)
marcador27.add_to(grp_este)
marcador28.add_to(grp_este)
marcador29.add_to(grp_este)
marcador30.add_to(grp_este)
marcador31.add_to(grp_este)
marcador32.add_to(grp_este)
marcador33.add_to(grp_este)
marcador34.add_to(grp_este)
marcador35.add_to(grp_este)
marcador36.add_to(grp_este)
marcador37.add_to(grp_este)
marcador38.add_to(grp_este)
marcador39.add_to(grp_este)
marcador40.add_to(grp_este)
marcador41.add_to(grp_este)
marcador42.add_to(grp_este)
marcador43.add_to(grp_este)
marcador44.add_to(grp_este)
marcador45.add_to(grp_este)
marcador46.add_to(grp_este)
marcador47.add_to(grp_este)
marcador48.add_to(grp_este)
marcador49.add_to(grp_este)
marcador50.add_to(grp_este)
marcador51.add_to(grp_este)
marcador52.add_to(grp_este)
marcador53.add_to(grp_este)
marcador54.add_to(grp_este)
marcador55.add_to(grp_este)
marcador56.add_to(grp_este)
marcador57.add_to(grp_este)



# Y ahora añadimos los grupos al mapa
grp_este.add_to(mi_mapa)
grp_oeste.add_to(mi_mapa)
# Y añadimos, además, el control de capas
folium.LayerControl().add_to(mi_mapa)
# Y guardamos el mapa
mi_mapa.save("CAPS.html")