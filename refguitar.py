from collections import namedtuple

class Guitar():
    def __init__(self):
        self.diapason = {
            'e': ['E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E' ],
            'B': ['B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E' ,'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B' ],
            'G': ['G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G' ],
            'D': ['D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E' ,'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D' ],
            'A': ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A' ],
            'E': ['E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E' ],
            }
        self.equivalente = {
            'G#': 'Ab',
            'A#': 'Bb',
            'C#': 'Db',
            'D#': 'Eb',
            'F#': 'Gb'
        }
        self.cromatica = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B' ]
        self.symbol = {
            'red_circle' :'\u2B55',
            'white_circle' :'\u26AA',
            'green_cross' :'\u274C',
            'black_cross' :'\u2716',
            'red_cross' :'\u274E'
        }
        self.mastil = {
            'e': 'I-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|',
            'B': 'I-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|',
            'G': 'I-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|',
            'D': 'I-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|',
            'A': 'I-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|',
            'E': 'I-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|',
            'r': '   1           3           5           7           9              I  12                15          17          19          21             I  24 '
        }
        self.mastil_res = self.mastil.copy()
        self.mastil_medio = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99, 105, 111, 117, 123, 129, 135, 141]
        
        self.formula = self.Formulas()
        self.intervalo = self.Intervalos()

    ###############################################
    # Metodos    
    ###############################################
    def encontrar_nota(self,nota, verbose = False):        
        """
        Encuentra la posición de una nota dada en cada cuerda del guitarra.
        
        Parámetros:
        - nota (str): Nota a ser encontrada.
        - verbose (bool): Si es True, imprime los resultados.

        Returns:
        - dict: Un diccionario con el string y las posiciones de la nota encontrada en ese string.
        """
        resultado = {}
        for cuerda, notas in self.diapason.items():
            nota = nota if nota not in self.equivalente else self.equivalente[nota]
            posicion = [i for i, x in enumerate(notas) if x == nota]
            if posicion:
                resultado[cuerda] = posicion
                if verbose:
                    print(f'La nota {nota} se encuentra en la cuerda {cuerda} en las posiciones {posicion}')
        return resultado
    
    def graficar_nota(self, nota, caracter = 'X',verbose = False):
        """
        Representa una nota dada en el diagrama de diapasón de guitarra en la terminal.
        El diagrama resultante se guarda en el atributo 'mastil_res'.

        Parámetros:
        - nota (str): Nota de la que se generará el diagrama.
        - caracter (str): Caracter de la representación de la nota del diagrama. El valor predeterminado es 'X'.
        - verbose (bool): Si es True, imprime los resultados.
        """
        resultado = self.encontrar_nota(nota, verbose)

        for cuerda, posiciones in resultado.items():
            diag_cuerda = list(self.mastil_res[cuerda])

            for idx in posiciones:
                cuerda_idx = self.mastil_medio[idx-1]
                if len(caracter) > 1:
                    diag_cuerda[cuerda_idx],diag_cuerda[cuerda_idx+1] = caracter
                else:
                    diag_cuerda[cuerda_idx] = caracter

            self.mastil_res[cuerda] = ''.join(diag_cuerda)
            print(cuerda,self.mastil_res[cuerda]) if verbose else None
        print('r',self.mastil_res['r']) if verbose else None

    def graficar_escala(self, tonica, tipo, indicacion='intervalo', verbose = False):
        """
        Representa la escala dada en el diagrama de diapasón de guitarra en la terminal.

        Parametros:
        - tonica (str): Tonica de la escala.
        - tipo (str): Tipo de escala.
        - indicacion (str): Indica qué se representa en el diagrama, intervalos o nombres de las notas ('intervalo' o 'nota').
        - verbose (bool): If True, prints the results.

        Returns:
        None
        """
        self.graficar_nota(tonica,caracter='T',verbose=verbose)

        esc_formula = self.formula.modo[tipo]
        inte_gen    = self.gen_prox_dato(self.intervalo.modo[tipo])
        note_gen    = self.gen_prox_nota(tonica)

        next(note_gen); next(inte_gen)
        
        for form in esc_formula:
            nota = next(note_gen); intervalo = next(inte_gen)

            if form == 't': 
                nota = next(note_gen)
            elif form == 'tm':
                nota = next(note_gen); nota = next(note_gen)

            caracter = intervalo if indicacion == 'intervalo' else nota
            self.graficar_nota(nota,caracter=caracter,verbose=verbose)
        for key in self.mastil_res.keys():
            print(self.mastil_res[key])

    def limpiar_mastil_res(self):
        """
        Reseteo del atributo mastil_res a una copia del atributo mastil.
        """
        self.mastil_res = self.mastil.copy()

    ###############################################
    # Generadores    
    ###############################################
    def gen_prox_dato(self,form):
        """
        Genera el siguiente elemento en la secuencia de elementos proporcionada.

        Parameters:
        - form (list): Secuencia de elementos.

        Yields:
        - Siguiente elemento de la secuencia.
        """
        idx = 0
        while True:
            yield form[idx]
            idx+=1; idx%=len(form)
    def gen_prox_nota(self,inicial='C'):
        """
        Genera la siguiente nota en la escala cromática a partir de la nota inicial proporcionada.
        
        Parámetros:
        - Inicial (str): la nota inicial para iniciar la generación desde. El valor predeterminado es 'C'.
    
        Yields:
        - str: La siguiente nota en la escala cromática.
        """
        nota = inicial if inicial not in self.equivalente else self.equivalente[inicial]
        idx = self.cromatica.index(nota) 
        while True:
            yield self.cromatica[idx]
            idx+=1; idx%=len(self.cromatica)

    ###############################################
    # Clases    
    ###############################################
    class Formulas():
        def __init__(self):
            # t: tono, st: semi tono, tm: tono y medio
            self.jonico    = ['t', 't', 'st', 't', 't', 't', 'st']
            self.dorico    = ['t', 'st', 't', 't', 't', 'st', 't']
            self.frigio    = ['st', 't', 't', 't', 'st', 't', 't']
            self.lidio     = ['t', 't', 't', 'st', 't', 't', 'st']
            self.mixolidio = ['t', 't', 'st', 't', 't', 'st', 't']
            self.eolico    = ['t', 'st', 't', 't', 'st', 't', 't']
            self.locrio    = ['st', 't', 't', 'st', 't', 't', 't']
            self.pentatonica_menor = ['tm', 't', 't', 't', 'tm']
            self.pentatonica_mayor = ['t', 't', 'tm', 't', 'tm']
            self.mayor = self.jonico
            self.menor = self.eolico
            self.modo  = {
                'mayor': self.mayor,
                'menor': self.menor,
                'jonico': self.jonico,
                'dorico': self.dorico,
                'frigio': self.frigio,
                'lidio': self.lidio,
                'mixolidio': self.mixolidio,
                'eolico': self.eolico,
                'locrio': self.locrio,
                'pentatonica_mayor': self.pentatonica_mayor,
                'pentatonica_menor': self.pentatonica_menor
            }
    class Intervalos():
        def __init__(self):
            self.jonico    = ['T', '2', '3', '4', '5', '6', '7']
            self.dorico    = ['T', '2', 'b3', '4', '5', '6', 'b7']
            self.frigio    = ['T', 'b2', 'b3', '4', '5', 'b6', 'b7']
            self.lidio     = ['T', '2', '3', '#4', '5', '6', '7']
            self.mixolidio = ['T', '2', '3', '4', '5', '6', 'b7']
            self.eolico    = ['T', '2', 'b3', '4', '5', 'b6', 'b7']
            self.locrio    = ['T', 'b2', 'b3', '4', 'b5', 'b6', 'b7']
            self.pentatonica_menor = ['T', '3', '4', '5', '7']
            self.pentatonica_mayor = ['T', '2', '3', '5', '6']
            self.mayor = self.jonico
            self.menor = self.eolico
            self.modo  = {
                'mayor': self.mayor,
                'menor': self.menor,
                'jonico': self.jonico,
                'dorico': self.dorico,
                'frigio': self.frigio,
                'lidio': self.lidio,
                'mixolidio': self.mixolidio,
                'eolico': self.eolico,
                'locrio': self.locrio,
                'pentatonica_mayor': self.pentatonica_mayor,
                'pentatonica_menor': self.pentatonica_menor
            }
            
        