#!/bin/bash
TELEGRAM_BOT_TOKEN="8682815952:AAEYO8E_YbFpOb2i1xmbMvvNntIa9208kOk"
TELEGRAM_CHANNEL="@aidesing_alerts"

cd /root/.openclaw/workspace
openclaw sessions_spawn --agentId main --mode run --runtime subagent --label "geopolitical-check-$(date +%H%M)" --task "Monitorea noticias geopolíticas de última hora que puedan afectar mercados financieros. Busca conflictos, sanciones, tensiones entre potencias, crisis energéticas. Genera alerta si detectas evento de alto impacto. Formato: 🌍 ALERTA [NIVEL] | Evento: [desc] | Impacto: [mercados] | Señal: [acción] | Canal: @aidesing_alerts"
