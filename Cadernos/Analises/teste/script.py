import pandas as pd

df = pd.read_excel('arquivo.xlsx')
nome_arquivo_saida = 'consultas.sql'

idDisciplina = int(input("Começar em qual ID de disciplina?"))  
status = 1  

Cursos = {"BEER":1,
"TEDR":2,
"TDI":3,
"TII":4,
"TIM":5,
"CLPR":6,
"CLL":7,
"BCCR":8,
"PRO":9,
"TPG":10,
"TER":11,
"TEL":12,
"TED":13,
"TCO":14,
"TAD":15,
"BCC":16,
"TIMR":17,
"TIIR":18}


Areas = { 
"ARQ":1,
"ART":2,
"COCIV":3,
"INFAR":4 ,
"INFPB":5, 
"ADM":6,
"BIO":7,
"CAR":8,
"DIR":9,
"EFI":10,
"ELE":11,
"ELO":12,
"FIL":13,
"FIS":14,
"GEO":15,
"HIS":16,
"LETPE":17,
"LETPI":18,
"LETPL":19,
"MAT":20,
"MEC":21,
"PED":22,
"QUI":23,
"SOC":24}


with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo:

    for index, row in df.iterrows():
        
        semestre = row['Semestre']
        nome = str(row['Componente Curricular'])
        sigla = str(row['Cód.'])
        idArea1 = str(row['Área Docente 1'])
        idArea2 = row['Área Docente 2']
        cargaHoraria = row['C.H. PPC (aulas)']
        cargaHorariaParcial = row['C.H. Reg. Parcial']
        regencia = row['Reg. Comp.']
        siglaCurso = str(row['Sigla Curso'])
        idCurso = -1
        
        if pd.isna(regencia):
            regencia = "SEM REGÊNCIA"
        regencia = str(regencia).upper()

        if pd.isna(cargaHorariaParcial):
            cargaHorariaParcial = 0

        if pd.isna(idArea2):
            idArea2 = "null"

        if semestre == "Ímpar":
            semestre = "IMPAR"
        elif pd.isna(semestre):
            semestre = ""
        semestre = str(semestre).upper()

        for curso in Cursos.items():
            if curso[0] == siglaCurso:
                idCurso = curso[1]
        
        for area in Areas.items():
            if area[0] == idArea1:
                idArea1 = area[1]
            
            if area[0] == str(idArea2):
                idArea2 = area[1]

        
        sql_query = f'INSERT INTO disciplina(idDisciplina, cargaHoraria, cargaHorariaParcial, nome, regencia, semestre, sigla, status, idArea, idArea2, idCurso) VALUES ({idDisciplina}, {cargaHoraria}, {cargaHorariaParcial},"{nome}","{regencia}", "{semestre}", "{sigla}", {status}, {idArea1}, {idArea2}, {idCurso});\n'

        arquivo.write(sql_query)
   
        idDisciplina += 1

print(f'Consultas SQL foram salvas no arquivo: {nome_arquivo_saida}')
