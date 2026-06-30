# Range Filter Strategy - Guía de Uso

## 📊 ESTRATEGIA AUTOMATIZADA RANGE FILTER

---

### 🎯 Descripción

Estrategia automatizada basada en el indicador **Range Filter** que:
- Detecta cambios de tendencia con precisión
- Genera señales de compra/venta automáticas
- Gestiona riesgo con TP/SL dinámicos
- Incluye trailing stop opcional

---

### 📥 INSTALACIÓN EN TRADINGVIEW

**Paso 1: Abrir Pine Editor**
1. Ve a https://www.tradingview.com/chart/
2. Abre cualquier gráfico (BTC, SPY, etc.)
3. Click en **"Pine Editor"** (pestaña abajo)

**Paso 2: Copiar Código**
1. Borra todo el código existente
2. Copia el contenido del archivo `range_filter_strategy.pine`
3. Pega en el Pine Editor
4. Click **"Add to Chart"**

**Paso 3: Configurar**
1. Aparecerá el panel de configuración a la derecha
2. Ajusta parámetros según el activo (ver tabla abajo)
3. Click **"Aceptar"**

---

### ⚙️ CONFIGURACIÓN POR ACTIVO

| Activo | Timeframe | Sampling Period | Multiplier | TP% | SL% | Trailing% |
|--------|-----------|-----------------|------------|-----|-----|-----------|
| **BTC/USDT** | 5min | 100 | 3.0 | 4.0% | 2.0% | 2.0% |
| **SPY** | 5min | 50 | 2.5 | 3.0% | 1.5% | 1.5% |
| **QQQ** | 5min | 50 | 2.5 | 3.0% | 1.5% | 1.5% |
| **TSLA** | 5min | 30 | 2.0 | 4.0% | 2.0% | 2.0% |
| **NVDA** | 5min | 40 | 2.5 | 3.5% | 1.8% | 1.8% |

---

### 📊 PARÁMETROS EXPLICADOS

**Strategy Settings:**
- **Start Date**: Fecha de inicio del backtesting
- **TP (%)**: Take Profit en porcentaje (ej: 4.0 = 4%)
- **SL (%)**: Stop Loss en porcentaje (ej: 2.0 = 2%)
- **Use Trailing Stop**: Activa trailing stop
- **Trailing Stop (%)**: % para mover el stop

**Range Filter Settings:**
- **Source**: Precio a usar (close, open, high, low, hl2, hlc3, ohlc4)
- **Sampling Period**: Período de muestreo (100 para BTC 5min)
- **Range Multiplier**: Multiplicador de rango (3.0 para BTC)

**Visual Settings:**
- **Show Buy/Sell Signals**: Mostrar flechas de señales
- **Show Target Bands**: Mostrar bandas superior/inferior
- **Show Trend Background**: Colorear fondo según tendencia

---

### 🎨 SEÑALES VISUALES

| Elemento | Color | Significado |
|----------|-------|-------------|
| **Flecha BUY** | Verde | Señal de compra |
| **Flecha SELL** | Rojo | Señal de venta |
| **Línea Filtro** | Verde | Tendencia alcista |
| **Línea Filtro** | Rojo | Tendencia bajista |
| **Fondo** | Verde claro | Tendencia alcista |
| **Fondo** | Rojo claro | Tendencia bajista |
| **Banda Superior** | Verde transparente | Target de venta |
| **Banda Inferior** | Rojo transparente | Target de compra |

---

### 📈 PANEL DE INFORMACIÓN

En la esquina superior derecha verás:
- **Trend**: Dirección actual (UP/DOWN/NEUTRAL)
- **Filter**: Valor actual del filtro
- **Position**: Posición actual (LONG/SHORT/FLAT)
- **P&L**: Profit/Loss de la operación abierta
- **Equity**: Capital total de la estrategia

---

### 🚨 ALERTAS CONFIGURABLES

**Para configurar alertas:**
1. Click en el reloj **"Alertas"** (arriba a la derecha)
2. Click en **"Range Filter Strategy"**
3. Selecciona condición:
   - 🟢 **Buy Signal**: Alerta en compra
   - 🔴 **Sell Signal**: Alerta en venta
   - ⚡ **Any Signal**: Cualquier señal

**Mensaje de alerta:**
```
Range Filter: BUY signal on {{ticker}} at {{close}}
```

---

### 💰 GESTIÓN DE RIESGO

**Reglas automáticas:**
- Máximo 10% del capital por trade (configurable)
- TP/SL basado en porcentaje
- Trailing stop opcional
- Comisión del 0.1% incluida

**Ejemplo de trade BTC:**
- Entrada: $60,000
- TP (4%): $62,400
- SL (2%): $58,800
- Si activa trailing: Stop se mueve con el precio

---

### 📊 BACKTESTING

**Para hacer backtest:**
1. Selecciona rango de fechas en la parte superior
2. La estrategia muestra automáticamente:
   - Trades ganadores/perdedores
   - Profit factor
   - Drawdown máximo
   - Retorno total

**Interpretación:**
- **Profit Factor > 1.5**: Buena estrategia
- **Drawdown < 20%**: Riesgo aceptable
- **Win Rate > 50%**: Más ganadores que perdedores

---

### 🔧 OPTIMIZACIÓN

**Para optimizar parámetros:**
1. Click derecho en la estrategia
2. Selecciona **"Strategy Tester"**
3. Click en **"Optimize"**
4. Selecciona parámetros a optimizar:
   - Sampling Period: 50-200
   - Multiplier: 1.0-5.0
   - TP%: 1.0-10.0
   - SL%: 0.5-5.0

---

### ⚠️ PRECAUCIONES

1. **No operar en noticias importantes**
2. **Evitar mercados con bajo volumen**
3. **Revisar configuración por activo**
4. **Hacer backtest antes de usar en real**
5. **Usar solo como confirmación, no única señal**

---

### 📱 INTEGRACIÓN CON AIDESING AI

**Alertas webhook (opcional):**
```
{{strategy.order.action}} - {{ticker}} @ {{close}}
```

**Para enviar a Telegram:**
1. Crear webhook en TradingView
2. Configurar endpoint
3. Recibir alertas en @aidesing_alerts

---

### 🚀 PRÓXIMOS PASOS

1. **Probar en demo** primero
2. **Ajustar parámetros** según resultados
3. **Combinar con otros indicadores**
4. **Usar con gestión de riesgo estricta**

---

**¿Necesitas ayuda para configurar algún parámetro específico?** 🔥
