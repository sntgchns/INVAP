invap = [dict(
            _id= 'nuclear',
            Nuclear= dict(
                    reactores_de_investigacion= dict(
                        NUR= dict(
                            pais= 'Argelia',
                            ubicacion= 'Argel',
                            puesta_en_marcha= '1989',
                            potencia_termica= '1 MW',
                            notas= 'Vendido al Alto Comisariado para la Investigación del gobierno argelino.'
                    ),
                        RA_6= dict(
                            pais= 'Argentina',
                            ubicacion= 'Bariloche',
                            puesta_en_marcha= '1982',
                            potencia_termica= '0,5 MW',
                            notas= 'Para la CNEA.'
                    ),
                        RA_8= dict(
                            pais= 'Argentina',
                            ubicacion= 'Pilcaniyeu',
                            puesta_en_marcha= '1997',
                            potencia_termica= '0,1 MW',
                            notas= 'Construido para la CNEA. Facilidad crítica para estudiar el comportamiento neutrónico del núcleo del reactor Carem.'
                    ),
                        RA_10= dict(
                            pais= 'Argentina',
                            ubicacion= 'Ezeiza',
                            puesta_en_marcha= '2024',
                            potencia_termica= '30 MW',
                            notas= 'En construcción para la CNEA.'
                    ),
                        OPAL= dict(
                            pais= 'Australia',
                            ubicacion= 'Sídney',
                            puesta_en_marcha= '2007',
                            potencia_termica= '20 MW',
                            notas= 'Vendido a la Organización Australiana para la Ciencia y la Tecnología Nuclear (ANSTO).'
                    ),
                        ETRR_2= dict(
                            pais= 'Egipto',
                            ubicacion= 'El Cairo',
                            puesta_en_marcha= '1997',
                            potencia_termica= '22 MW',
                            notas= 'Vendido a la Autoridad de Energía Atómica de Egipto'
                    ),
                        RP_0= dict(
                            pais= 'Perú',
                            ubicacion= 'Lima',
                            puesta_en_marcha= '1978',
                            potencia_termica= '10 MW',
                            notas= 'Provisión del sistema de instrumentación nuclear al Instituto Peruano de Energía Nuclear.'
                    ),
                        RP_10= dict(
                            pais= 'Perú',
                            ubicacion= 'Huarangal',
                            puesta_en_marcha= '1988',
                            potencia_termica= '10 MW',
                            notas= 'Provisión del sistema de instrumentación nuclear al Instituto Peruano de Energía Nuclear.'
                    ),
                        LPRR= dict(
                            pais= 'Arabia Saudita',
                            ubicacion= 'Riad',
                            puesta_en_marcha= '2023',
                            potencia_termica= '0,1 MW',
                            notas= 'En construcción, para el King Abdulaziz City for Science & Technology.'
                    ),
                        PALLAS= dict(
                            pais= 'Países Bajos',
                            ubicacion= 'Petten',
                            puesta_en_marcha= '2028',
                            potencia_termica= '25 MW',
                            notas= 'A ser construido para la Foundation Pallas'
                    ),
                        RMB= dict(
                            pais= 'Brasil',
                            ubicacion= 'Iperó',
                            puesta_en_marcha= 'Sin fecha aún',
                            potencia_termica= '30 MW',
                            notas= 'En fase de Ingeniería de Detalle, cliente CNEN.'
                    )
                ),
                    planta_de_produccion_de_radioisotopos= dict(),
                    plantas_de_elementos_combustibles= dict(),
                    servicios_a_plantas_nucleares= dict(),
                    sistema_de_gestion_de_residuos= dict(),
                    estudio_de_emplazamiento= dict()
                    )
            ),
        dict(
            _id= 'espacial',
            Espacial= dict(
                    satelites= dict(
                        SAC_A= dict(
                            año= '1998',
                            uso= 'Ensayos de sistemas ópticos, energéticos, de guiado y control aplicables en futuros modelos'
                    ),
                        SAC_B= dict(
                            año= '1996',
                            uso= 'Aplicaciones astronómicas'
                    ),
                        SAC_C= dict(
                            año= '1998',
                            uso= 'Monitoreo ambiental y de catástrofes naturales'
                    ),
                        SAC_D= dict(
                            año= '2007',
                            uso= 'Monitoreo de la salinidad en mares y océanos'
                    ),
                        SAOCOM= dict(),
                        ARSAT_1= dict(
                            fecha_de_lanzamiento= '16 de octubre de 2014',
                            vehiculo_de_lanzamiento= 'Ariane 5',
                            banda= 'KU',
                            orbita= 'Geoestacionaria',
                            posicion_orbital= '71,8° Oeste',
                            servicios= 'Telefonía, datos y televisión'
                        ),
                        ARSAT_2= dict(
                            fecha_de_lanzamiento= '30 de septiembre de 2015',
                            vehiculo_de_lanzamiento= 'Ariane 5',
                            banda= 'KU y C',
                            orbita= 'Geoestacionaria',
                            posicion_orbital= '81° Oeste',
                            servicios= 'Transporte de datos y video'
                        ),
                        ARSAT_SG1= dict(
                            fecha_de_lanzamiento= 'Por anunciar',
                            vehiculo_de_lanzamiento= 'Por anunciar',
                            banda= '',
                            orbita= '',
                            posicion_orbital= '81° Oeste',
                            servicios= ''
                        )
                ),
                    segmento_terreno= dict(
                        ingenieria_de_operaciones= dict(),
                        desarrollo_de_software= dict(),
                        entrenamiento_de_operadores= dict(),
                        certificaciones= dict(),
                        soporte_de_operaciones= dict()
                        )
                    )
            ),
        dict(
            _id= 'defensa',
            Defensa= dict(
                    radares= dict(
                        RMA_C320= dict(),
                        RSMA_S= dict(
                            volumen_de_cobertura= dict(
                                alcance= '256 NM',
                                acimut= '360°',
                                altitud= '100.000 pies',
                                elevavion_máxima= '> 45°'
                                ),
                            modos= '1, 2, 3 / A, C, ELS y EHS',
                            capacidad_de_deteccion_de_blancos_total= '> 1.000 aviones',
                            exactitud= '< 0,2 NM rms, < 0,06° rms',
                            resolucion= '0,05 NM, 0,6°',
                            probabilidad_de_deteccion= '> 99,7%',
                            validacion_de_codigo= 'modo 3/A > 97,1%, modo C > 96,7%',
                            frecuencia_de_operacion= '1030 / 1090 MHz',
                            frecuencia_de_interrogacion= '50 a 400 Hz',
                            FRUIT= '11000 / segundo',
                            velocidad_de_giro= 'Hasta 15 RPM',
                            condiciones_ambientales= dict(
                                viento_con_radar_operativo= '60 nudos',
                                viento_con_radar_sin_operar= '100 nudos',
                                temperatura_exterior= '-30°C/+60°C',
                                humedad_ambiente_máxima= '100%',
                                sismo= 'INTI Reglamento IMPRES CIRSOC 103: Zona 4'
                            ),
                            disponibilidad= '> 99,997%',
                            MTBCF= '> 180000 horas',
                            MTTR= '30 minutos',
                            salida_de_datos= 'ASTERIX Cat 1, Cat 2, Cat 21, Cat 34, Cat 48',
                            configuracion_y_control= 'Consola de comandos y herramientas gráficas para uso local y remoto.'
                    ),
                        RPA_240T= dict(
                            frecuencia_de_operacion= 'Banda L (D)',
                            rango_instrumentado= '240NM',
                            precision= '0,2° acimut; 0,3° elevación',
                            altura_maxima= '100Kft',
                            velocidad_de_giro= '6 RPM',
                            seguimiento_de_blancos_simultaneos= '> 600',
                            MTBCF= '> 1500 horas',
                            MTTR= '< 1 hora',
                            modos_IFF= '1, 2, 3 / A, C, S (4 y 5 opcionales)',
                            salida_de_datos= 'ASTERIX (otros a requerimiento del cliente)',
                            configuracion_y_control= 'Consola de comandos y herramientas gráficas para uso local y remoto.'
                    ),
                        RPA_170M= dict(
                            frecuencia_de_operacion= 'Banda L (D)',
                            rango_instrumentado= '170NM',
                            precision= 'Monopulso en acimut y elevación.',
                            altura_maxima= '100Kft',
                            velocidad_de_giro= '6 a 14 RPM',
                            seguimiento_de_blancos_simultaneos= '> 600',
                            tiempo_de_despliegue= '< 30 minutos',
                            MTBCF= '> 1500 horas',
                            MTTR= '< 1 hora',
                            modos_IFF= '1, 2, 3 / A, C, S (4 y 5 opcionales)',
                            salida_de_datos= 'ASTERIX (otros a requerimiento del cliente)',
                            configuracion_y_control= 'Consola de comandos y herramientas gráficas para uso local y remoto.'
                    ),
                        AN_TPS_43= dict(
                            notas= 'Modernización de Radares de Invap (PMRI) sobre el Radar Táctico 3D para la Defensa Aérea TPS-43 de Westinghouse.'
                        ),
                        RVT= dict(
                            RVT_30= dict(
                                drone= '4 Km',
                                peaton= '8 Km',
                                bote_de_goma= '12 Km',
                                vehiculo_pequeño= '15 Km',
                                vehiculo_grande= '25 Km',
                                maximo_alcance_instrumentado= '30 Km',
                                precision__en_acimut= '0.6°',
                                precision__en_elevación= '0.2 m - 10 m'
                            ),
                            RVT_50= dict(
                                drone= '6 Km',
                                peaton= '10 Km',
                                bote_de_goma= '15 Km',
                                vehiculo_pequeño= '25 Km',
                                vehiculo_grande= '35 Km',
                                maximo_alcance_instrumentado= '50 Km',
                                precision__en_acimut= '0.3°',
                                precision__en_elevación= '0.2 m - 10 m'
                            ),
                            RVT_80= dict(
                                drone= '8 Km',
                                peaton= '15 Km',
                                bote_de_goma= '23 Km',
                                vehiculo_pequeño= '36 Km',
                                vehiculo_grande= '48 Km',
                                maximo_alcance_instrumentado= '80 Km',
                                precision__en_acimut= '0.3°',
                                precision__en_elevación= '0.2 m - 10 m'
                            ),
                        ),
                        RMF_200V= dict(
                            velocidad_de_escaneo= dict(
                                a_7_RPM= dict(
                                    avion_de_linea= '189 Km',
                                    aviones_medianos= '112 Km',
                                    avioneta_pequeña= '67 Km',
                                    drones= '40 Km'
                                ),
                                a_15_RPM= dict(
                                    avion_de_linea= '154 Km',
                                    aviones_medianos= '103 Km',
                                    avioneta_pequeña= '60 Km',
                                    drones= '33 Km'
                                ),
                                a_30_RPM= dict(
                                    avion_de_linea= '134 Km',
                                    aviones_medianos= '82 Km',
                                    avioneta_pequeña= '47 Km',
                                    drones= '27 Km'
                                ),
                                a_60_RPM= dict(
                                    avion_de_linea= '122 Km',
                                    aviones_medianos= '71 Km',
                                    avioneta_pequeña= '41 Km',
                                    drones= '23 Km'
                                )
                            ),
                        ),
                        RUAS_160= dict(
                            descripcion= dict(
                                longitud= '3,10 m',
                                ancho_fuselaje= '0,7 m',
                                ancho_patines= '1,8 m',
                                altura= '1,72 m',
                                diametro_de_rotor_superior_e_inferior= '3,6 m',
                            ),
                            pesos= dict(
                                peso_maximo_de_despegue= '150 Kg',
                                peso_vacio= '80 Kg',
                                capacidad_de_carga_util= '70 Kg (sensores y combustible)'
                            ),
                            sistema_propulsivo= dict(
                                tipo_de_motor= 'Motor a piston 2T',
                                potencia= '39 HP',
                                opcional= 'Redundancia doble motor a pistón'
                            ),
                        ),
                    ),
                    defensa= dict(
                        SCODA= dict(),
                        DS_STA= dict(),
                        EVT_035A= dict(),
                        EVT_035N= dict()
                )
            )
            ),
        dict(
            _id= 'medicina',
            Medicina= dict(
                    radioterapia_externa= 'Aceleradores lineales',
                    radioterapia_interna= 'Braquiterapia',
                    intecnus= 'Fundación INTECNUS',
                    otros= [
                        'Protonterapia',
                        'Medicina Nuclear',
                        'Ciclotrón y Radiofarmacia',
                        'Garantías, repuestos y programas de mantenimiento preventivo y correctivo',
                        'Diseño de Búnkers', 'Instalación y Puesta en Marcha de Equipamiento Médico',
                        'Implementación Regulatoria y Normativa Local',
                        'Capacitación en trabajo clínico, operación y mantenimiento de equipamientos para médicos, técnicos, físicos e ingenieros',
                        'Construcción y Seguimiento de Obras Civiles'
                        ]
                    
                    )
            ),
        dict(
            _id= 'sedes',
            Sedes = dict(
                argentina= dict(
                    bariloche= dict(
                        direccion= 'Av. Cmte. Luis Piedrabuena 4950 (R8403CPV), San Carlos de Bariloche, Río Negro, Argentina',
                        telefono= '+542944409300',
                        fax= '+542944409336',
                        coordenadas= "S 41°7'25 O 71°14'35"
                    ),
                    buenos_aires= dict(
                        direccion= 'Esmeralda 356 planta baja (C1035ABH), Buenos Aires, Argentina',
                        telefono= '+541141324444',
                        fax= '+541143943543'
                    ),
                    cordoba='',
                    neuquen= '',
                    rosario= '',
                ), 
                argelia= '',
                arabia_saudita= '',
                australia= dict(
                    direccion= '24 Talara Road GYMEA NSW 2227 Australia',
                    telefono= '+61400017508',
                ),
                bolivia= dict(
                    direccion= 'Calle 9 de Calacoto No 7979 esq. Sanchez de Bustamante Edificio Vitruvio 2, Piso 3, Oficina H'
                ),
                brasil= '',
                egipto= '',
                estados_unidos= dict(
                    direccion= 'Black River Technology, Inc. 2808 Centre Circle Dr., Ste. A Downers Grove, IL 60515, USA',
                    telefono= '+12195481823',
                    fax= '+12195488162'
                ),
                holanda= '',
                india= '',
                venezuela= ''
                )
            ),
        dict(
            _id= 'social',
            Social = dict(
                facebook= 'https://www.facebook.com/INVAP',
                instagram= 'https://www.instagram.com/invapargentina',
                twitter= 'https://twitter.com/invapargentina',
                linkedin= 'https://www.linkedin.com/company/invap',
                youtube= 'https://www.youtube.com/user/invapin'
                )
            )
]

rutas = {
    'rutas': ['/nuclear', '/espacial', '/defensa', '/medicina', '/sedes', '/social', '/ping']
    }

instrucciones = ['Bienvenido. Esta es una API no oficial de INVAP: ',
    'Para navegar los datos, ingresa a las siguientes rutas del dominio:',
    'Recorda no usar caracteres especiales, acentos ni espacios en blanco. Gracias por conectarte!',
    'web_contact: santiago.soñora.com'
]
