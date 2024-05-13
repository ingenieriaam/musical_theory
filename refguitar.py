class Guitar():
    def __init__(self):
        self.diapason = {
            'e': ['E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F' ,'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'C#', 'D', 'D#', 'E' ],
            'B': ['B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#','Cb', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B' ],
            'G': ['G', 'Ab', 'A', 'Bb', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G' ,'Ab', 'A', 'Bb', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G' ],
            'D': ['D', 'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D' ,'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D' ],
            'A': ['A', 'Bb', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A' ,'Bb', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A' ],
            'E': ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E' ,'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E' ]
            }
        self.equivalente = {
            'A#': 'Bb', 'Bb': 'A#',
            'C#': 'Db', 'Db': 'C#',
            'D#': 'Eb', 'Eb': 'D#',
            'F#': 'Gb', 'Gb': 'F#',
            'G#': 'Ab', 'Ab': 'G#',
            'A#': 'Bb', 'Bb': 'A#'
        }
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
        self.mastil_medio = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99, 105, 111, 117, 123, 129, 135, 141]

    def encontrar_nota(self,nota, verbose = False):
        resultado = {}
        for cuerda, notas in self.diapason.items():
            nota = nota if nota not in self.equivalente else self.equivalente[nota]
            posicion = [i for i, x in enumerate(notas) if x == nota]
            if posicion:
                resultado[cuerda] = posicion
                if verbose:
                    print(f'La nota {nota} se encuentra en la cuerda {cuerda} en las posiciones {posicion}')
        return resultado
    
    def graficar_nota_terminal(self,nota, verbose = False):
        mastil = self.mastil.copy()
        # cuerda: lista de espacios en el diapason
        # self.mastil_medio contiene el espacio a marcar en el diagrama
        resultado = self.encontrar_nota(nota, verbose)
        for cuerda, posiciones in resultado.items():
            diag_cuerda = list(mastil[cuerda])
            for idx in posiciones:
                diag_cuerda[self.mastil_medio[idx-1]] = 'X'
            mastil[cuerda] = ''.join(diag_cuerda)
            print(cuerda,mastil[cuerda])
        print('r',mastil['r'])
        
        