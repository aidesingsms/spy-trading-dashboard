# Sistema de Monitoreo de Mercados - Sub-Agentes

## Fecha de Creación: 2026-06-19
## Propietario: Orlando Osorio (Aidesing Smart Solutions)

---

## Agentes Activos

### 1. Geopolitical Monitor
- **Session Key**: agent:main:subagent:a88b589a-e73c-47dc-9e23-f55f50cc9962
- **Run ID**: cda1d45f-9743-4ae5-b6db-297ffc4556e1
- **Función**: Monitorear noticias geopolíticas de alto impacto
- **Frecuencia**: Cada 30 minutos
- **Cobertura**:
  - Conflictos militares
  - Sanciones económicas
  - Tensiones US-China, Rusia-Ucrania, Israel-Irán
  - Crisis energéticas
  - Inestabilidad política

### 2. FED Monitor
- **Session Key**: agent:main:subagent:51a76248-6237-4370-910b-c8ec22ee97c7
- **Run ID**: d82f4345-9a64-4723-a13f-d4f657634714
- **Función**: Monitorear política monetaria y datos económicos
- **Frecuencia**: Cada 30 minutos
- **Cobertura**:
  - Decisiones de tasas FED
  - Datos CPI, PPI, NFP, GDP, PCE
  - Minutas FOMC
  - Declaraciones de miembros FED
  - Bancos centrales globales

### 3. Market Sentiment Monitor
- **Session Key**: agent:main:subagent:ff0bee8c-75e6-4baa-a59a-0140bfbb44a5
- **Run ID**: 78d0ab0e-8d25-4eb5-ba5b-19f975a5a1c0
- **Función**: Monitorear sentimiento y noticias corporativas
- **Frecuencia**: Cada 30 minutos
- **Cobertura**:
  - Earnings y guidance
  - M&A (fusiones y adquisiciones)
  - Ratings de analistas
  - Regulación (antitrust, FDA)
  - Tendencias redes sociales

---

## Formato de Alertas

### Alerta Geopolítica
```
🌍 ALERTA GEOPOLÍTICA [ALTA/MEDIA/BAJA]
📰 Evento: [descripción detallada]
📈 Impacto esperado: [mercados afectados]
⏰ Horario: [timestamp]
💡 Señal: [COMPRAR/ESPERAR/VENDER]
```

### Alerta FED
```
🏦 ALERTA FED [ALTA/MEDIA/BAJA]
📰 Evento: [descripción detallada]
📈 Impacto esperado: [mercados afectados]
⏰ Horario: [timestamp]
💡 Señal: [COMPRAR/ESPERAR/VENDER]
```

### Alerta Mercado
```
📊 ALERTA MERCADO [ALTA/MEDIA/BAJA]
📰 Evento: [descripción detallada]
📈 Impacto esperado: [acciones/sectores]
⏰ Horario: [timestamp]
💡 Señal: [COMPRAR/ESPERAR/VENDER]
```

---

## Canales de Comunicación

- **Canal Principal**: Telegram (8585127775)
- **Frecuencia de Actualización**: Cada 30 minutos
- **Horario de Operación**: 24/7 (mercados globales)

---

## Acciones por Nivel de Alerta

### ALTA (Rojo)
- Notificar inmediatamente
- Evaluar posiciones abiertas
- Considerar cierre de posiciones riesgosas
- Buscar oportunidades de entrada

### MEDIA (Amarillo)
- Notificar en siguiente ciclo
- Monitorear desarrollo
- Ajustar stops si es necesario
- Preparar posibles entradas

### BAJA (Verde)
- Registrar en log
- Revisar en próximo ciclo
- Sin acción inmediata requerida

---

## Mercados Monitoreados

### Índices
- SPY (S&P 500)
- QQQ (Nasdaq 100)
- DIA (Dow Jones)
- IWM (Russell 2000)

### Sectores
- XLK (Tecnología)
- XLF (Financieros)
- XLE (Energía)
- XLV (Salud)
- XLRE (Bienes Raíces)

### Commodities
- Oro (GLD)
- Petróleo (USO)
- Plata (SLV)

### Volatilidad
- VIX
- VIX3M
- VVIX

---

## Notas

- Los agentes están configurados para ejecutar una vez (mode=run)
- Para monitoreo continuo, se requiere configurar cron jobs
- Las alertas se envían al canal de Telegram configurado
- El sistema puede escalarse agregando más agentes especializados

---

## Próximos Pasos

1. [ ] Configurar cron jobs para ejecución continua
2. [ ] Crear dashboard de alertas
3. [ ] Agregar agente de análisis técnico
4. [ ] Integrar con broker para ejecución automática
5. [ ] Configurar filtros de alertas por relevancia

---

*Documento creado por Kimi Claw para Aidesing Smart Solutions*