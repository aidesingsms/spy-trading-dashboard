import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import sys

# Descargar datos de SPY con intervalo de 30 minutos
spy = yf.Ticker('SPY')
df = spy.history(period='5d', interval='30m')

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

# Análisis del último periodo
last = df.iloc[-1]
prev = df.iloc[-2] if len(df) > 1 else None

price = last['Close']
rsi = last['RSI']
macd = last['MACD']
macd_hist = last['MACD_Hist']
ma20 = last['MA20']
ma50 = last['MA50']
support = last['Support']
resistance = last['Resistance']
volume = last['Volume']

# Detectar señales y generar alerta
alert_type = None
alert_reason = []
confidence = "Baja"

# RSI oversold (< 30)
if rsi < 30:
    alert_type = "LONG"
    alert_reason.append(f"RSI en sobreventa ({rsi:.2f} < 30)")
    confidence = "Alta" if rsi < 25 else "Media"

# RSI overbought (> 70)
elif rsi > 70:
    alert_type = "SHORT"
    alert_reason.append(f"RSI en sobrecompra ({rsi:.2f} > 70)")
    confidence = "Alta" if rsi > 75 else "Media"

# MACD cruce alcista
elif prev is not None and prev['MACD'] < prev['MACD_Signal'] and last['MACD'] > last['MACD_Signal']:
    alert_type = "LONG"
    alert_reason.append("MACD cruce alcista")
    confidence = "Media"

# MACD cruce bajista
elif prev is not None and prev['MACD'] > prev['MACD_Signal'] and last['MACD'] < last['MACD_Signal']:
    alert_type = "SHORT"
    alert_reason.append("MACD cruce bajista")
    confidence = "Media"

# Breakout alcista con volumen
elif price > resistance and volume > df['Volume'].rolling(20).mean().iloc[-1]:
    alert_type = "BREAKOUT"
    alert_reason.append(f"Ruptura alcista de ${resistance:.2f} con volumen elevado")
    confidence = "Alta"

# Breakout bajista con volumen
elif price < support and volume > df['Volume'].rolling(20).mean().iloc[-1]:
    alert_type = "BREAKOUT"
    alert_reason.append(f"Ruptura bajista de ${support:.2f} con volumen elevado")
    confidence = "Alta"

# Precio cerca de soporte (sin breakout)
elif price <= support * 1.005:
    alert_type = "LONG"
    alert_reason.append(f"Precio cerca de soporte ${support:.2f}")
    confidence = "Media"

# Precio cerca de resistencia (sin breakout)
elif price >= resistance * 0.995:
    alert_type = "SHORT"
    alert_reason.append(f"Precio cerca de resistencia ${resistance:.2f}")
    confidence = "Media"

# Si no hay señal clara, evaluar tendencia general
if alert_type is None:
    if price > ma20 and price > ma50 and macd_hist > 0:
        alert_type = "LONG"
        alert_reason.append("Tendencia alcista general")
        confidence = "Baja"
    elif price < ma20 and price < ma50 and macd_hist < 0:
        alert_type = "SHORT"
        alert_reason.append("Tendencia bajista general")
        confidence = "Baja"
    else:
        alert_type = "NEUTRAL"
        alert_reason.append("Sin señales claras")
        confidence = "Baja"

# Calcular niveles de entrada, target y stop
if alert_type == "LONG":
    entry = price
    target = resistance if price < resistance else price * 1.02
    stop = support * 0.995 if price > support else price * 0.98
elif alert_type == "SHORT":
    entry = price
    target = support if price > support else price * 0.98
    stop = resistance * 1.005 if price < resistance else price * 1.02
elif alert_type == "BREAKOUT":
    entry = price
    if price > resistance:
        target = price * 1.02
        stop = resistance * 0.995
    else:
        target = price * 0.98
        stop = support * 1.005
else:
    entry = price
    target = price * 1.01
    stop = price * 0.99

# Generar mensaje de alerta
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

alert_message = f"""📈 ALERTA SPY [{alert_type}]
📰 Análisis: {' | '.join(alert_reason)}
💰 Entrada: ${entry:.2f}
🎯 Target: ${target:.2f}
🛑 Stop: ${stop:.2f}
⏰ Horario: {timestamp}
📊 Confianza: {confidence}

📊 Indicadores:
• RSI(14): {rsi:.2f}
• MACD: {macd:.4f} (Hist: {macd_hist:.4f})
• MA20: ${ma20:.2f} | MA50: ${ma50:.2f}
• Soporte: ${support:.2f} | Resistencia: ${resistance:.2f}
• Volumen: {volume:,.0f}
"""

print(alert_message)

# Guardar análisis en archivo
with open('/root/.openclaw/workspace/spy_alert.txt', 'w') as f:
    f.write(alert_message)

print("Alerta guardada en spy_alert.txt")
