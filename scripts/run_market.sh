#!/bin/bash
TELEGRAM_BOT_TOKEN="8682815952:AAEYO8E_YbFpOb2i1xmbMvvNntIa9208kOk"
TELEGRAM_CHANNEL="@aidesing_alerts"

cd /root/.openclaw/workspace
openclaw sessions_spawn --agentId main --mode run --runtime subagent --label "market-check-$(date +%H%M)" --task "Monitorea earnings, M&A, guidance corporativo, cambios de ratings, noticias de regulación, tendencias redes sociales. Genera alerta si detectas evento que pueda mover acciones >2%. Formato: 📊 ALERTA [NIVEL] | Evento: [desc] | Impacto: [acciones] | Señal: [acción] | Canal: @aidesing_alerts"