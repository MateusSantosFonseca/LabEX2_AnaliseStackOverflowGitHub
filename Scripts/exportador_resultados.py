import csv

def exportar_resultados_csv(path_arquivo_csv, resultados):
    with open(path_arquivo_csv, mode='w+') as arquivo_csv:
        csv_writer = csv.writer(arquivo_csv, quotechar='"')
        header = (["Nome repositório", "Linguagem primária", "Qt. menções da LP nas quest. do SO", "Qt. menções da LP nas quest. do SO s/ repetição", "Qt. menções do título das top issues nas quest. do SO", "Qt. menções do título das bottom issues nas quest. do SO"])
        csv_writer.writerow(header)
        
        for linha in resultados:
            linha_splitada = linha.split(",")
            
            dict_resultado = {0: linha_splitada[0], 1: linha_splitada[1], 2: linha_splitada[2],
                              3: linha_splitada[3], 4: linha_splitada[4], 5: linha_splitada[5]}
            csv_writer.writerow(dict_resultado.values())