import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Descargar datos de SPY con intervalo de 30 minutos
spy = yf.Ticker('SPY')
# Obtener datos históricos de los últimos 5 días con intervalo de 30 minutos
df = spy.history(period='5d', interval='30m')

print('=== DATOS SPY ULTIMOS 5 DIAS (30min) ===')
print(df.tail(20))
print()

# Calcular indicadores técnicos
def calculate_rsi(prices, period=14):
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_macd(prices, fast=12, slow=26, signal=9):
    ema_fast = prices.ewm(span=fast).mean()
    ema_slow = prices.ewm(span=slow).mean()
    macd = ema_fast - ema_slow
    macd_signal = macd.ewm(span=signal).mean()
    macd_hist = macd - macd_signal
    return macd, macd_signal, macd_hist

# Calcular medias móviles
df['MA20'] = df['Close'].rolling(window=20).mean()
df['MA50'] = df['Close'].rolling(window=50).mean()
df['MA200'] = df['Close'].rolling(window=200).mean()

# Calcular RSI
df['RSI'] = calculate_rsi(df['Close'], 14)

# Calcular MACD
df['MACD'], df['MACD_Signal'], df['MACD_Hist'] = calculate_macd(df['Close'])

# Encontrar soportes y resistencias recientes
recent_highs = df['High'].rolling(window=10, min_periods=5).max()
recent_lows = df['Low'].rolling(window=10, min_periods=5).min()
df['Resistance'] = recent_highs
df['Support'] = recent_lows

print('=== ULTIMOS 10 PERIODOS CON INDICADORES ===')
print(df[['Close', 'Volume', 'MA20', 'MA50', 'RSI', 'MACD', 'MACD_Hist', 'Support', 'Resistance']].tail(10))
print()

# Análisis del último periodo
last = df.iloc[-1]
prev = df.iloc[-2] if len(df) > 1 else None

print('=== ANALISIS DEL ULTIMO PERIODO ===')
print(f'Precio actual: ${last["Close"]:.2f}')
print(f'RSI (14): {last["RSI"]:.2f}')
print(f'MACD: {last["MACD"]:.4f}')
print(f'MACD Histograma: {last["MACD_Hist"]:.4f}')
print(f'MA20: ${last["MA20"]:.2f}')
print(f'MA50: ${last["MA50"]:.2f}')
print(f'Soporte: ${last["Support"]:.2f}')
print(f'Resistencia: ${last["Resistance"]:.2f}')
print(f'Volumen: {last["Volume"]:,.0f}')
print()

# Detectar señales
signals = []

# RSI oversold (< 30)
if last['RSI'] < 30:
    signals.append(('LONG', f'RSI en sobreventa ({last["RSI"]:.2f} < 30)'))

# RSI overbought (> 70)
if last['RSI'] > 70:
    signals.append(('SHORT', f'RSI en sobrecompra ({last["RSI"]:.2f} > 70)'))

# MACD cruce alcista
if prev is not None and prev['MACD'] < prev['MACD_Signal'] and last['MACD'] > last['MACD_Signal']:
    signals.append(('LONG', 'MACD cruce alcista'))

# MACD cruce bajista
if prev is not None and prev['MACD'] > prev['MACD_Signal'] and last['MACD'] < last['MACD_Signal']:
    signals.append(('SHORT', 'MACD cruce bajista'))

# Precio cerca de soporte
if last['Close'] <= last['Support'] * 1.005:
    signals.append(('LONG', f'Precio cerca de soporte ${last["Support"]:.2f}'))

# Precio cerca de resistencia
if last['Close'] >= last['Resistance'] * 0.995:
    signals.append(('SHORT', f'Precio cerca de resistencia ${last["Resistance"]:.2f}'))

# Breakout
if last['Close'] > last['Resistance'] and last['Volume'] > df['Volume'].rolling(20).mean().iloc[-1]:
    signals.append(('BREAKOUT', f'Ruptura alcista con volumen'))

if last['Close'] < last['Support'] and last['Volume'] > df['Volume'].rolling(20).mean().iloc[-1]:
    signals.append(('BREAKOUT', f'Ruptura bajista con volumen'))

print('=== SENALES DETECTADAS ===')
if signals:
    for signal, reason in signals:
        print(f'{signal}: {reason}')
else:
    print('No se detectaron señales claras en este periodo.')

# Guardar análisis
analysis = {
    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'price': round(last['Close'], 2),
    'rsi': round(last['RSI'], 2),
    'macd': round(last['MACD'], 4),
    'macd_hist': round(last['MACD_Hist'], 4),
    'ma20': round(last['MA20'], 2),
    'ma50': round(last['MA50'], 2),
    'support': round(last['Support'], 2),
    'resistance': round(last['Resistance'], 2),
    'volume': int(last['Volume']),
    'signals': signals
}

print()
print('=== RESUMEN PARA ALERTA ===')
print(f'Timestamp: {analysis["timestamp"]}')
print(f'Precio: ${analysis["price"]}')
print(f'RSI: {analysis["rsi"]}')
print(f'Señales: {len(signals)}')
