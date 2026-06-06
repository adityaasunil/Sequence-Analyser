class Analyser:
    def __init__(self, dna_strings: list[str]):
        self.strings = [x.upper() for x in dna_strings]

    def __str__(self):
        return f'DNA sequences({len(self.strings)}): {', '.join(self.strings)}'
    
ob = Analyser(['cgtaccg', 'gcatggc'])

if __name__ == '__main__':
    print(ob)

