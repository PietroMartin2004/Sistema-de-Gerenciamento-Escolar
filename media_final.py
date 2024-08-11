import conexao

def obter_medias_finais():
    conexao.conectar_banco()
    try:
        media = """
        SELECT
            matricula,
            
            (portugues_primeira_unidade +
             portugues_segunda_unidade +
             portugues_terceira_unidade) / 3 AS portugues_media_final,
            (matematica_primeira_unidade +
             matematica_segunda_unidade +
             matematica_terceira_unidade) / 3 AS matematica_media_final,
            (biologia_primeira_unidade +
             biologia_segunda_unidade +
             biologia_terceira_unidade) / 3 AS biologia_media_final,
            (fisica_primeira_unidade +
             fisica_segunda_unidade +
             fisica_terceira_unidade) / 3 AS fisica_media_final,
            (ingles_primeira_unidade +
             ingles_segunda_unidade +
             ingles_terceira_unidade) / 3 AS ingles_media_final,
            (filosofia_primeira_unidade +
             filosofia_segunda_unidade +
             filosofia_terceira_unidade) / 3 AS filosofia_media_final,
            (artes_primeira_unidade +
             artes_segunda_unidade +
             artes_terceira_unidade) / 3 AS artes_media_final,
            (quimica_primeira_unidade +
             quimica_segunda_unidade +
             quimica_terceira_unidade) / 3 AS quimica_media_final,
            (historia_primeira_unidade +
             historia_segunda_unidade +
             historia_terceira_unidade) / 3 AS historia_media_final,
            (sociologia_primeira_unidade +
             sociologia_segunda_unidade +
             sociologia_terceira_unidade) / 3 AS sociologia_media_final,;
        """
        conexao.cursor.execute(media)
    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")