#!/bin/bash
# Script de alerta directa por Telegram (sin dependencias)
# Zona horaria: ET (UTC-4)
TELEGRAM_BOT_TOKEN="8682815952:AAEYO8E_YbFpOb2i1xmbMvvNntIa9208kOk"
TELEGRAM_CHANNEL="@aidesing_alerts"

# Función para enviar mensaje
send_alert() {
    local message="$1"
    curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
        -d "chat_id=${TELEGRAM_CHANNEL}" \
        -d "text=${message}" \
        -d "parse_mode=HTML" > /dev/null 2>&1
}

# Hora actual en ET
HORA_ET=$(TZ="America/New_York" date '+%I:%M %p ET')
FECHA_ET=$(TZ="America/New_York" date '+%Y-%m-%d')

# Alerta de mercado
send_alert "📈 <b>ALERTA MERCADO</b>

⏰ ${HORA_ET}
📅 ${FECHA_ET}

🔄 Mercado activo
📊 Monitoreo en curso

Próxima actualización: 30 min"

echo "Alerta enviada: ${HORA_ET} ET" >> /tmp/alert_log.txt
