# Sistema de Análisis Técnico - Sub-Agentes

## Fecha: 2026-06-19
## Estado: 4/8 agentes creados (límite alcanzado)

---

## Agentes de Análisis Técnico Creados

### 1. SPY Analyzer
- **Session Key**: agent:main:subagent:af327453-7030-4bb1-8f1f-6564035184dd
- **Run ID**: 49746bf1-b12a-404d-a957-0b262402a14b
- **Activo**: SPY (S&P 500 ETF)
- **Indicadores**: RSI, MACD, Volumen, Soportes/Resistencias, Medias Móviles
- **Frecuencia**: Cada 30 minutos
- **Canal**: @aidesing_alerts

### 2. TSLA Analyzer
- **Session Key**: agent:main:subagent:0c840666-0035-4f81-a748-1373420a5b88
- **Run ID**: c5d20ece-48ce-43a1-b9bb-863495764a6e
- **Activo**: TSLA (Tesla)
- **Indicadores**: RSI, MACD, Volumen, Soportes/Resistencias, Medias Móviles
- **Frecuencia**: Cada 30 minutos
- **Canal**: @aidesing_alerts

### 3. NVDA Analyzer
- **Session Key**: agent:main:subagent:b14c6d50-6d96-446e-9157-8bf605caaa90
- **Run ID**: 23a4a179-e3e8-43a4-adb8-d798116fee1b
- **Activo**: NVDA (NVIDIA)
- **Indicadores**: RSI, MACD, Volumen, Soportes/Resistencias, Medias Móviles
- **Frecuencia**: Cada 30 minutos
- **Canal**: @aidesing_alerts

### 4. SPCX Analyzer
- **Session Key**: agent:main:subagent:d6aa9392-499a-458a-a168-8077d48d33c8
- **Run ID**: 0e5996b0-f312-4a92-ab6e-3aa7ae329500
- **Activo**: SPCX (SpaceX)
- **Indicadores**: RSI, MACD, Volumen, Soportes/Resistencias, Medias Móviles
- **Frecuencia**: Cada 30 minutos
- **Canal**: @aidesing_alerts

---

## Agentes Pendientes (Límite de 5 alcanzado)

### 5. NFLX Analyzer
- **Activo**: NFLX (Netflix)
- **Estado**: Pendiente

### 6. Oro Analyzer
- **Activo**: Oro (GC=F / GLD)
- **Estado**: Pendiente

### 7. Plata Analyzer
- **Activo**: Plata (SI=F / SLV)
- **Estado**: Pendiente

### 8. Petróleo Analyzer
- **Activo**: Petróleo (CL=F / USO)
- **Estado**: Pendiente

---

## Formato de Alertas

```
📈 ALERTA [ACTIVO] [LONG/SHORT/BREAKOUT]
📰 Análisis: [descripción técnica]
💰 Entrada: $[precio]
🎯 Target: $[precio]
🛑 Stop: $[precio]
⏰ Horario: [timestamp]
📊 Confianza: [Alta/Media/Baja]
```

---

## Indicadores Técnicos Utilizados

- RSI (14 periodos)
- MACD
- Volumen
- Soportes y Resistencias
- Medias Móviles (20, 50, 200)

---

## Señales de Trading

### LONG
- RSI < 30 (sobrevendido)
- Soporte fuerte
- Divergencia alcista
- Volumen creciente

### SHORT
- RSI > 70 (sobrecomprado)
- Resistencia fuerte
- Divergencia bajista
- Volumen decreciente

### BREAKOUT
- Ruptura de rango con volumen
- Confirmación con cierre
- Stop debajo del breakout

---

## Configuración de Scripts

Los scripts están en:
- /root/.openclaw/workspace/scripts/

Con token del bot:
- TELEGRAM_BOT_TOKEN="8682815952:AAEYO8E_YbFpOb2i1xmbMvvNntIa9208kOk"
- TELEGRAM_CHANNEL="@aidesing_alerts"

---

## Próximos Pasos

1. [ ] Crear agentes pendientes (NFLX, Oro, Plata, Petróleo)
2. [ ] Configurar cron jobs para análisis continuo
3. [ ] Probar alertas de cada agente
4. [ ] Ajustar parámetros de confianza
5. [ ] Agregar más activos si es necesario

---

## Notas

- Límite de 5 agentes simultáneos
- Los agentes restantes se crearán cuando los actuales terminen
- Cada agente analiza cada 30 minutos durante horario de mercado
- Las alertas se envían al canal @aidesing_alerts