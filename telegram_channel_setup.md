# Configuración Canal de Alertas Telegram

## Fecha: 2026-06-19
## Estado: Esperando ID del canal

---

## Pasos para Configurar

### 1. Crear Canal en Telegram
- Nombre sugerido: "Aidesing Trading Alerts"
- Tipo: Privado (recomendado)
- Descripción: Alertas automáticas de trading

### 2. Añadir Bot como Administrador
- Bot: @AidesingAIBot
- Permisos requeridos:
  - Enviar mensajes
  - Enviar medios
  - Añadir miembros

### 3. Obtener ID del Canal
- Añadir @userinfobot al canal
- Obtener ID (formato: -1001234567890)

### 4. Configurar en Sistema
- Actualizar scripts con nuevo ID
- Probar envío de alertas
- Activar monitoreo automático

---

## Formato de Alertas en Canal

```
🌍 ALERTA GEOPOLÍTICA [ALTA]
📰 Evento: [descripción]
📈 Impacto: [mercados afectados]
⏰ Horario: [timestamp]
💡 Señal: [acción]
```

---

## Scripts a Actualizar

- /root/.openclaw/workspace/scripts/run_geopolitical.sh
- /root/.openclaw/workspace/scripts/run_fed.sh
- /root/.openclaw/workspace/scripts/run_market.sh

---

## Notas

- Canal privado recomendado por seguridad
- Solo administradores pueden ver alertas
- Bot enviará alertas automáticas según cron jobs configurados
- Logs se mantienen en /root/.openclaw/workspace/logs/