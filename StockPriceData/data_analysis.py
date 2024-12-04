def calculate_and_display_average_price(data):
    # Проверяем, содержит ли DataFrame данные о закрытии
    if 'Close' in data.columns:
        average_price = data['Close'].mean()
        print(f"Средняя цена закрытия за указанный период: {average_price:.2f}")
    else:
        print("Данные о закрытии отсутствуют.")


def notify_if_strong_fluctuations(data, threshold):
    # Проверяем, содержит ли DataFrame данные о закрытии
    if 'Close' in data.columns:
        max_price = data['Close'].max()  # Находим максимальную цену
        min_price = data['Close'].min()  # Находим минимальную цену

        fluctuation = ((max_price - min_price) / min_price) * 100  # Рассчитываем процент колебаний

        # Проверяем, превышает ли колебание заданный порог
        if fluctuation > threshold:
            print(f"Уведомление: Цены акций колебались более чем на {threshold}% за указанный период. "
                  f"Минимальная цена: {min_price:.2f}, Максимальная цена: {max_price:.2f}, "
                  f"Общий процент колебания: {fluctuation:.2f}%")
        else:
            print(f"Цены акций колебались менее чем на {threshold}%. Процент колебания: {fluctuation:.2f}%")
    else:
        print("Данные о закрытии отсутствуют.")
