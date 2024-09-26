import conexao

def obter_medias_finais():

    #conexão com o banco de dados
    conexao.conectar_banco()
    try:
        #Calcular as médias finais das disciplinas.
        #O ROUND é usado para arredondar os resultados para duas casas decimais.
        media = """
              UPDATE aluno
        SET
            portugues_media_final = ROUND((portugues_primeira_unidade +
                                            portugues_segunda_unidade +
                                            portugues_terceira_unidade) / 3, 2),
            matematica_media_final = ROUND((matematica_primeira_unidade +
                                             matematica_segunda_unidade +
                                             matematica_terceira_unidade) / 3, 2),
            biologia_media_final = ROUND((biologia_primeira_unidade +
                                           biologia_segunda_unidade +
                                           biologia_terceira_unidade) / 3, 2),
            fisica_media_final = ROUND((fisica_primeira_unidade +
                                        fisica_segunda_unidade +
                                        fisica_terceira_unidade) / 3, 2),
            ingles_media_final = ROUND((ingles_primeira_unidade +
                                        ingles_segunda_unidade +
                                        ingles_terceira_unidade) / 3, 2),
            filosofia_media_final = ROUND((filosofia_primeira_unidade +
                                           filosofia_segunda_unidade +
                                           filosofia_terceira_unidade) / 3, 2),
            artes_media_final = ROUND((artes_primeira_unidade +
                                       artes_segunda_unidade +
                                       artes_terceira_unidade) / 3, 2),
            quimica_media_final = ROUND((quimica_primeira_unidade +
                                          quimica_segunda_unidade +
                                          quimica_terceira_unidade) / 3, 2),
            historia_media_final = ROUND((historia_primeira_unidade +
                                          historia_segunda_unidade +
                                          historia_terceira_unidade) / 3, 2),
            sociologia_media_final = ROUND((sociologia_primeira_unidade +
                                            sociologia_segunda_unidade +
                                            sociologia_terceira_unidade) / 3, 2)
        """
        #Atualizar as médias finais no banco de dados.
        conexao.cursor.execute(media)

        #Obtém todos os resultados, caso sejam retornados.
        conexao.cursor.fetchall()

    except Exception as e:
        #Exibe uma mensagem de erro se der errado.
        print(f"Erro ao executar a consulta: {e}")