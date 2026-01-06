try:
    from app import app
    from exercicios import EXERCICIOS, buscar_exercicio_por_id
    print("Importação com sucesso!")
    print(f"Total exercícios: {len(EXERCICIOS)}")
    print(f"Teste busca id 1: {buscar_exercicio_por_id(1)}")
except Exception as e:
    print(f"Erro fatal: {e}")
