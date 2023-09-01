from datetime import datetime

def formatar_data(data_param):
    # Converte a data de string para objeto datetime
    data_obj = datetime.strptime(data_param, '%Y-%m-%d')
    # Formata a data para MM-YYYY
    data_formatada = data_obj.strftime('%m-%Y')
    return data_formatada